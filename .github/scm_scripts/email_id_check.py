#!/usr/bin/python3
import re
import sys

def check_email(email):
    #Check for non-ascii in The email id
    if not email.isascii():
        print("Email title contains non-ascii characters")
        sys.exit(1)
        
    regex = "^[a-zA-Z0-9].@infoblox.com$"
    if (re.search(regex, GITHUB_EMAIL_URL)):
        print("Usage: email_check <EMAIL ID> <IS VALID>")

    ts = title.split('@')
    if len(ts) < 2:
        print("Commit email id format: <a-zA-z0-9>@<infoblox.com>")
        sys.exit(1)

    tail = ts[0].strip()
    if len(tail) < 3:
        print("Email ID INVALID: ", tail)
        sys.exit(1)

    #Check JIRA and Version One
    cats = tail.split('.')
    if len(cats) != 2:
        print("Email ID format: Infoblox.com")
        sys.exit(1)

    print(tail)
    sys.exit(0)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: email_check <email Title>")
        sys.exit(1)

    email = sys.argv[1]
    check_email(email)
