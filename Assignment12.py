import re

def extract_emails(text, exclude_domain):
    # Define a regex pattern that excludes the specified domain
    pattern = rf"\b[A-Za-z0-9._%+-]+@(?:?!{re.escape(exclude_domain)})[A-Za-z0-9.-]+\.[A-Z|a-z]{{2,}}\b"
    
    # Find all email addresses using the modified pattern
    emails = re.findall(pattern, text)
    return emails

# Sample text containing email addresses
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

# Extract emails excluding those from 'exclude.com'
exclude_domain = "exclude.com"
emails = extract_emails(text, exclude_domain)
print(emails)
