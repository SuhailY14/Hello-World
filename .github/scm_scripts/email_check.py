import re
from requests_html import HTMLSession

email = "https://github.com/settings/emails"
x = re.search("^[a-zA-Z0-9].@infoblox.com$", email)
email = r.html.find('email', first=True).text
print(email)
