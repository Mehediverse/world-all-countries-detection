"""
Bulk Country Detector for Phone Numbers
Supports Excel, CSV, PDF files with advanced area code detection
"""

import re
import csv
import sys
from collections import Counter
from countrydetect_advanced import detect_country_advanced, detect_country_with_confidence, get_country_name, bulk_detect

def extract_phone_numbers_from_text(text):
    """Extract phone numbers from text using regex patterns"""
    # Pattern: 10-15 digits, possibly with + prefix and spaces/dashes
    pattern = r'\+?[\d\s\-\(\)]{10,20}'
    matches = re.findall(pattern, text)
    
    # Filter to only keep valid-looking numbers
    numbers = []
    for match in matches:
        digits = ''.join(filter(str.isdigit, match))
        if 10 <= len(digits) <= 15:
            numbers.append(match.strip())
    
    return numbers


def process_csv_bulk(file_path, output_file=None, show_confidence=False):
    """
    Process CSV file with phone numbers - optimized for 100k+ rows
    
    Args:
        file_path (str): Path to CSV file
        output_file (str): Optional output CSV file path
        show_confidence (bool): Include confidence level
    
    Returns:
        dict: Statistics about processed numbers
    """
    print(f"📄 Processing CSV: {file_path}")
    print("=" * 100)
    
    results = []
    phone_column = None
    total_rows = 0
    detected_count = 0
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        
        # Try to find header and phone column
        try:
            header = next(reader)
            print(f"Header: {header}")
            
            # Find column with "Number" or "Phone" in name
            for i, col in enumerate(header):
                if 'number' in col.lower() or 'phone' in col.lower():
                    phone_column = i
                    print(f"✓ Found phone column: '{col}' at index {i}")
                    break
        except StopIteration:
            print("⚠️  No header found, will search all columns")
        
        # Process rows
        for row_num, row in enumerate(reader, start=1):
            total_rows += 1
            
            # Extract phone number
            phone_number = None
            if phone_column is not None and phone_column < len(row):
                phone_number = row[phone_column]
            else:
                # Search all columns for phone-like data
                for cell in row:
                    if cell and any(char.isdigit() for char in cell):
                        phone_number = cell
                        break
            
            if phone_number:
                # Detect country
                if show_confidence:
                    country, confidence = detect_country_with_confidence(phone_number)
                    country_name = get_country_name(country)
                    results.append({
                        'row': row_num,
                        'number': phone_number,
                        'country': country,
                        'country_name': country_name,
                        'confidence': confidence
                    })
                else:
                    country = detect_country_advanced(phone_number)
                    country_name = get_country_name(country)
                    results.append({
                        'row': row_num,
                        'number': phone_number,
                        'country': country,
                        'country_name': country_name
                    })
                
                if country != "🌍 Unknown":
                    detected_count += 1
                
                # Progress indicator for large files
                if row_num % 1000 == 0:
                    print(f"  Processed {row_num:,} rows... ({detected_count:,} detected)")
    
    print()
    print(f"✓ Completed: {total_rows:,} rows processed")
    print(f"✓ Detected: {detected_count:,} countries ({detected_count*100//total_rows if total_rows > 0 else 0}%)")
    print()
    
    # Statistics
    country_counts = Counter(r['country_name'] for r in results)
    print("📊 Country Distribution (Top 10):")
    print("-" * 100)
    for country, count in country_counts.most_common(10):
        percentage = count * 100 / total_rows if total_rows > 0 else 0
        print(f"  {country:30} : {count:6,} numbers ({percentage:5.2f}%)")
    
    # Save to output file
    if output_file:
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            if show_confidence:
                fieldnames = ['row', 'number', 'country', 'country_name', 'confidence']
            else:
                fieldnames = ['row', 'number', 'country', 'country_name']
            
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
        
        print()
        print(f"💾 Results saved to: {output_file}")
    
    return {
        'total_rows': total_rows,
        'detected': detected_count,
        'unknown': total_rows - detected_count,
        'country_distribution': dict(country_counts),
        'results': results
    }


def process_excel_bulk(file_path, output_file=None, show_confidence=False):
    """
    Process Excel file with phone numbers - optimized for 100k+ rows
    """
    try:
        import pandas as pd
    except ImportError:
        print("❌ pandas not installed. Install with: pip install pandas openpyxl")
        return None
    
    print(f"📊 Processing Excel: {file_path}")
    print("=" * 100)
    
    # Read Excel file
    df = pd.read_excel(file_path)
    total_rows = len(df)
    
    print(f"Columns: {list(df.columns)}")
    print(f"Total rows: {total_rows:,}")
    print()
    
    # Find phone number column
    phone_col = None
    for col in df.columns:
        if 'number' in str(col).lower() or 'phone' in str(col).lower():
            phone_col = col
            print(f"✓ Found phone column: '{col}'")
            break
    
    if phone_col is None:
        print("⚠️  No obvious phone column, using first column with digits")
        for col in df.columns:
            if df[col].astype(str).str.contains(r'\d', regex=True).any():
                phone_col = col
                print(f"✓ Using column: '{col}'")
                break
    
    if phone_col is None:
        print("❌ No phone column found!")
        return None
    
    # Process numbers
    print("Processing...")
    if show_confidence:
        df['Country_Full'] = df[phone_col].apply(lambda x: detect_country_with_confidence(str(x))[0])
        df['Country_Name'] = df['Country_Full'].apply(get_country_name)
        df['Confidence'] = df[phone_col].apply(lambda x: detect_country_with_confidence(str(x))[1])
    else:
        df['Country_Full'] = df[phone_col].apply(lambda x: detect_country_advanced(str(x)))
        df['Country_Name'] = df['Country_Full'].apply(get_country_name)
    
    detected = (df['Country_Name'] != 'Unknown').sum()
    
    print()
    print(f"✓ Completed: {total_rows:,} rows processed")
    print(f"✓ Detected: {detected:,} countries ({detected*100//total_rows}%)")
    print()
    
    # Statistics
    country_counts = df['Country_Name'].value_counts()
    print("📊 Country Distribution (Top 10):")
    print("-" * 100)
    for country, count in country_counts.head(10).items():
        percentage = count * 100 / total_rows
        print(f"  {country:30} : {count:6,} numbers ({percentage:5.2f}%)")
    
    # Save output
    if output_file:
        if output_file.endswith('.csv'):
            df.to_csv(output_file, index=False, encoding='utf-8')
        else:
            df.to_excel(output_file, index=False)
        print()
        print(f"💾 Results saved to: {output_file}")
    
    return df


def process_pdf_bulk(file_path, output_file=None):
    """
    Extract and process phone numbers from PDF file
    """
    try:
        import PyPDF2
    except ImportError:
        print("❌ PyPDF2 not installed. Install with: pip install PyPDF2")
        return None
    
    print(f"📑 Processing PDF: {file_path}")
    print("=" * 100)
    
    # Extract text from PDF
    all_text = ""
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        total_pages = len(pdf_reader.pages)
        
        print(f"Total pages: {total_pages}")
        print("Extracting text...")
        
        for page_num in range(total_pages):
            page = pdf_reader.pages[page_num]
            all_text += page.extract_text() + "\n"
            
            if (page_num + 1) % 10 == 0:
                print(f"  Extracted {page_num + 1}/{total_pages} pages...")
    
    # Extract phone numbers
    print("Extracting phone numbers...")
    phone_numbers = extract_phone_numbers_from_text(all_text)
    
    print(f"✓ Found {len(phone_numbers):,} phone numbers")
    print()
    
    # Detect countries
    print("Detecting countries...")
    results = []
    detected_count = 0
    
    for i, number in enumerate(phone_numbers, 1):
        country = detect_country_advanced(number)
        country_name = get_country_name(country)
        
        results.append({
            'number': number,
            'country': country,
            'country_name': country_name
        })
        
        if country != "🌍 Unknown":
            detected_count += 1
        
        if i % 1000 == 0:
            print(f"  Processed {i:,}/{len(phone_numbers):,} numbers...")
    
    print()
    print(f"✓ Detected: {detected_count:,} countries ({detected_count*100//len(phone_numbers) if phone_numbers else 0}%)")
    print()
    
    # Statistics
    country_counts = Counter(r['country_name'] for r in results)
    print("📊 Country Distribution (Top 10):")
    print("-" * 100)
    for country, count in country_counts.most_common(10):
        percentage = count * 100 / len(phone_numbers) if phone_numbers else 0
        print(f"  {country:30} : {count:6,} numbers ({percentage:5.2f}%)")
    
    # Save output
    if output_file:
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['number', 'country', 'country_name'])
            writer.writeheader()
            writer.writerows(results)
        print()
        print(f"💾 Results saved to: {output_file}")
    
    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("╔" + "=" * 98 + "╗")
        print("║" + " " * 25 + "BULK COUNTRY DETECTOR FOR 100K+ PHONE NUMBERS" + " " * 27 + "║")
        print("╚" + "=" * 98 + "╝")
        print()
        print("Usage:")
        print("  python bulk_country_detector.py <input_file> [output_file] [--confidence]")
        print()
        print("Supported formats:")
        print("  • CSV files (.csv)")
        print("  • Excel files (.xlsx, .xls)")
        print("  • PDF files (.pdf)")
        print()
        print("Options:")
        print("  --confidence    Include confidence level in results")
        print()
        print("Examples:")
        print("  python bulk_country_detector.py \"GAZA IPRN  My SMS Numbers.csv\"")
        print("  python bulk_country_detector.py input.xlsx output.csv --confidence")
        print("  python bulk_country_detector.py numbers.pdf results.csv")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith('--') else None
    show_confidence = '--confidence' in sys.argv
    
    # Auto-generate output filename if not provided
    if not output_file:
        output_file = input_file.rsplit('.', 1)[0] + '_detected.csv'
    
    print()
    
    # Process based on file type
    if input_file.endswith('.csv'):
        process_csv_bulk(input_file, output_file, show_confidence)
    elif input_file.endswith(('.xlsx', '.xls')):
        process_excel_bulk(input_file, output_file, show_confidence)
    elif input_file.endswith('.pdf'):
        process_pdf_bulk(input_file, output_file)
    else:
        print(f"❌ Unsupported file format: {input_file}")
        sys.exit(1)
    
    print()
    print("✅ Processing complete!")
    print()

