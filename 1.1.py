import urllib2 
import re      
import urllib
import os

extensions = ['gif', 'png', 'bmp', 'jpg', 'jpeg', 'png']
list1 = ['q', 'w', 'e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','m','n']
list2 =  ['1','2','3','4','5','6','7','8','9','0']
main_dir = os.getcwd()


count = 1
new_dir = main_dir + '\\' + '1'
os.mkdir(new_dir)
os.chdir(new_dir)
url =  'http://lenta.ru/'
image_urls = re.findall('img .*?src="(.*?)"', urllib2.urlopen(url).read()) 
for i in range(len(image_urls)): 
    address = image_urls[i]
    if address[address.rfind('.') + 1 : ] in extensions:
        image_name = address[address.rfind('/') + 1 : ]
        for j in range(len(image_name)):
            if not (image_name[j] in list1) and not (image_name[j] in list2) and (image_name[j] != '.'):
                extra_str = image_name[: j] + str(count) + image_name[j + 1 :]
                image_name = extra_str
                extra_str = ''
                count += 1
        urllib.urlretrieve(address, image_name)

'''for i in range(len(image_urls)): 
    address = image_urls[i]
    if address[address.rfind('.') + 1 : ] in extensions:
        image_name = address[address.rfind('/') + 1 : ]
        try:
            urllib.urlretrieve(address, image_name)
        except:
            image_name = str(count) + image_name[image_name.rfind('.') : ]
            count += 1
            urllib.urlretrieve(address, image_name)
'''
print 'end'
