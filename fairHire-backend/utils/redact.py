import re    # regular expressions
# Detects and masks PII in resumes

def redact_pii(text: str):
    pii_found = {}

    # Email
    emails = re.findall(r'\S+@\S+\.\S+', text)
    pii_found['emails'] = emails
    text = re.sub(r'\S+@\S+\.\S+', '[REDACTED_EMAIL]', text)

    # Phone number
    phones = re.findall(r'\+?\d[\d\s-]{7,}\d', text)
    pii_found['phones'] = phones
    text = re.sub(r'\+?\d[\d\s-]{7,}\d', '[REDACTED_PHONE]', text)

    # Names
    # Could match other capitalized words 
    # e.g. "My name is [REDACTED_NAME]"
    names = re.findall(r'[A-Z][a-z]+ [A-Z][a-z]+', text)
    pii_found['names'] = names
    for name in names:
        text = text.replace(name, '[REDACTED_NAME]')
    
    return text, pii_found