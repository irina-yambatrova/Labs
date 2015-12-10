
import urllib
import urllib2
import re
import os


main_Dir = os.getcwd()
numbPages = 15
maxLenUrlsList = numbPages * 10
extensions = {'gif', 'bmp', 'jpg', 'jpeg', 'png', 'js', 'css', 'html', 'ico'}
list1 = {'q', 'w', 'e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','m','n'}
list2 =  {'1','2','3','4','5','6','7','8','9','0'}


def Right_Address(url, main_Url):
    if url.find('http') < 0:
        correct_Url = main_Url + url
    else:
        correct_Url = url
    if (url.find('@') > 0) or (url.find('#') > 0) or (url =='/rss'):
        return False
    else:
        return correct_Url

def Right_Resources_List(url):
    content = urllib2.urlopen(url).read()
    img_urls = re.findall('img.*?src="(.*?)"', content)
    img_urls1 = re.findall('href="(.*?)"', content)
    js_urls = re.findall('script.*?src=\"(.*?.js)\"', content)
    js_urls1 = re.findall('link.*?href=\"(.*?.js)\"', content)
    css_urls = re.findall('link.*?href=\"(.*?.css)\"',content)
    urls = img_urls + js_urls + css_urls + js_urls1 + img_urls1
    return urls


def Save_Recources_Url(main_Url, url, count, main_Dir):
    k = 1
    extraContent = ''
    newDir = main_Dir + '\\' + str(count)
    os.mkdir(newDir)
    os.chdir(newDir)
    content = urllib2.urlopen(Right_Address(url, main_Url)).read()
    urlsList = Right_Resources_List(Right_Address(url, main_Url))
    for i in range(len(urlsList)):
        address = urlsList[i]
        if address[address.rfind('.') + 1 : ] in extensions:
            image_name = address[address.rfind('/') + 1 : ]
            for j in range(len(image_name)):
                if not (image_name[j] in list1) and not (image_name[j] in list2) and (image_name[j] != '.'):
                    extra_str = image_name[: j] + str(k) + image_name[j + 1 :]
                    image_name = extra_str
                    extra_str = ''
                    k += 1
            index = content.find(address)
            extraContent = content[ : index] + './' + image_name + content[index + len(address):]
            content = extraContent
            extraContent = ''
            if address.find('http') < 0:
                address = main_Url + address
            if address.find('http') > 0:
                address = address[address.find('http') : ]
            urllib.urlretrieve(address, image_name)
    fout = open(str(count) + '.html', 'w')
    fout.write(content)
    fout.close()


savedPages = []
count = 1
i = 0
correct_Url = ''
urlsList = []
main_Url = 'http://lenta.ru/'
word = 'Москва'
urlsList.append(main_Url)

while (i < len(urlsList)) and (len(savedPages) <= numbPages):
    url = urlsList[i]
    correct_Url = Right_Address(url, main_Url)
    if (correct_Url == False):
        urlsList.pop(i)
    else:
        content = urllib2.urlopen(correct_Url).read()
        if (content.find(word) > 0) and (correct_Url not in savedPages) and (len(savedPages) <= numbPages):
            Save_Recources_Url(main_Url, url, count, main_Dir)
            os.chdir(main_Dir)
            print count
            count += 1
            savedPages.append(correct_Url)
        urlsList += re.findall('a.*?href="(.*?)"',content)
        urlsList.pop(i)
print 'END'
