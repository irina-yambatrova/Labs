import urllib
import urllib2
import re
import os


main_dir = os.getcwd()
numb_pages = 15 
max_len_urls_list = numb_pages * 10 

extensions = {'gif', 'bmp', 'jpg', 'jpeg', 'png', 'js', 'css', 'html', 'ico'}
correct_letters = {'1','2','3','4','5','6','7','8','9','0','q', 'w', 'e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','m','n'}


def Right_Address(url, main_url):
    if url.find('http') < 0:
        correct_url = main_url + url
    else:
        correct_url = url
    if (url.find('@') > 0) or (url.find('#') > 0) or (url =='/rss'):
        return False
    else:
        return correct_url

def Right_Resources_List(url):
    content = urllib2.urlopen(url).read()
    img_urls = re.findall('img.*?src="(.*?)"', content)
    img_urls1 = re.findall('href="(.*?)"', content)
    js_urls = re.findall('script.*?src=\"(.*?.js)\"', content)
    js_urls1 = re.findall('link.*?href=\"(.*?.js)\"', content)
    css_urls = re.findall('link.*?href=\"(.*?.css)\"',content)
    urls = img_urls + js_urls + css_urls + js_urls1 + img_urls1
    return urls


def Save_Recources_Url(main_url, url, count, main_dir):
    extra_content = ''
    new_dir = main_dir + '\\' + str(count)
    os.mkdir(new_dir)
    os.chdir(new_dir)
    
    def Change_Name():
        if not (image_name[index_entry_letters] in correct_letters)  and (image_name[index_entry_letters] != '.'):
                    extra_str = image_name[: index_entry_letters] + str(random(correct_letters)) + image_name[index_entry_letters + 1 :]
                    image_name = extra_str
                    extra_str = ''
 
    content = urllib2.urlopen(Right_Address(url, main_url)).read()
    urls_list = Right_Resources_List(Right_Address(url, main_url))
    for i in range(len(urls_list)):
        address = urls_list[i]
        if address[address.rfind('.') + 1 : ] in extensions:
            image_name = address[address.rfind('/') + 1 : ]
            for j in range(len(image_name)):
                 Change_Name() 
            index = content.find(address)
            extra_content = content[ : index] + './' + image_name + content[index + len(address):]
            content = extra_content
            extra_content = ''
            if address.find('http') < 0:
                address = main_url + address
            if address.find('http') > 0:
                address = address[address.find('http') : ]
            urllib.urlretrieve(address, image_name)
    fout = open(str(count) + '.html', 'w')
    fout.write(content)
    fout.close()


saved_pages = [] 
count = 1
correct_url = ''
urls_list = [] 
main_url = 'http://lenta.ru/'
word = 'Москва'
urls_list.append(main_url)

while (0 < len(urls_list)) and (len(saved_pages) <= numb_pages):
    url = urls_list[0]
    correct_url = Right_Address(url, main_url)
    if (correct_url == False):
        urls_list.pop(0)
    else:
        content = urllib2.urlopen(correct_url).read()
        if (content.find(word) > 0) and (correct_url not in saved_pages) and (len(saved_pages) <= numb_pages):
            Save_Recources_Url(main_url, url, count, main_dir)
            os.chdir(main_dir)
            print count
            count += 1
            saved_pages.append(correct_url)
        urls_list += re.findall('a.*?href="(.*?)"',content)
        urls_list.pop(0)
print 'END'
