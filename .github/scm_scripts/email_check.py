import re
from requests_html import HTMLSession

url = "https://github.com/settings/emails"
x = re.search("^[a-zA-Z0-9].@infoblox.com$", url)
session = HTMLSession
r = session('https://github.com/settings/emails').get()
r.html.render()
for re_match in re.finditer(x, r.html.raw_html.decode()):
    print(re_match.group())
