"""
Process phone numbers from Excel, CSV, or PDF files and detect countries
Usage: python process_phone_files.py <file_path>
"""

import sys
import csv
from countrydetect_advanced import detect_country_advanced, get_country_name

def process_csv_file(file_path):
    """Process CSV file and detect countries for phone numbers"""
    results = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        # Try to detect if there's a header
        sample = f.read(1024)
        f.seek(0)
        
        has_header = csv.Sniffer().has_header(sample)
        reader = csv.reader(f)
        
        if has_header:
            header = next(reader)
            print(f"CSV Header: {header}")
            print("-" * 80)
        
        for row_num, row in enumerate(reader, start=1):
            # Process each cell in the row
            for col_num, cell in enumerate(row):
                # Check if cell contains a phone number (has digits)
                if cell and any(char.isdigit() for char in cell):
                    country = detect_country_advanced(cell)
                    country_name = get_country_name(country)
                    
                    results.append({
                        'row': row_num,
                        'col': col_num,
                        'number': cell,
                        'country': country,
                        'country_name': country_name
                    })
                    
                    print(f"Row {row_num:4}, Col {col_num}: {cell:20} → {country} ({country_name})")
    
    return results

def process_excel_file(file_path):
    """Process Excel file using pandas"""
    try:
        import pandas as pd
    except ImportError:
        print("❌ pandas not installed. Install with: pip install pandas openpyxl")
        return []
    
    # Read Excel file
    df = pd.read_excel(file_path)
    
    results = []
    
    # Add country detection columns
    for col in df.columns:
        # Check if column contains phone numbers
        sample = df[col].astype(str).iloc[0] if len(df) > 0 else ""
        if any(char.isdigit() for char in str(sample)):
            # Add country columns
            country_col = f"{col}_Country"
            df[country_col] = df[col].astype(str).apply(detect_country_advanced)
            df[f"{col}_Country_Name"] = df[country_col].apply(get_country_name)
    
    # Print results
    print(df)
    
    # Save to new Excel file
    output_file = file_path.replace('.xlsx', '_with_countries.xlsx').replace('.xls', '_with_countries.xlsx')
    df.to_excel(output_file, index=False)
    print()
    print(f"✅ Saved results to: {output_file}")
    
    return df

def process_text_file(file_path):
    """Process plain text file with phone numbers"""
    results = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if line and any(char.isdigit() for char in line):
                country = detect_country_advanced(line)
                country_name = get_country_name(country)
                
                results.append({
                    'line': line_num,
                    'number': line,
                    'country': country,
                    'country_name': country_name
                })
                
                print(f"Line {line_num:4}: {line:20} → {country} ({country_name})")
    
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python process_phone_files.py <file_path>")
        print()
        print("Supported formats:")
        print("  • CSV files (.csv)")
        print("  • Excel files (.xlsx, .xls) - requires pandas")
        print("  • Text files (.txt)")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    print("=" * 80)
    print(f"PROCESSING FILE: {file_path}")
    print("=" * 80)
    print()
    
    if file_path.endswith('.csv'):
        results = process_csv_file(file_path)
    elif file_path.endswith(('.xlsx', '.xls')):
        results = process_excel_file(file_path)
    elif file_path.endswith('.txt'):
        results = process_text_file(file_path)
    else:
        print(f"❌ Unsupported file format: {file_path}")
        print("Supported: .csv, .xlsx, .xls, .txt")
        sys.exit(1)
    
    print()
    print("=" * 80)
    print("✅ Processing complete!")
    print("=" * 80)
