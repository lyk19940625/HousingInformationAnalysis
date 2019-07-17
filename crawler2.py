import crawler1
import requests
import csv
import random
from bs4 import BeautifulSoup
from time import ctime,sleep

houseList = crawler1.main()
start_url = "https://sh.lianjia.com/zufang/rs"

def parser_page(url,houseInfo):
    res_list2 = []
    house_address = houseInfo.split('  ')[0]
    house_style = houseInfo.split('  ')[1]
    try:
        res = requests.get(url)
    except Exception as e:
        print('异常处理')
        sleep(random.uniform(20))
        res = requests.get(url)
    #print(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    #print(soup.select('.house-lst'))
    for house in soup.select('.house-lst'):
        liLen = 0
        print(len(house.find_all('li')))
        if(int(len(house.find_all('li'))>1)):
            for li in house.find_all('li'):
                liLen = liLen+1
                if liLen >10:
                    break
                house_list = []
                house_price = li.find("div", {"class": "price"}).text
                house_follow = li.find("div", {"class": "col-2"}).text
                house_list.append(house_address)
                house_list.append(house_style)
                house_list.append(house_price)
                house_list.append(house_follow)
                res_list2.append(house_list)
                #print(house_list)
    return(res_list2)



def main():
    with open('租房.csv', 'w+',newline='') as f:
        wr = csv.writer(f)
        for i in houseList:
            url = start_url+i
            print(url)
            #parser_page(url,i)
            rs2 = parser_page(url, i)
            for item in rs2:
                wr.writerow(item)
            sleep(random.uniform(0.5, 2))
    f.close()
if __name__ == '__main__':
    main()