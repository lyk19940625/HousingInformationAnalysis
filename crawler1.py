import requests
import os
from bs4 import BeautifulSoup
import csv
district_list = ['pudong','minhang','baoshan','xuhui','putuo','yangpu','huangpu']
start_url = "https://sh.lianjia.com/ershoufang/"
res_list = []
houseList = []
def parser_page(url,house_district):
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    for sellListContent in soup.select('.sellListContent'):
        for li in soup.find_all('li', {"class": "clear"}):
            house_list = []
            houseInfo = li.find("div", {"class": "houseInfo"}).text.split(' | ')
            house_address = houseInfo[0]
            house_style = houseInfo[1]
            house_size = houseInfo[2]
            house_price = li.find("div", {"class": "totalPrice"}).text
            followInfo = li.find("div", {"class": "followInfo"}).text.split(' / ')
            house_follow = followInfo[0]
            house_see = followInfo[1]
            house_list.append(house_address)
            house_list.append(house_style)
            house_list.append(house_size)
            house_list.append(house_price)
            house_list.append(house_follow)
            house_list.append(house_see)
            house_list.append(house_district)
            houseList.append(house_address+' '+house_style)
            res_list.append(house_list)
    return res_list



def save(result):
    if (os.path.exists('二手房.csv')):
        os.remove('二手房.csv')
    with open('二手房.csv', 'w',newline='') as f:
        wr = csv.writer(f)
        for item in result:
            wr.writerow(item)



def main():
    for i in district_list:
        url = start_url+i+'/co52/'
        parser_page(url,i)

    save(res_list)
    print(houseList)
    return  houseList

if __name__ == '__main__':
    main()