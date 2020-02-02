import ssl
import pafy
import certifi

url = ''
print(certifi.where())
vPafy = pafy.new(url) 
print(vPafy.title)
print(vPafy.rating)
print(vPafy.viewcount)
print(vPafy.author)
print(vPafy.length)
print(vPafy.description)
