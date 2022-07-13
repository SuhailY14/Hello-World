import re
from requests_html import HTMLSession

email = "https://github.com/settings/emails"
x = re.search("^[a-zA-Z0-9].@infoblox.com$", email)
try:
  session = HTMLSession()
  r = session.get(email)
  email = r.html.find('email')
if x:
    print ("YES! We have a match!")
else:
    print ("No match")
