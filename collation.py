import csv
import os
import numpy as np
from sklearn.naive_bayes import GaussianNB
infoList1 = []
infoList2 = []
ershou = []
def readCSVList(filePath):
    try:
        file=open(filePath,'r',encoding="gbk")# 读取以utf-8
        context = file.read() # 读取成str
        list_result=context.split("\n")#  以回车符\n分割成单独的行
        #每一行的各个元素是以【,】分割的，因此可以
        length=len(list_result)
        for i in range(length):
            list_result[i]=list_result[i].split(",")
        return list_result
    except Exception :
        print("文件读取转换失败，请检查文件路径及文件编码是否正确")
    finally:
        file.close();# 操作完成一定要关闭


def csv1Info(dataset1):
    s1List = []
    for s1 in  dataset1:
        if s1[0] not in s1List:
            try:
                houseInfo = []
                s1List.append(s1[0])
                houseInfo.append(s1[0][:-1])
                if s1[6] == 'pudong':
                    houseInfo.append('浦东')
                elif s1[6] == 'minhang':
                    houseInfo.append('闵行')
                elif s1[6] == 'baoshan':
                    houseInfo.append('宝山')
                elif s1[6] == 'xuhui':
                    houseInfo.append('徐汇')
                elif s1[6] == 'putuo':
                    houseInfo.append('普陀')
                elif s1[6] == 'yangpu':
                    houseInfo.append('杨浦')
                elif s1[6] == 'huangpu':
                    houseInfo.append('黄埔')
                houseInfo.append(int(float(s1[2].split('平')[0])))
                houseInfo.append(int(float(s1[3].split('万')[0])))
                ershouInfo = houseInfo.copy()
                ershou.append(ershouInfo)
                houseInfo.append(int(float(s1[4].split('人')[0])))
                houseInfo.append(int(float(s1[5].split('次')[0][1:])))
                houseInfo.append(0)
                houseInfo.append(0)
                infoList1.append(houseInfo)
            except Exception as e:
                print('Got an error ', e)
        else:
            for i in infoList1:
                try:
                    if i[0] == (s1[0]):
                        i[2] = int((i[2] + float(s1[2].split('平')[0])) / 2)
                        i[3] = int((i[3] + float(s1[3].split('万')[0])) / 2)
                        i[4] = int((i[4] + float(s1[4].split('人')[0])) / 2)
                        i[5] = int((i[5] + float(s1[5].split('次')[0][1:])) / 2)

                except Exception as e:
                    print('Got an error ', e)
            for j in ershou:
                try:
                    if j[0] == (s1[0]):
                        j[2] = int((j[2] + float(s1[2].split('平')[0])) / 2)
                        j[3] = int((j[3] + float(s1[3].split('万')[0])) / 2)

                except Exception as e:
                    print('Got an error ', e)

    return infoList1,ershou

def csv2Info(dataset2):
    s2List = []
    for s2 in  dataset2:
        if s2[0] not in s2List:
            try:
                houseInfo = []
                s2List.append(s2[0])
                houseInfo.append(s2[0])
                houseInfo.append(int(float(s2[2].split('元')[0])))
                houseInfo.append(int(float(s2[3].split('人')[0])))
                infoList2.append(houseInfo)
            except Exception as e:
                print('Got an error ', e)
        else:
            for i in infoList2:
                try:
                    if i[0] == (s2[0]):
                        i[1] = int((i[1] + float(s2[2].split('元')[0])) / 2)
                        i[2] = int(i[2] + float(s2[3].split('人')[0]))

                except Exception as e:
                    print('Got an error ', e)
    return infoList2

def addInfo(info1,info2):
    for i1 in info1:
        for i2 in info2:
            if(i1[0] == i2[0]):
                i1[6] = i2[1]
                i1[7] = i2[2]
    return info1


def save(result,name):
    if (os.path.exists(name)):
        os.remove(name)
    with open(name, 'w',newline='') as f:
        wr = csv.writer(f)
        for item in result:
            wr.writerow(item)

def main():
    dataset1 = readCSVList('二手房.csv')[0:-1]
    dataset2 = readCSVList('租房.csv')[0:-1]
    rs1_1,rs1_2 = csv1Info(dataset1)
    for er in rs1_2:
        if er[3] < 100:
            er[3] = '60多万'
        elif 100 <= er[3] and er[3] < 200:
            er[3] = '100多万'
        elif 200 <= er[3] and er[3] < 300:
            er[3] = '200多万'
        elif 300 <= er[3] and er[3] < 400:
            er[3] = '300多万'
        elif 400 <= er[3] and er[3] < 500:
            er[3] = '400多万'
        elif 500 <= er[3] and er[3] < 600:
            er[3] = '500多万'
        elif 600 <= er[3] and er[3] < 700:
            er[3] = '600多万'
        elif 700 <= er[3] and er[3] < 900:
            er[3] = '800多万'
        elif 900 <= er[3] and er[3]< 1100:
            er[3] = '1000多万'
        elif 1100 <= er[3] and er[3]< 1300:
            er[3] = '1200多万'
        elif 1300 <= er[3]:
            er[3] = '1300万以上'
    #bayes(rs1)
    print(rs1_2)
    rs2 = csv2Info(dataset2)
    addInfo(rs1_1,rs2)
    fileName1 = '综合.csv'
    save(addInfo(rs1_1,rs2),fileName1)
    fileName2 = 'train.csv'
    save(rs1_2, fileName2)
if __name__ == '__main__':
    main()