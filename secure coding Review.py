import re

# Sample Python application to audit
code = """
import sqlite3

username = input("Enter username: ")
password = input("Enter password: ")

db_password = "admin123"

conn = sqlite3.connect("users.db")
query = "SELECT * FROM users WHERE username = '" + username + "'"
cursor = conn.execute(query)

if password == db_password:
    print("Login successful")

result = eval(input("Enter expression: "))
"""

print("===== SECURITY CODING REVIEW =====")
print("Language: Python")
print("Application: Login Application")
print("-----------------------------------")

findings = []

# 1. Hard-coded password
if re.search(r'(password|passwd|pwd)\s*=\s*["\']', code, re.I):
    findings.append((
        "HIGH",
        "Hard-coded password detected",
        "Use environment variables or a secure secret manager."
    ))

# 2. SQL Injection
if re.search(r'["\'].*SELECT.*["\'].*\+.*username', code, re.I):
    findings.append((
        "CRITICAL",
        "Possible SQL Injection",
        "Use parameterized SQL queries."
    ))

# 3. eval()
if re.search(r'\beval\s*\(', code):
    findings.append((
        "CRITICAL",
        "Unsafe eval() function detected",
        "Avoid eval() with untrusted user input."
    ))

# 4. Plain-text password comparison
if re.search(r'password\s*==\s*\w+', code, re.I):
    findings.append((
        "MEDIUM",
        "Password is compared directly",
        "Use secure password hashing such as bcrypt or Argon2."
    ))

# Display findings
for number, finding in enumerate(findings, 1):
    severity, issue, recommendation = finding

    print(f"\nFinding {number}")
    print(f"Severity       : {severity}")
    print(f"Vulnerability  : {issue}")
    print(f"Recommendation : {recommendation}")

print("\n-----------------------------------")
print(f"Total vulnerabilities found: {len(findings)}")
print("Security review completed.")