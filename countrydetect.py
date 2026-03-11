"""
Country Detection Module
Provides country code mapping and detection functions for phone numbers
"""

COUNTRY_CODES = [
    ('Afghanistan', 'AF', '93', '🇦🇫'),
    ('Albania', 'AL', '355', '🇦🇱'),
    ('Algeria', 'DZ', '213', '🇩🇿'),
    ('American Samoa', 'AS', '1684', '🇦🇸'),
    ('Andorra', 'AD', '376', '🇦🇩'),
    ('Angola', 'AO', '244', '🇦🇴'),
    ('Anguilla', 'AI', '1264', '🇦🇮'),
    ('Antarctica', 'AQ', '672', '🇦🇶'),
    ('Antigua and Barbuda', 'AG', '1268', '🇦🇬'),
    ('Argentina', 'AR', '54', '🇦🇷'),
    ('Armenia', 'AM', '374', '🇦🇲'),
    ('Aruba', 'AW', '297', '🇦🇼'),
    ('Australia', 'AU', '61', '🇦🇺'),
    ('Austria', 'AT', '43', '🇦🇹'),
    ('Azerbaijan', 'AZ', '994', '🇦🇿'),
    ('Åland Islands', 'AX', '35818', '🇦🇽'),
    ('Bahamas', 'BS', '1242', '🇧🇸'),
    ('Bahrain', 'BH', '973', '🇧🇭'),
    ('Bangladesh', 'BD', '880', '🇧🇩'),
    ('Barbados', 'BB', '1246', '🇧🇧'),
    ('Belarus', 'BY', '375', '🇧🇾'),
    ('Belgium', 'BE', '32', '🇧🇪'),
    ('Belize', 'BZ', '501', '🇧🇿'),
    ('Benin', 'BJ', '229', '🇧🇯'),
    ('Bermuda', 'BM', '1441', '🇧🇲'),
    ('Bhutan', 'BT', '975', '🇧🇹'),
    ('Bolivia', 'BO', '591', '🇧🇴'),
    ('Bonaire, Sint Eustatius and Saba', 'BQ', '599', '🇧🇶'),
    ('Bosnia and Herzegovina', 'BA', '387', '🇧🇦'),
    ('Botswana', 'BW', '267', '🇧🇼'),
    ('Bouvet Island', 'BV', '47', '🇧🇻'),
    ('Brazil', 'BR', '55', '🇧🇷'),
    ('British Indian Ocean Territory', 'IO', '246', '🇮🇴'),
    ('Brunei', 'BN', '673', '🇧🇳'),
    ('Bulgaria', 'BG', '359', '🇧🇬'),
    ('Burkina Faso', 'BF', '226', '🇧🇫'),
    ('Burundi', 'BI', '257', '🇧🇮'),
    ('Cambodia', 'KH', '855', '🇰🇭'),
    ('Cameroon', 'CM', '237', '🇨🇲'),
    ('Canada', 'CA', '1', '🇨🇦'),
    ('Cape Verde', 'CV', '238', '🇨🇻'),
    ('Cayman Islands', 'KY', '1345', '🇰🇾'),
    ('Central African Republic', 'CF', '236', '🇨🇫'),
    ('Chad', 'TD', '235', '🇹🇩'),
    ('Chile', 'CL', '56', '🇨🇱'),
    ('China', 'CN', '86', '🇨🇳'),
    ('Christmas Island', 'CX', '61', '🇨🇽'),
    ('Cocos (Keeling) Islands', 'CC', '61', '🇨🇨'),
    ('Colombia', 'CO', '57', '🇨🇴'),
    ('Comoros', 'KM', '269', '🇰🇲'),
    ('Congo', 'CG', '242', '🇨🇬'),
    ('Cook Islands', 'CK', '682', '🇨🇰'),
    ('Costa Rica', 'CR', '506', '🇨🇷'),
    ('Croatia', 'HR', '385', '🇭🇷'),
    ('Cuba', 'CU', '53', '🇨🇺'),
    ('Curaçao', 'CW', '599', '🇨🇼'),
    ('Cyprus', 'CY', '357', '🇨🇾'),
    ('Czech Republic', 'CZ', '420', '🇨🇿'),
    ('Denmark', 'DK', '45', '🇩🇰'),
    ('DR Congo', 'CD', '243', '🇨🇩'),
    ('Djibouti', 'DJ', '253', '🇩🇯'),
    ('Dominica', 'DM', '1767', '🇩🇲'),
    ('Dominican Republic', 'DO', '1809', '🇩🇴'),
    ('Ecuador', 'EC', '593', '🇪🇨'),
    ('Egypt', 'EG', '20', '🇪🇬'),
    ('El Salvador', 'SV', '503', '🇸🇻'),
    ('Equatorial Guinea', 'GQ', '240', '🇬🇶'),
    ('Eritrea', 'ER', '291', '🇪🇷'),
    ('Estonia', 'EE', '372', '🇪🇪'),
    ('Eswatini', 'SZ', '268', '🇸🇿'),
    ('Ethiopia', 'ET', '251', '🇪🇹'),
    ('Falkland Islands', 'FK', '500', '🇫🇰'),
    ('Faroe Islands', 'FO', '298', '🇫🇴'),
    ('Fiji', 'FJ', '679', '🇫🇯'),
    ('Finland', 'FI', '358', '🇫🇮'),
    ('France', 'FR', '33', '🇫🇷'),
    ('French Guiana', 'GF', '594', '🇬🇫'),
    ('French Polynesia', 'PF', '689', '🇵🇫'),
    ('French Southern Territories', 'TF', '262', '🇹🇫'),
    ('Gabon', 'GA', '241', '🇬🇦'),
    ('Gambia', 'GM', '220', '🇬🇲'),
    ('Georgia', 'GE', '995', '🇬🇪'),
    ('Germany', 'DE', '49', '🇩🇪'),
    ('Ghana', 'GH', '233', '🇬🇭'),
    ('Gibraltar', 'GI', '350', '🇬🇮'),
    ('Greece', 'GR', '30', '🇬🇷'),
    ('Greenland', 'GL', '299', '🇬🇱'),
    ('Grenada', 'GD', '1473', '🇬🇩'),
    ('Guadeloupe', 'GP', '590', '🇬🇵'),
    ('Guam', 'GU', '1671', '🇬🇺'),
    ('Guatemala', 'GT', '502', '🇬🇹'),
    ('Guernsey', 'GG', '44', '🇬🇬'),
    ('Guinea', 'GN', '224', '🇬🇳'),
    ('Guinea-Bissau', 'GW', '245', '🇬🇼'),
    ('Guyana', 'GY', '592', '🇬🇾'),
    ('Haiti', 'HT', '509', '🇭🇹'),
    ('Heard Island and McDonald Islands', 'HM', '672', '🇭🇲'),
    ('Honduras', 'HN', '504', '🇭🇳'),
    ('Hong Kong', 'HK', '852', '🇭🇰'),
    ('Hungary', 'HU', '36', '🇭🇺'),
    ('Ivory Coast', 'CI', '225', '🇨🇮'),
    ('Iceland', 'IS', '354', '🇮🇸'),
    ('India', 'IN', '91', '🇮🇳'),
    ('Indonesia', 'ID', '62', '🇮🇩'),
    ('Iran', 'IR', '98', '🇮🇷'),
    ('Iraq', 'IQ', '964', '🇮🇶'),
    ('Ireland', 'IE', '353', '🇮🇪'),
    ('Isle of Man', 'IM', '44', '🇮🇲'),
    ('Israel', 'IL', '972', '🇮🇱'),
    ('Italy', 'IT', '39', '🇮🇹'),
    ('Jamaica', 'JM', '1876', '🇯🇲'),
    ('Japan', 'JP', '81', '🇯🇵'),
    ('Jersey', 'JE', '44', '🇯🇪'),
    ('Jordan', 'JO', '962', '🇯🇴'),
    ('Kazakhstan', 'KZ', '7', '🇰🇿'),
    ('Kosovo', 'XK', '383', '🇽🇰'),
    ('Kenya', 'KE', '254', '🇰🇪'),
    ('Kiribati', 'KI', '686', '🇰🇮'),
    ('Korea, North', 'KP', '850', '🇰🇵'),
    ('Korea, South', 'KR', '82', '🇰🇷'),
    ('Kuwait', 'KW', '965', '🇰🇼'),
    ('Kyrgyzstan', 'KG', '996', '🇰🇬'),
    ('Laos', 'LA', '856', '🇱🇦'),
    ('Latvia', 'LV', '371', '🇱🇻'),
    ('Lebanon', 'LB', '961', '🇱🇧'),
    ('Lesotho', 'LS', '266', '🇱🇸'),
    ('Liberia', 'LR', '231', '🇱🇷'),
    ('Libya', 'LY', '218', '🇱🇾'),
    ('Liechtenstein', 'LI', '423', '🇱🇮'),
    ('Lithuania', 'LT', '370', '🇱🇹'),
    ('Luxembourg', 'LU', '352', '🇱🇺'),
    ('Macao', 'MO', '853', '🇲🇴'),
    ('Madagascar', 'MG', '261', '🇲🇬'),
    ('Malawi', 'MW', '265', '🇲🇼'),
    ('Malaysia', 'MY', '60', '🇲🇾'),
    ('Maldives', 'MV', '960', '🇲🇻'),
    ('Mali', 'ML', '223', '🇲🇱'),
    ('Malta', 'MT', '356', '🇲🇹'),
    ('Marshall Islands', 'MH', '692', '🇲🇭'),
    ('Martinique', 'MQ', '596', '🇲🇶'),
    ('Mauritania', 'MR', '222', '🇲🇷'),
    ('Mauritius', 'MU', '230', '🇲🇺'),
    ('Mayotte', 'YT', '262', '🇾🇹'),
    ('Mexico', 'MX', '52', '🇲🇽'),
    ('Micronesia', 'FM', '691', '🇫🇲'),
    ('Moldova', 'MD', '373', '🇲🇩'),
    ('Monaco', 'MC', '377', '🇲🇨'),
    ('Mongolia', 'MN', '976', '🇲🇳'),
    ('Montenegro', 'ME', '382', '🇲🇪'),
    ('Montserrat', 'MS', '1664', '🇲🇸'),
    ('Morocco', 'MA', '212', '🇲🇦'),
    ('Mozambique', 'MZ', '258', '🇲🇿'),
    ('Myanmar', 'MM', '95', '🇲🇲'),
    ('Namibia', 'NA', '264', '🇳🇦'),
    ('Nauru', 'NR', '674', '🇳🇷'),
    ('Nepal', 'NP', '977', '🇳🇵'),
    ('Netherlands', 'NL', '31', '🇳🇱'),
    ('New Caledonia', 'NC', '687', '🇳🇨'),
    ('New Zealand', 'NZ', '64', '🇳🇿'),
    ('Nicaragua', 'NI', '505', '🇳🇮'),
    ('Niger', 'NE', '227', '🇳🇪'),
    ('Nigeria', 'NG', '234', '🇳🇬'),
    ('Niue', 'NU', '683', '🇳🇺'),
    ('Norfolk Island', 'NF', '672', '🇳🇫'),
    ('North Macedonia', 'MK', '389', '🇲🇰'),
    ('Northern Mariana Islands', 'MP', '1670', '🇲🇵'),
    ('Norway', 'NO', '47', '🇳🇴'),
    ('Oman', 'OM', '968', '🇴🇲'),
    ('Palestine', 'PS', '970', '🇵🇸'),
    ('Pakistan', 'PK', '92', '🇵🇰'),
    ('Palau', 'PW', '680', '🇵🇼'),
    ('Panama', 'PA', '507', '🇵🇦'),
    ('Papua New Guinea', 'PG', '675', '🇵🇬'),
    ('Paraguay', 'PY', '595', '🇵🇾'),
    ('Peru', 'PE', '51', '🇵🇪'),
    ('Philippines', 'PH', '63', '🇵🇭'),
    ('Pitcairn Islands', 'PN', '64', '🇵🇳'),
    ('Poland', 'PL', '48', '🇵🇱'),
    ('Portugal', 'PT', '351', '🇵🇹'),
    ('Puerto Rico', 'PR', '1787', '🇵🇷'),
    ('Qatar', 'QA', '974', '🇶🇦'),
    ('Réunion', 'RE', '262', '🇷🇪'),
    ('Romania', 'RO', '40', '🇷🇴'),
    ('Russia', 'RU', '7', '🇷🇺'),
    ('Rwanda', 'RW', '250', '🇷🇼'),
    ('Saint Barthélemy', 'BL', '590', '🇧🇱'),
    ('Saint Helena, Ascension and Tristan da Cunha', 'SH', '290', '🇸🇭'),
    ('Saint Kitts and Nevis', 'KN', '1869', '🇰🇳'),
    ('Saint Lucia', 'LC', '1758', '🇱🇨'),
    ('Saint Martin', 'MF', '590', '🇲🇫'),
    ('Saint Pierre and Miquelon', 'PM', '508', '🇵🇲'),
    ('Saint Vincent and the Grenadines', 'VC', '1784', '🇻🇨'),
    ('Samoa', 'WS', '685', '🇼🇸'),
    ('San Marino', 'SM', '378', '🇸🇲'),
    ('Sao Tome and Principe', 'ST', '239', '🇸🇹'),
    ('Saudi Arabia', 'SA', '966', '🇸🇦'),
    ('Senegal', 'SN', '221', '🇸🇳'),
    ('Serbia', 'RS', '381', '🇷🇸'),
    ('Seychelles', 'SC', '248', '🇸🇨'),
    ('Sierra Leone', 'SL', '232', '🇸🇱'),
    ('Singapore', 'SG', '65', '🇸🇬'),
    ('Sint Maarten', 'SX', '1721', '🇸🇽'),
    ('Slovakia', 'SK', '421', '🇸🇰'),
    ('Slovenia', 'SI', '386', '🇸🇮'),
    ('Solomon Islands', 'SB', '677', '🇸🇧'),
    ('Somalia', 'SO', '252', '🇸🇴'),
    ('South Africa', 'ZA', '27', '🇿🇦'),
    ('South Georgia and the South Sandwich Islands', 'GS', '500', '🇬🇸'),
    ('South Sudan', 'SS', '211', '🇸🇸'),
    ('Spain', 'ES', '34', '🇪🇸'),
    ('Sri Lanka', 'LK', '94', '🇱🇰'),
    ('Sudan', 'SD', '249', '🇸🇩'),
    ('Suriname', 'SR', '597', '🇸🇷'),
    ('Svalbard and Jan Mayen', 'SJ', '47', '🇸🇯'),
    ('Sweden', 'SE', '46', '🇸🇪'),
    ('Switzerland', 'CH', '41', '🇨🇭'),
    ('Syria', 'SY', '963', '🇸🇾'),
    ('Taiwan', 'TW', '886', '🇹🇼'),
    ('Tajikistan', 'TJ', '992', '🇹🇯'),
    ('Tanzania', 'TZ', '255', '🇹🇿'),
    ('Thailand', 'TH', '66', '🇹🇭'),
    ('Timor-Leste', 'TL', '670', '🇹🇱'),
    ('Togo', 'TG', '228', '🇹🇬'),
    ('Tokelau', 'TK', '690', '🇹🇰'),
    ('Tonga', 'TO', '676', '🇹🇴'),
    ('Trinidad and Tobago', 'TT', '1868', '🇹🇹'),
    ('Tunisia', 'TN', '216', '🇹🇳'),
    ('Turkey', 'TR', '90', '🇹🇷'),
    ('Turkmenistan', 'TM', '993', '🇹🇲'),
    ('Turks and Caicos Islands', 'TC', '1649', '🇹🇨'),
    ('Tuvalu', 'TV', '688', '🇹🇻'),
    ('Uganda', 'UG', '256', '🇺🇬'),
    ('Ukraine', 'UA', '380', '🇺🇦'),
    ('United Arab Emirates', 'AE', '971', '🇦🇪'),
    ('United Kingdom', 'GB', '44', '🇬🇧'),
    ('United States', 'US', '1', '🇺🇸'),
    ('United States Minor Outlying Islands', 'UM', '1', '🇺🇲'),
    ('Uruguay', 'UY', '598', '🇺🇾'),
    ('Uzbekistan', 'UZ', '998', '🇺🇿'),
    ('Vanuatu', 'VU', '678', '🇻🇺'),
    ('Vatican City', 'VA', '379', '🇻🇦'),
    ('Venezuela', 'VE', '58', '🇻🇪'),
    ('Vietnam', 'VN', '84', '🇻🇳'),
    ('Virgin Islands (British)', 'VG', '1284', '🇻🇬'),
    ('Virgin Islands (U.S.)', 'VI', '1340', '🇻🇮'),
    ('Wallis and Futuna', 'WF', '681', '🇼🇫'),
    ('Western Sahara', 'EH', '212', '🇪🇭'),
    ('Yemen', 'YE', '967', '🇾🇪'),
    ('Zambia', 'ZM', '260', '🇿🇲'),
    ('Zimbabwe', 'ZW', '263', '🇿🇼'),
]

# Build country map: prefix -> "flag country_name"
# Priority countries for shared prefixes (most commonly used)
PRIORITY_COUNTRIES = {
    '1': 'United States',      # USA/Canada both use 1
    '7': 'Russia',             # Russia/Kazakhstan both use 7
    '44': 'United Kingdom',    # UK and several territories use 44
    '61': 'Australia',         # Australia and territories
    '47': 'Norway',            # Norway and territories
    '262': 'Réunion',          # Multiple French territories
    '590': 'Guadeloupe',       # Multiple Caribbean territories
    '599': 'Curaçao',          # Multiple Caribbean territories
    '500': 'Falkland Islands', # Multiple territories
    '672': 'Antarctica',       # Multiple territories
    '64': 'New Zealand',       # New Zealand and territories
    '212': 'Morocco',          # Morocco and Western Sahara
}

COUNTRY_MAP = {}
for name, code, prefix, flag in COUNTRY_CODES:
    country_display = f"{flag} {name}"
    
    # If this prefix has a priority country, only add it if this is the priority
    if prefix in PRIORITY_COUNTRIES:
        if name == PRIORITY_COUNTRIES[prefix]:
            COUNTRY_MAP[prefix] = country_display
        # If prefix not yet in map and this isn't the priority, skip it
        elif prefix not in COUNTRY_MAP:
            pass  # Will be added by priority country later
    else:
        # For non-priority prefixes, keep first occurrence
        if prefix not in COUNTRY_MAP:
            COUNTRY_MAP[prefix] = country_display

def detect_country(phone_number):
    """
    Detect country from phone number using prefix matching.
    Optimized for full phone numbers (11-14 digits) from Excel, CSV, PDF files.
    
    Args:
        phone_number (str): Phone number to detect (can include +, spaces, dashes, etc.)
    
    Returns:
        str: Country name with flag emoji (e.g., "🇺🇸 United States") or "🌍 Unknown"
    """
    import re
    
    if not phone_number:
        return '🌍 Unknown'
    
    # Normalize phone number (remove all non-digit characters)
    normalized_number = re.sub(r'[^\d]', '', str(phone_number))
    
    if not normalized_number:
        return '🌍 Unknown'
    
    # Sort prefixes by length (longest first) for accurate matching
    sorted_prefixes = sorted(COUNTRY_MAP.keys(), key=len, reverse=True)
    
    for prefix in sorted_prefixes:
        if normalized_number.startswith(prefix):
            return COUNTRY_MAP[prefix]
    
    return '🌍 Unknown'

def get_country_name(country_with_flag):
    """
    Extract country name from the flag + name format.
    
    Args:
        country_with_flag (str): Country string like "🇺🇸 United States"
    
    Returns:
        str: Just the country name (e.g., "United States")
    """
    if ' ' in country_with_flag:
        return country_with_flag.split(' ', 1)[1]
    return country_with_flag
