# -*- coding:UTF-8 -*-
from sys import argv
from os.path import exists
import xlrd
cript, add, pkg = argv

def do_out(element, lastIMSI,firstICCID,lastICCID):
	outfile1 = element[0] + '.xml'
	outfile2 = pkg + '.zip'
	outfile3 = element[0] + '_' + add + '_' + element[4] +'.txt'
	outline = '\t'.join([element[1],element[5],element[6],lastIMSI,firstICCID,lastICCID,element[3],element[4],outfile1,outfile2,outfile3,'\n'])
	return outline

def do_line(data):
	item = data
	count = item[5]
	firstIMSI= item[6]
	lastIMSI = str( int(firstIMSI) + int(count) -1)
	item[7] = item[7].split('\n')
	firstICCID = item[7][0]
	tempICCID = firstICCID.split('A')
	temp1 = str( int(tempICCID[1]) + int(count) -1)	
	lastICCID = tempICCID[0] + 'A' + temp1
#	print (firstIMSI,lastIMSI,firstICCID,lastICCID)
#	for i in range(len(item)):
#		print (i,':',item[i], "\tlen:",len(item[i]))
#		input (">")
	
	linecon = str(do_out (item,lastIMSI,firstICCID,lastICCID))
	return linecon
#	print (do_out(item,lastIMSI,firstICCID,lastICCID))

def read_xlsx():
	openfile = pkg +'.xlsx' 
	workbook = xlrd.open_workbook(openfile)
	booksheet = workbook.sheet_by_name('Sheet1')
	p =list()
	for row in range(1,booksheet.nrows):
		row_data = []
#		for col in range(booksheet.ncols):
		for col in range(8):
			cel = booksheet.cell(row, col)
			val = cel.value
			try:
				val = cel.value
				val = re.sub(r'\s+','',val)
			except:
				pass
			row_data.append(val)
		
		p.append(row_data)
	return p

def reduce_txt(data):
#	print(type(data))
#	print("len data is:",len(data))
#	input(">>")
	outfile = pkg+'.txt'
	outlines = []

	for each in data:
#		print(each)
		liner=do_line(each)
		outlines.append(liner)
        
	outfile = open(outfile,'w')
	outfile.writelines(outlines)
	outfile.close()
#		input("<<")

#	print (data)

if __name__=='__main__':
	data_list = list()
	data_list = read_xlsx()
#        print (data_list)
	reduce_txt(data_list)
	
	print("ok!")
	input("<")
