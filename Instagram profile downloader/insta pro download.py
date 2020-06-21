import requests
from bs4 import BeautifulSoup

url = input()
r = requests.get(url)
s = BeautifulSoup(r.text,"html.parser")
u = s.find('meta',property="og:image")
url = u.attrs['content']
with open('image.jpg',"wb") as pic:
    binary = requests.get(url).content
    pic.write(binary)