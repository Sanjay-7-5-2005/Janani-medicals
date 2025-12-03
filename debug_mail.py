import os
import smtplib
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

server = os.getenv('MAIL_SERVER')
port = int(os.getenv('MAIL_PORT', 587))
username = os.getenv('MAIL_USERNAME')
password = os.getenv('MAIL_PASSWORD')

print(f"DEBUG: Attempting to connect to {server}:{port}")
print(f"DEBUG: Username: {username}")
# Mask password for security in logs, but show length to verify it's not empty
masked_password = '*' * len(password) if password else "None"
print(f"DEBUG: Password Length: {len(password) if password else 0}")
print(f"DEBUG: Password (First 2 chars): {password[:2] if password else 'N/A'}")

try:
    smtp = smtplib.SMTP(server, port)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    print("DEBUG: TLS connection established. Attempting login...")
    smtp.login(username, password)
    print("SUCCESS: Login successful!")
    smtp.quit()
except Exception as e:
    print(f"ERROR: Login failed. Reason: {e}")
