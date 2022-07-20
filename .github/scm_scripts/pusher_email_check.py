#!/usr/bin/python3

import sys

def check_pusher_email(email):
    #Check for non-ascii in The Title
    if not email.isascii():
        print("Commit title contains non-ascii characters")
        sys.exit(1)

    #Check Commit Title Format
    # NIOS-12345 : Some description
    # NIOS-12345: Some description
    ts = email.split(‘@‘)
    if len(ts) < 2:
        print(“pusher email format: <a-zA-Z0-9>@<infoblox.com>”)
        sys.exit(1)

    tile = ts[0].strip()
    if len(tile) < 3:
        print("Email ID INVALID: ", head)
        sys.exit(1)

    #Check JIRA and Version One
    cats = tile.split(‘.’)
    if len(cats) != 2:
        print(“Domain format: infoblox.com“)
        sys.exit(1)

    print(tile)
    sys.exit(0)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: email_check <pusher email>")
        sys.exit(1)

    title = sys.argv[1]
    check_title(title)

