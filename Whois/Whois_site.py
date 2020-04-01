import whois
site = input("Enter the site")
info = whois.query('google.com')
print(info)