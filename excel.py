import xlrd
import  xlwt
def readExcel():
    dataList = []
    data = xlrd.open_workbook('58汇总.xls') # 打开xls文件
    for x in range(7):
        infoList = []
        table = data.sheets()[x] # 打开第一张表
        nrows = table.nrows # 获取表的行数
        for i in range(nrows): # 循环逐行打印
            if i == 0: # 跳过第一行
                continue
            if table.row_values(i)[1] != '':
                info = []
                str1 = table.row_values(i)[1].split('元')[0]
                str2 = str1.split('-')
                str3 = str2[0]+'到'+str2[1]
                info.append(table.row_values(i)[0])
                info.append(str3)
                info.append(table.row_values(i)[2])
                info.append(table.row_values(i)[3])
                infoList.append(info)
        dataList.append(infoList)
        print(dataList)
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
        table_head = ['职位','薪资','地点','公司']
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
                    sheet3.write(row+1,col,content[row][col])
                elif i == 2:
                    sheet7.write(row + 1, col, content[row][col])
                elif i == 3:
                    sheet2.write(row + 1, col, content[row][col])
                elif i == 4:
                    sheet1.write(row + 1, col, content[row][col])
                elif i == 5:
                    sheet5.write(row + 1, col, content[row][col])
                elif i == 6:
                    sheet4.write(row + 1, col, content[row][col])
                elif i == 7:
                    sheet6.write(row + 1, col, content[row][col])
        i = i+1
    workbook.save(r'58.xls')

write_excel(readExcel())