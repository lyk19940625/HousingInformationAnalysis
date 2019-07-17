import matplotlib.pyplot as plt
import xlwt
import os
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

def getData(dataset):
    dataList = []
    pudong = []
    minhang = []
    baoshan = []
    xuhui = []
    putuo = []
    yangpu = []
    huangpu = []
    for data in dataset:
        #print(data[1])
        address = data[1]
        if address == '浦东':
            pudong.append(data)
        elif address == '闵行':
            minhang.append(data)
        elif address == '宝山':
            baoshan.append(data)
        elif address == '徐汇':
            xuhui.append(data)
        elif address == '普陀':
            putuo.append(data)
        elif address == '杨浦':
            yangpu.append(data)
        elif address == '黄埔':
            huangpu.append(data)
    dataList.append(pudong)
    dataList.append(minhang)
    dataList.append(baoshan)
    dataList.append(xuhui)
    dataList.append(putuo)
    dataList.append(yangpu)
    dataList.append(huangpu)
    return dataList

def getXY(datalist,district):
    x = []
    y1_1 = []
    y1_2 = []
    y2_1 = []
    y2_2 = []
    xy =[]
    if district == 'pudong':
        for i in datalist[0]:
            x.append(i[0])
            y1_1.append(i[3])
            y1_2.append(int((int(i[4])+int(i[5]))/6))
            y2_1.append(i[6])
            y2_2.append(i[7])
    elif district == 'minhang':
        for i in datalist[1]:
            x.append(i[0])
            y1_1.append(i[3])
            y1_2.append(int(i[4])+int(i[5]))
            y2_1.append(i[6])
            y2_2.append(i[7])
    elif district == 'baoshan':
        for i in datalist[2]:
            x.append(i[0])
            y1_1.append(i[3])
            y1_2.append(int(i[4])+int(i[5]))
            y2_1.append(i[6])
            y2_2.append(i[7])
    elif district == 'xuhui':
        for i in datalist[3]:
            x.append(i[0])
            y1_1.append(i[3])
            y1_2.append(int(i[4])+int(i[5]))
            y2_1.append(i[6])
            y2_2.append(i[7])
    elif district == 'putuo':
        for i in datalist[4]:
            x.append(i[0])
            y1_1.append(i[3])
            y1_2.append(int(i[4])+int(i[5]))
            y2_1.append(i[6])
            y2_2.append(i[7])
    elif district == 'yangpu':
        for i in datalist[5]:
            x.append(i[0])
            y1_1.append(i[3])
            y1_2.append(int(i[4])+int(i[5]))
            y2_1.append(i[6])
            y2_2.append(i[7])
    elif district == 'huangpu':
        for i in datalist[6]:
            x.append(i[0])
            y1_1.append(i[3])
            y1_2.append(int(i[4])+int(i[5]))
            y2_1.append(i[6])
            y2_2.append(i[7])
    xy.append(x)
    xy.append(y1_1)
    xy.append(y1_2)
    xy.append(y2_1)
    xy.append(y2_2)
    return xy

def draw(xy):
    name_list = xy[0]
    num_list = xy[2]
    num_list1 = xy[4]
    print(num_list)
    print(num_list1)
    x = list(range(len(num_list)))
    total_width, n = 0.8, 2
    width = total_width / n

    plt.bar(x, num_list, width=width, label='二手房热度', fc='y')
    for i in range(len(x)):
        x[i] = x[i] + width
    plt.bar(x, num_list1, width=width, label='出租房热度', tick_label=name_list, fc='r')
    plt.legend()
    plt.show()


def main():
    dataset = readCSVList('综合.csv')[:-1]
    res = getData(dataset)
    XY = getXY(res,'pudong')
    draw(XY)

if __name__ == '__main__':
    main()