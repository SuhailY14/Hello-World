import re
from requests_html import HTMLSession

url = "https://github.com/settings/emails"
x = re.search("^[a-zA-Z0-9].@infoblox.com$", url)
session = HTMLSession()
r = session.get(url)
r.html.render()
