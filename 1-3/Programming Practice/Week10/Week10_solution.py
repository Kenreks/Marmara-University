from selenium import webdriver
from bs4 import BeautifulSoup
import os

def make_soup(link):
    driver = webdriver.Chrome(os.getcwd()+'/chromedriver')   # can be different with OS. Refer to chromedriver file on your machine.
    driver.get(link)
    elem = driver.find_element_by_xpath("//*")
    html = elem.get_attribute("outerHTML")
    soup = BeautifulSoup(html,'html.parser')
    return soup

def get_awards(soup):
    data = {}
    whose = soup.find_all(class_="award-whose-info")
    titles=soup.find_all(class_="module-title")
    desc=soup.find_all(class_="module-desc")
    dates=soup.find_all(class_="module-date")
    links=soup.find_all(class_="module-title") 

    for item in range(len(whose)):
        name=whose[item].text
        title=titles[item].text
        description=desc[item].text
        date=dates[item].text
        link=links[item]['href']
        data.setdefault(name,{})
        data[name]['link']=link
        data[name]['description']=description
        data[name]['date']=date
        data[name]['title']=title
    return data

def print_awards(data):
    for key in data:
        print('Name :',key)
        print("Title :", data[key]['title'])
        print('Description :',data[key]['description'])
        print("Date :", data[key]["date"])
        print("Link :", data[key]["link"])
        print("*"*50)

soup = make_soup("https://www.sehir.edu.tr/en/awards-grants-and-achievements")
awards = get_awards(soup)
print_awards(awards)
