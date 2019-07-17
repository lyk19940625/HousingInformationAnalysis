import numpy as np
import matplotlib.pyplot as plt

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
        if address == 'pudong':
            pudong.append(data)
        elif address == 'minhang':
            minhang.append(data)
        elif address == 'baoshan':
            baoshan.append(data)
        elif address == 'xuhui':
            xuhui.append(data)
        elif address == 'putuo':
            putuo.append(data)
        elif address == 'yangpu':
            yangpu.append(data)
        elif address == 'huangpu':
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
    n = 12
    # 生成一个1-12的列表，不包括12，[ 0  1  2  3  4  5  6  7  8  9 10 11]
    x = np.arange(n)
    # np.random.uniform(0.5,1.0,n),生成n个0.5-1.0之间的随机数
    y1 = 3 * np.random.uniform(0.5, 1.0, n)
    y2 = 3 * np.random.uniform(0.5, 1.0, n)

    # 生成一个包含有n个值，均为0.2的list，表示允许的误差范围[-0.2,0.2]
    error = [0.2, ] * n

    # bar(left, height, width=0.8, bottom=None, hold=None, **kwargs)
    # 绘制柱形图
    # left:柱形图的x坐标
    # height柱形图的高度，以0.0为基准
    # width:柱形图的宽度，默认0.8
    # facecolor:颜色
    # edgecolor:边框颜色n
    # bottom:表示底部从y轴的哪个刻度开始画
    # yerr:应该是对应的数据的误差范围，加上这个参数，柱状图头部会有一个蓝色的范围标识,标出允许的误差范围,在水平柱状图中这个参数为xerr
    plt.bar(x, +y1, width=0.8, facecolor="#9999ff", edgecolor="white", yerr=error)
    plt.bar(x, -y2, facecolor="#ff9999", edgecolor="white")
    # 绘制文字，显示柱状图形的值
    for x, y1, y2 in zip(x, y1, y2):
        plt.text(x + 0.4, y1 + 0.05, '%.2f' % y1, ha='center', va='bottom')
        plt.text(x + 0.4, -(y2 + 0.05), '%.2f' % y2, ha='center', va='top')

    plt.ylim(-3.5, 3.5)
    plt.show()


def main():
    dataset = readCSVList('综合.csv')[:-1]
    district = 'pudong'
    drawXY = getXY(getData(dataset),district)
    draw(drawXY)


if __name__ == '__main__':
    main()