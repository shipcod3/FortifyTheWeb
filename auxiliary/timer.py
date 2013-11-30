from time import localtime, strftime

def timer():
	endtime=strftime("%a, %d %b %Y %X +0000", localtime())
	print endtime