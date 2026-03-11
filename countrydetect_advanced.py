"""
Advanced Country Detection Module with Area Code Support
Handles 100k+ phone numbers with precise detection for shared country codes
"""

from countrydetect import COUNTRY_CODES, COUNTRY_MAP, detect_country as basic_detect, get_country_name

# ============================================================================
# ADVANCED AREA CODE RULES for Shared Prefixes
# ============================================================================

# Russia (+7) vs Kazakhstan (+7) - Area Code Detection
RUSSIA_AREA_CODES = [
    # Moscow and region
    '495', '499', '496', '498',
    # Saint Petersburg
    '812',
    # Major cities
    '343',  # Yekaterinburg
    '383',  # Novosibirsk
    '846',  # Samara
    '861',  # Krasnodar
    '843',  # Kazan
    '831',  # Nizhny Novgorod
    '8412', # Penza
    '4162', # Blagoveshchensk
    '4232', # Vladivostok
    '3852', # Barnaul
    # Mobile operators in Russia (9XX format after +7)
    '900', '901', '902', '903', '904', '905', '906', '908', '909',
    '910', '911', '912', '913', '914', '915', '916', '917', '918', '919',
    '920', '921', '922', '923', '924', '925', '926', '927', '928', '929',
    '930', '931', '932', '933', '934', '936', '937', '938', '939',
    '950', '951', '952', '953', '954', '955', '956', '958', '960',
    '961', '962', '963', '964', '965', '966', '967', '968', '969',
    '970', '971', '977', '978', '980', '981', '982', '983', '984',
    '985', '986', '987', '988', '989', '991', '992', '993', '994',
    '995', '996', '997', '999',
]

KAZAKHSTAN_AREA_CODES = [
    # Kazakhstan cities
    '7172',  # Nur-Sultan (Astana)
    '727',   # Almaty
    '7272',  # Almaty
    '7142',  # Shymkent
    '7132',  # Aktobe
    '7152',  # Karaganda
    '7212',  # Pavlodar
    # Mobile operators in Kazakhstan (7XX format after +7)
    '700', '701', '702', '705', '707', '708', '747', '750', '751', '760', '761', '762', '763', '764', '771', '775', '776', '777', '778',
]

# USA (+1) vs Canada (+1) - Area Code Detection
USA_AREA_CODES = [
    # Major USA area codes (sample - comprehensive list)
    '201', '202', '203', '205', '206', '207', '208', '209', '210', '212', '213', '214', '215', '216', '217', '218', '219',
    '220', '223', '224', '225', '227', '228', '229', '231', '234', '239', '240', '248', '251', '252', '253', '254', '256',
    '260', '262', '267', '269', '270', '272', '274', '276', '279', '281', '283', '301', '302', '303', '304', '305', '307',
    '308', '309', '310', '312', '313', '314', '315', '316', '317', '318', '319', '320', '321', '323', '325', '326', '327',
    '330', '331', '332', '334', '336', '337', '339', '341', '346', '347', '351', '352', '360', '361', '364', '380', '385',
    '386', '401', '402', '404', '405', '406', '407', '408', '409', '410', '412', '413', '414', '415', '417', '419', '423',
    '424', '425', '430', '432', '434', '435', '440', '442', '443', '447', '458', '463', '464', '469', '470', '475', '478',
    '479', '480', '484', '501', '502', '503', '504', '505', '507', '508', '509', '510', '512', '513', '515', '516', '517',
    '518', '520', '530', '531', '534', '539', '540', '541', '551', '557', '559', '561', '562', '563', '564', '567', '570',
    '571', '572', '573', '574', '575', '580', '582', '585', '586', '601', '602', '603', '605', '606', '607', '608', '609',
    '610', '612', '614', '615', '616', '617', '618', '619', '620', '623', '626', '628', '629', '630', '631', '636', '640',
    '641', '646', '650', '651', '657', '659', '660', '661', '662', '667', '669', '678', '680', '681', '682', '689', '701',
    '702', '703', '704', '706', '707', '708', '712', '713', '714', '715', '716', '717', '718', '719', '720', '724', '725',
    '727', '730', '731', '732', '734', '737', '740', '743', '747', '754', '757', '760', '762', '763', '765', '769', '770',
    '772', '773', '774', '775', '779', '781', '785', '786', '801', '802', '803', '804', '805', '806', '808', '810', '812',
    '813', '814', '815', '816', '817', '818', '828', '830', '831', '832', '838', '843', '845', '847', '848', '850', '854',
    '856', '857', '858', '859', '860', '862', '863', '864', '865', '870', '872', '878', '901', '903', '904', '906', '907',
    '908', '909', '910', '912', '913', '914', '915', '916', '917', '918', '919', '920', '925', '928', '929', '930', '931',
    '934', '936', '937', '938', '940', '941', '945', '947', '949', '951', '952', '954', '956', '959', '970', '971', '972',
    '973', '975', '978', '979', '980', '984', '985', '989',
]

CANADA_AREA_CODES = [
    # Major Canada area codes
    '204', '226', '236', '249', '250', '289', '306', '343', '365', '367', '403', '416', '418', '431', '437', '438',
    '450', '468', '474', '506', '514', '519', '548', '579', '581', '584', '587', '604', '613', '639', '647', '672',
    '705', '709', '742', '753', '778', '780', '782', '807', '819', '825', '867', '873', '902', '905',
]

# UK (+44) territories - more specific detection
UK_AREA_CODES = [
    '20',   # London
    '113', '114', '115', '116', '117', '118', '121', '131', '141', '151', '161',  # Major cities
    '1202', '1203', '1204', '1205', '1206', '1207', '1208', '1209',  # Geographic
    '7',    # Mobile (most UK mobiles start with 07)
]

GUERNSEY_CODES = ['1481']
JERSEY_CODES = ['1534']
ISLE_OF_MAN_CODES = ['1624']

# ============================================================================
# +47: Norway vs Svalbard and Jan Mayen vs Bouvet Island
# ============================================================================
NORWAY_AREA_CODES = [
    '2', '3', '5', '6', '7',  # Major geographic areas (Oslo=2, Bergen=5, Trondheim=7, etc.)
    '9',  # Mobile prefix
    '40', '41', '45', '46', '47', '48', '49',  # Mobile operators
]

SVALBARD_AREA_CODES = ['79']  # Svalbard and Jan Mayen

# Bouvet Island is uninhabited (no phone service - defaults to Norway)

# ============================================================================
# +61: Australia vs Christmas Island vs Cocos (Keeling) Islands
# ============================================================================
AUSTRALIA_AREA_CODES = [
    '2',  # New South Wales, ACT
    '3',  # Victoria, Tasmania
    '4',  # Mobile (all Australian mobiles)
    '7',  # Queensland
    '8',  # South Australia, Western Australia, Northern Territory (but not 89162, 89164)
]

CHRISTMAS_ISLAND_CODES = ['89164']
COCOS_ISLANDS_CODES = ['89162']

# ============================================================================
# +64: New Zealand vs Pitcairn Islands
# ============================================================================
NEW_ZEALAND_AREA_CODES = [
    '3',  # South Island
    '4',  # Wellington region
    '6',  # Lower North Island
    '7',  # Hamilton/Waikato/Bay of Plenty
    '9',  # Auckland region
    '20', '21', '22', '27', '28', '29',  # Mobile
]

# Pitcairn Islands use satellite phones (no standard area code - defaults to New Zealand)

# ============================================================================
# +212: Morocco vs Western Sahara
# ============================================================================
MOROCCO_AREA_CODES = [
    '5',  # All Moroccan landlines and some mobile start with 5
    '6',  # Mobile networks
    '7',  # Mobile networks
]

WESTERN_SAHARA_CODES = ['5288', '5289']  # Western Sahara (disputed territory)

# ============================================================================
# +262: Réunion vs Mayotte vs French Southern Territories
# ============================================================================
REUNION_AREA_CODES = [
    '262',  # Réunion landlines
    '692', '693',  # Réunion mobile
]

MAYOTTE_AREA_CODES = [
    '269',  # Mayotte landlines
    '639',  # Mayotte mobile
]

# French Southern Territories - research stations only (defaults to Réunion)

# ============================================================================
# +500: Falkland Islands vs South Georgia
# ============================================================================
FALKLAND_ISLANDS_CODES = ['2', '3', '5', '6']

# South Georgia - research stations only (defaults to Falklands)

# ============================================================================
# +590: Guadeloupe vs Saint Barthélemy vs Saint Martin
# ============================================================================
GUADELOUPE_CODES = ['590']

SAINT_MARTIN_BARTHELEMY_CODES = ['690']  # Both territories share this

# ============================================================================
# +599: Curaçao vs Bonaire/Sint Eustatius/Saba
# ============================================================================
CURACAO_CODES = ['9']  # Curaçao numbers start with 9

BONAIRE_BES_CODES = ['3', '4', '7']  # Bonaire, Sint Eustatius, Saba

# ============================================================================
# +672: Antarctica vs Norfolk Island vs Heard/McDonald Islands
# ============================================================================
ANTARCTICA_CODES = ['1']  # Research stations

NORFOLK_ISLAND_CODES = ['3']  # Norfolk Island

# Heard/McDonald Islands - uninhabited (defaults to Antarctica)

def detect_country_advanced(phone_number):
    """
    Advanced country detection with area code support for shared prefixes.
    
    Handles ALL 12 shared country codes:
    - Russia (+7) vs Kazakhstan (+7)
    - USA (+1) vs Canada (+1) 
    - UK (+44) vs Channel Islands and territories
    - Norway (+47) vs Svalbard
    - Australia (+61) vs Christmas Island vs Cocos Islands
    - New Zealand (+64) vs Pitcairn Islands
    - Morocco (+212) vs Western Sahara
    - Réunion (+262) vs Mayotte
    - Falkland Islands (+500) vs South Georgia
    - Guadeloupe (+590) vs Saint Martin/Barthélemy
    - Curaçao (+599) vs Bonaire/BES
    - Antarctica (+672) vs Norfolk Island
    
    Args:
        phone_number (str): Phone number to detect
    
    Returns:
        str: Country name with flag emoji (e.g., "🇺🇸 United States")
    """
    if not phone_number:
        return "🌍 Unknown"
    
    # Normalize: remove all non-digits
    import re
    cleaned = re.sub(r'[^\d]', '', str(phone_number))
    
    if not cleaned:
        return "🌍 Unknown"
    
    # ========================================================================
    # Handle +7 (Russia vs Kazakhstan)
    # ========================================================================
    if cleaned.startswith('7'):
        remainder = cleaned[1:]
        
        if len(remainder) >= 3:
            # Check Russia area codes
            for code in RUSSIA_AREA_CODES:
                if remainder.startswith(code):
                    return "🇷🇺 Russia"
            
            # Check Kazakhstan area codes
            for code in KAZAKHSTAN_AREA_CODES:
                if remainder.startswith(code):
                    return "🇰🇿 Kazakhstan"
            
            # Default to Russia for +7 (most common)
            return "🇷🇺 Russia"
    
    # ========================================================================
    # Handle +1 (USA vs Canada)
    # ========================================================================
    if cleaned.startswith('1') and len(cleaned) >= 11:
        area_code = cleaned[1:4]
        
        # Check USA area codes
        if area_code in USA_AREA_CODES:
            return "🇺🇸 United States"
        
        # Check Canada area codes
        if area_code in CANADA_AREA_CODES:
            return "🇨🇦 Canada"
        
        # Default to USA for +1 (more common)
        return "🇺🇸 United States"
    
    # ========================================================================
    # Handle +44 (UK vs territories)
    # ========================================================================
    if cleaned.startswith('44'):
        remainder = cleaned[2:]
        
        # Check for specific territories
        for code in GUERNSEY_CODES:
            if remainder.startswith(code):
                return "🇬🇬 Guernsey"
        
        for code in JERSEY_CODES:
            if remainder.startswith(code):
                return "🇯🇪 Jersey"
        
        for code in ISLE_OF_MAN_CODES:
            if remainder.startswith(code):
                return "🇮🇲 Isle of Man"
        
        # Otherwise it's UK
        return "🇬🇧 United Kingdom"
    
    # ========================================================================
    # Handle +47 (Norway vs Svalbard and Jan Mayen)
    # ========================================================================
    if cleaned.startswith('47'):
        remainder = cleaned[2:]
        
        # Check Svalbard
        for code in SVALBARD_AREA_CODES:
            if remainder.startswith(code):
                return "🇸🇯 Svalbard and Jan Mayen"
        
        # Check Norway area codes
        for code in NORWAY_AREA_CODES:
            if remainder.startswith(code):
                return "🇳🇴 Norway"
        
        # Default to Norway
        return "🇳🇴 Norway"
    
    # ========================================================================
    # Handle +61 (Australia vs Christmas Island vs Cocos Islands)
    # ========================================================================
    if cleaned.startswith('61'):
        remainder = cleaned[2:]
        
        # Check Christmas Island (specific code)
        for code in CHRISTMAS_ISLAND_CODES:
            if remainder.startswith(code):
                return "🇨🇽 Christmas Island"
        
        # Check Cocos Islands (specific code)
        for code in COCOS_ISLANDS_CODES:
            if remainder.startswith(code):
                return "🇨🇨 Cocos (Keeling) Islands"
        
        # Check Australia area codes
        for code in AUSTRALIA_AREA_CODES:
            if remainder.startswith(code):
                return "🇦🇺 Australia"
        
        # Default to Australia
        return "🇦🇺 Australia"
    
    # ========================================================================
    # Handle +64 (New Zealand vs Pitcairn Islands)
    # ========================================================================
    if cleaned.startswith('64'):
        remainder = cleaned[2:]
        
        # Check New Zealand area codes
        for code in NEW_ZEALAND_AREA_CODES:
            if remainder.startswith(code):
                return "🇳🇿 New Zealand"
        
        # Default to New Zealand (Pitcairn uses satellite - no standard code)
        return "🇳🇿 New Zealand"
    
    # ========================================================================
    # Handle +212 (Morocco vs Western Sahara)
    # ========================================================================
    if cleaned.startswith('212'):
        remainder = cleaned[3:]
        
        # Check Western Sahara (specific codes)
        for code in WESTERN_SAHARA_CODES:
            if remainder.startswith(code):
                return "🇪🇭 Western Sahara"
        
        # Check Morocco area codes
        for code in MOROCCO_AREA_CODES:
            if remainder.startswith(code):
                return "🇲🇦 Morocco"
        
        # Default to Morocco
        return "🇲🇦 Morocco"
    
    # ========================================================================
    # Handle +262 (Réunion vs Mayotte)
    # ========================================================================
    if cleaned.startswith('262'):
        remainder = cleaned[3:]
        
        # Check Mayotte area codes
        for code in MAYOTTE_AREA_CODES:
            if remainder.startswith(code):
                return "🇾🇹 Mayotte"
        
        # Check Réunion area codes
        for code in REUNION_AREA_CODES:
            if remainder.startswith(code):
                return "🇷🇪 Réunion"
        
        # Default to Réunion
        return "🇷🇪 Réunion"
    
    # ========================================================================
    # Handle +500 (Falkland Islands vs South Georgia)
    # ========================================================================
    if cleaned.startswith('500'):
        remainder = cleaned[3:]
        
        # Check Falkland Islands codes
        for code in FALKLAND_ISLANDS_CODES:
            if remainder.startswith(code):
                return "🇫🇰 Falkland Islands"
        
        # Default to Falkland Islands (South Georgia has no standard service)
        return "🇫🇰 Falkland Islands"
    
    # ========================================================================
    # Handle +590 (Guadeloupe vs Saint Martin vs Saint Barthélemy)
    # ========================================================================
    if cleaned.startswith('590'):
        remainder = cleaned[3:]
        
        # Check Saint Martin/Barthélemy
        for code in SAINT_MARTIN_BARTHELEMY_CODES:
            if remainder.startswith(code):
                return "🇲🇫 Saint Martin"  # Could be Saint Barthélemy too
        
        # Check Guadeloupe
        for code in GUADELOUPE_CODES:
            if remainder.startswith(code):
                return "🇬🇵 Guadeloupe"
        
        # Default to Guadeloupe
        return "🇬🇵 Guadeloupe"
    
    # ========================================================================
    # Handle +599 (Curaçao vs Bonaire/Sint Eustatius/Saba)
    # ========================================================================
    if cleaned.startswith('599'):
        remainder = cleaned[3:]
        
        # Check Curaçao
        for code in CURACAO_CODES:
            if remainder.startswith(code):
                return "🇨🇼 Curaçao"
        
        # Check Bonaire/BES
        for code in BONAIRE_BES_CODES:
            if remainder.startswith(code):
                return "🇧🇶 Bonaire, Sint Eustatius and Saba"
        
        # Default to Curaçao
        return "🇨🇼 Curaçao"
    
    # ========================================================================
    # Handle +672 (Antarctica vs Norfolk Island)
    # ========================================================================
    if cleaned.startswith('672'):
        remainder = cleaned[3:]
        
        # Check Norfolk Island
        for code in NORFOLK_ISLAND_CODES:
            if remainder.startswith(code):
                return "🇳🇫 Norfolk Island"
        
        # Check Antarctica
        for code in ANTARCTICA_CODES:
            if remainder.startswith(code):
                return "🇦🇶 Antarctica"
        
        # Default to Antarctica
        return "🇦🇶 Antarctica"
    
    # ========================================================================
    # All other countries: use basic detection
    # ========================================================================
    return basic_detect(phone_number)


def detect_country_with_confidence(phone_number):
    """
    Detect country and provide confidence level.
    
    Returns:
        tuple: (country_str, confidence_level)
        confidence_level: "high", "medium", "low"
    """
    result = detect_country_advanced(phone_number)
    
    # Determine confidence
    if result == "🌍 Unknown":
        return (result, "none")
    
    cleaned = ''.join(filter(str.isdigit, str(phone_number)))
    
    # High confidence: unique prefix or area code matched
    if cleaned.startswith('93'):  # Afghanistan
        return (result, "high")
    elif cleaned.startswith('7'):  # Russia/Kazakhstan - area code matched
        return (result, "high" if any(cleaned[1:].startswith(c) for c in RUSSIA_AREA_CODES + KAZAKHSTAN_AREA_CODES) else "medium")
    elif cleaned.startswith('1'):  # USA/Canada - area code matched
        area = cleaned[1:4]
        return (result, "high" if area in USA_AREA_CODES or area in CANADA_AREA_CODES else "medium")
    else:
        return (result, "high")


# Convenience function
def bulk_detect(phone_numbers, show_confidence=False):
    """
    Detect countries for a list of phone numbers efficiently.
    
    Args:
        phone_numbers (list): List of phone number strings
        show_confidence (bool): Include confidence level in results
    
    Returns:
        list: List of tuples (number, country, [confidence])
    """
    results = []
    for number in phone_numbers:
        if show_confidence:
            country, confidence = detect_country_with_confidence(number)
            results.append((number, country, confidence))
        else:
            country = detect_country_advanced(number)
            results.append((number, country))
    return results
