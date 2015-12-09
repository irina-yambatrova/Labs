import urllib2 #чтение кода страницы
import re      #регулярные выражения
import urllib #скачивание

extensions = ['gif', 'png', 'bmp', 'jpg', 'jpeg', 'png']
k = 1
url =  'http://lenta.ru/'
image_urls = re.findall('img .*?src="(.*?)"', urllib2.urlopen(url).read()) 
for i in range(len(image_urls)): #поиск файлов, которые нужно скачивать
    address = image_urls[i]
    if address[address.rfind('.') + 1 : ] in extensions:
        image_name = address[address.rfind('/') + 1 : ]
        if '%' in image_name:
            image_name = k
            k += 1
        urllib.urlretrieve(address, image_name) #cамо скачивание
print 'end'
