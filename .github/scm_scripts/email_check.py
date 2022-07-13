import re

email = input("Enter Email Address: ")
x = re.search("^[a-zA-Z0-9].@infoblox.com$", email)
if x:
    print ("YES! We have a match!")
else:
    print ("No match")
