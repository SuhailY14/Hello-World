import re
import requests
from requests_html import HTMLSession

email = "https://github.com/settings/emails"
x = re.search("^[a-zA-Z0-9].@infoblox.com$", email)
email = response.html.find('email', first=True).text
print(email)
