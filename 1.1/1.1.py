import urllib2
import re
import urllib


extensions = ['jpg', 'jpeg','png','gif','js', 'dib ','bmp', 'html',  'css', 'jsp', 'scn']
url = 'http://vk.com/irinafebruary?z=album145487720_223961386' #'http://tnt-online.ru/'
c = urllib2.urlopen(url)
#print type(c)
content = c.read()
image_urls = re.findall('img .*?src="(.*?)"', content)
for i in range(len(image_urls)):
    address = image_urls[i]
    if address[address.rfind('.') + 1 : ] in extensions:
        image_name = address[address.rfind('/') + 1 : ]
        urllib.urlretrieve(address, image_name)
print 'end'
