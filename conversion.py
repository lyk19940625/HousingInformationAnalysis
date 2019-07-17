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
def write_excel(datalist):
    i = 1
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet1 = workbook.add_sheet('浦东', cell_overwrite_ok=True)
    sheet2 = workbook.add_sheet('闵行', cell_overwrite_ok=True)
    sheet3 = workbook.add_sheet('宝山', cell_overwrite_ok=True)
    sheet4 = workbook.add_sheet('徐汇', cell_overwrite_ok=True)
    sheet5 = workbook.add_sheet('普陀', cell_overwrite_ok=True)
    sheet6 = workbook.add_sheet('杨浦', cell_overwrite_ok=True)
    sheet7 = workbook.add_sheet('黄埔', cell_overwrite_ok=True)
    for x in datalist:
        table_head = ['小区','区域','面积（平方米）','价格（万元）','关注人数','带看人数','月租','租房热度']
        content = x
        # 初始化workbook 并且添加excel Sheet
        #写excel表头
        headlen = len(table_head)
        for j in range(headlen):
            if i == 1:
                sheet1.write(0,j,table_head[j])
            elif i == 2:
                sheet2.write(0, j, table_head[j])
            elif i == 3:
                sheet3.write(0, j, table_head[j])
            elif i == 4:
                sheet4.write(0, j, table_head[j])
            elif i == 5:
                sheet5.write(0, j, table_head[j])
            elif i == 6:
                sheet6.write(0, j, table_head[j])
            elif i == 7:
                sheet7.write(0, j, table_head[j])
        contentRow = len(content) #列表元素个数  = 待写入内容行数
        #从content获取要写入的第一列的内容,存入列表
        for row in range(contentRow):
            for col in range(len(content[row])):
                if i == 1:
                    sheet1.write(row+1,col,content[row][col])
                elif i == 2:
                    sheet2.write(row + 1, col, content[row][col])
                elif i == 3:
                    sheet3.write(row + 1, col, content[row][col])
                elif i == 4:
                    sheet4.write(row + 1, col, content[row][col])
                elif i == 5:
                    sheet5.write(row + 1, col, content[row][col])
                elif i == 6:
                    sheet6.write(row + 1, col, content[row][col])
                elif i == 7:
                    sheet7.write(row + 1, col, content[row][col])
        i = i+1
    workbook.save(r'house.xls')




def main():
    dataset = readCSVList('综合.csv')[:-1]
    res = getData(dataset)
    if (os.path.exists('house.csv')):
        os.remove('house.csv')
    write_excel(res)


if __name__ == '__main__':
    main()