#encoding=utf8
import math
import random
import csv
import time
from copy import deepcopy

def loadCsv(filename):
	lines = csv.reader(open(filename, "rt"))
	dataset = list(lines)
	for i in range(len(dataset)):
		for j in range(len(dataset[i])-1):
			if(is_float(dataset[i][j])):
				dataset[i][j] = float(dataset[i][j])
			else:
				pass
	return dataset
def is_float(s):
	s=str(s)
	if s.isdigit():
		return True	
	if  s.count('.')==1:
		new_s=s.split('.')
		left_num=new_s[0]
		right_num=new_s[1]
		if right_num.isdigit():
			if left_num.isdigit():
				return True
			elif left_num.count('-')==1 and left_num.startswith('-'):
				tmp_num=left_num.split('-')[-1]
				if tmp_num.isdigit():
					return True
	return False

def splitDataset(dataset, splitRatio):
	row = len(dataset)
	testSize = row//10 + row % 10
	testSet = []
	copy = list(dataset)
	for i in range(testSize):
		index = testSize * splitRatio
		try:
			testSet.append(copy.pop(index))
		except:
			pass
	return [copy, testSet]
def splitDataset1(dataset, splitRatio):
	row = len(dataset)
	testSize = row//10
	testSet = []
	copy = list(dataset)
	for i in range(testSize):
		index = testSize * splitRatio
		try:
			testSet.append(copy.pop(index))
		except:
			pass
	return [copy, testSet]
def mean(numbers):#求均值

	return sum(numbers)/float(len(numbers))

def stdev(numbers):#求标准差

	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)

def summarize(dataset,types):
	for i in range(len(dataset)):
		del dataset[i][-1]
	summaries=[]
	tempdataset=trainingSetGlobal.copy()
	for attribute in zip(*dataset):
		if(is_float(attribute[1])):
			summaries.append((mean(attribute), stdev(attribute)))
		else:
			#计算概率
			separatedcolum = {}
			for i in range(len(attribute)):
				#print(len(attribute))
				vector = attribute[i]
				if (vector not in separatedcolum):
					separatedcolum[vector] = 1
				else:
					separatedcolum[vector] = separatedcolum[vector] + 1
			temp = {}
			for colattribute in separatedcolum:
				p = (separatedcolum[colattribute]+1)/(len(attribute)+len(separatedcolum))
				temp[colattribute] = p
				temp["denominator"] = len(attribute)+len(separatedcolum)
			summaries.append((temp, 0))
	return summaries
def class2Type(dataset,colum,type2,typei,types):      #指定某一类决策属性计算单个属性的概率
	n = len(type2)#n表示每一属性的类别数目
	count = n #这里同样记录的是某一属性的一类在指定决策类的类别数目，初始值为n,加上了拉普拉斯修正，初始值为该属性的类别数
	countType = 1#记录某一类出现的总次数，初始值为1因为使用了拉普拉斯修正
	for line in range(len(colum)):
		if dataset[line][-1] == types:#决策类
			count += 1
			if colum[line] == type2:
				countType += 1
	return (countType/count)

def testAll(dataset,colum,types):               #计算某一类决策属性下的贝叶斯概率
	#print("训练集数据数：{}",len(dataset))
	type2 = []#记录一列属性的类别
	for line in colum:
		if line not in type2:
			type2.append(line)
	n = len(type2)#n表示每一属性的类别数目
	p = 1
	for i in range(n):
		p = p * class2Type(dataset,colum,type2,type2[i],types)
	typeCount = 0
	for i in range(len(dataset)):
		if(dataset[i][-1]==types):
			typeCount+=1
	p = p * (typeCount/len(dataset))#  指定某一类决策属性计算单个属性的概率汇总相乘*某一类占总数据的比例
	return p


def separateByClass(dataset):
	separated = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		if (vector[-1] not in separated):
			separated[vector[-1]] = []
		separated[vector[-1]].append(vector)
	return separated

def summarizeByClass(dataset):
	separated = separateByClass(dataset)
	summaries = {}
	for classValue, instances in separated.items():#iteritems
		#print("{}:{}".format(classValue,len(instances)))
		summaries[classValue] = summarize(instances,classValue)
	return summaries
def summarizeByClassforTen(dataset):
	separated = separateByClass(dataset)
	summaries = []
	for i in range(len(dataset)):#iteritems
		pass
	return summaries

def calculateProbability(x, mean, stdev):
	exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
	return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent

def calculateClassProbabilities(summaries, inputVector):

	#print(len(summaries["won"]))
	#print(len(summaries["nowin"]))
	probabilities = {}
	for classValue, classSummaries in summaries.items():
		probabilities[classValue] = 1
		#print(len(classSummaries))#数据集36列
		for i in range(len(classSummaries)):#每一列操作
			mean, stdev = classSummaries[i]
			x = inputVector[i]
			if(stdev==0):
				#print(type(mean[x]))
				try:
					probabilities[classValue]*=mean[x]
				except:
					probabilities[classValue]*=1/mean["denominator"]
			else:
				probabilities[classValue] *= calculateProbability(x, mean, stdev)
	return probabilities



#针对测试集
def predict(summaries, inputVector):
	probabilities = calculateClassProbabilities(summaries, inputVector)
	bestLabel, bestProb = None, -1
	for classValue, probability in probabilities.items():
		#print(len(separatedglobal))
		probability = probability * ((separatedglobal[classValue]+1)/(separatedglobal["trainSetRows"]+len(separatedglobal)-1))
		if bestLabel is None or probability > bestProb:
			bestProb = probability
			bestLabel = classValue
	return bestLabel

def getPredictions(summaries, testSet):
	predictions = []
	for i in range(len(testSet)):
		result = predict(summaries, testSet[i])
		print('第{0}条测试数据 , 测试结果：{1} '.format(i,result ))
		predictions.append(result)
	return predictions

def getAccuracy(testSet, predictions):
	correct = 0
	for i in range(len(testSet)):
		if testSet[i][-1] == predictions[i]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0



filenametrain = 'train.csv'
filenametest = 'test.csv'
def main():
	time_start=time.time();#time.time()为1970.1.1到当前时间的毫秒数
	SUMaccuracy = 0
	trainingSet = loadCsv(filenametrain)	
	testSet = loadCsv(filenametest)
	global separatedglobal
	separatedglobal = {}
	for i in range(len(trainingSet)):
		vector = trainingSet[i][-1]
		if (vector not in separatedglobal):
			separatedglobal[vector] = 1
		else:
			separatedglobal[vector] = separatedglobal[vector] + 1
	separatedglobal["trainSetRows"] = len(trainingSet)
	global trainingSetGlobal 
	trainingSetGlobal = deepcopy(trainingSet)
	print('训练集行数={0} , 测试集行数={1} '.format(len(trainingSet), len(testSet)))		
	summaries = summarizeByClass(trainingSet)
	predictions = getPredictions(summaries, testSet)
	accuracy = getAccuracy(testSet, predictions)
	SUMaccuracy += accuracy 
	#print('准确率: {0}%'.format(accuracy))
	#print('平均准确率: {0:.6f}%'.format(SUMaccuracy))
	time_end=time.time();#time.time()为1970.1.1到当前时间的毫秒数  
	time_end = time_end-time_start 
	print('程序用时: {0:.4f}s'.format(time_end))
main()