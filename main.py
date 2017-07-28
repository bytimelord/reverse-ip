#-*-coding: utf-8-*-

import urllib.request
import urllib.parse
import json

#Bu satırdaki proxy adresini değiştiriniz. Günlük reverse ip çekme sınırını delmek içindir.
proxy = urllib.request.ProxyHandler({'http':'149.202.94.120:3128'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)

domain = input("Domain Adresi : ")
degerler = {'remoteAddress':domain}
veri = urllib.parse.urlencode(degerler).encode('utf-8')
response = urllib.request.Request("http://domains.yougetsignal.com/domains.php", veri)
response.add_header('User-Agent','Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0')
f = urllib.request.urlopen(response)
content = f.read()
content = content.decode('utf-8')
dContent = json.loads(content)
for i in dContent['domainArray']:
	print(i)
