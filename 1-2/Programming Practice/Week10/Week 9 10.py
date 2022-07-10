
from bs4 import BeautifulSoup
from urllib2 import urlopen

"WEEK 10"
def Q1_(url):
    html_string = urlopen(url).read()
    soup = BeautifulSoup(html_string,'html.parser')

    for item in soup.find_all(class_='all-items-award-view-item'):
        print item.find_all(class_="award-whose-info")[0].text
        # print  item.find_all(class_='img-date-wrapper')[0].a
        print item.find_all(class_='img-date-wrapper')[0].a['href']
        print item.find_all(class_='module-desc')[0].text
        print item.find_all(class_='module-date')[0].text
        print "NEXT"

Q1_('https://www.sehir.edu.tr/en/awards-grants-and-achievements')




"""WEEK 9"""
file_obj = open("delicious.tiny.txt")
data = {} # {url:{blog: 5018 .... }}
tag_names = []
for line in file_obj:
    line = line[:-1].split("\t")
    url = line[0]
    left_line = line[3:]
    data.setdefault(url,{})
    for i in range(0,len(left_line),2):
        data[url][left_line[i]] = left_line[i+1]
        if left_line[i] not in tag_names:
            tag_names.append(left_line[i])
to_file = open("matrix.txt",'w')
to_file.write("URLS")
for tag in tag_names:
    to_file.write("\t"+tag)
for url in data:
    to_file.write("\n"+url)
    for tag in tag_names:
        if tag in data[url]:
            to_file.write("\t"+data[url][tag])
        else:
            to_file.write("\t"+"0")
to_file.close()

new_file = open("new_matrix.txt",'w')
new_file.write("tags")
for url in data:
    new_file.write("\t"+url)

for tag in tag_names:
    new_file.write("\n"+tag)
    for url in data:
        if  tag in data[url]:
            new_file.write("\t"+data[url][tag])
        else:
            new_file.write("\t"+"0")

new_file.close()












































































































































































