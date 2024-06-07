# 1、先去掉" [ ] { }
with open('F:/Desktop/test_data/test_data.csv', 'r') as file:
	content = file.read()
content = content.replace('}', '')
with open('F:/Desktop/test_data/test_data.csv', 'w') as file:
	file.write(content)

#2、提取txt中有多少个不同名的jpg
# jpg_list=[]
# file=open("F:/Desktop/test_data/test_data.csv")
# for line in file.readlines():
# 	lines=line.split(',')
# 	li=lines[-5:]
# 	print(li)
# 	if lines[1] not in jpg_list:
# 		jpg_list.append(lines[1])
# print(jpg_list)
# print(len(jpg_list))

#3、根据jpg创建相应的txt
# list1=['530_000001.jpg', '530_000002.jpg', '530_000003.jpg', '530_000004.jpg', '530_000005.jpg', '530_000006.jpg', '530_000007.jpg', '530_000008.jpg']
# for l in list1:
# 	files=open("F:/Desktop/test_data/result/"+l[:-3]+"txt",'w')
# 	files.close()

#4、将标签和坐标写进txt
# file=open("F:/Desktop/test_data/test_data.csv")
# for line in file.readlines():
# 	lines=line.split(',')
# 	li5=lines[-5:]
# 	# print(lines)
# 	# print(li5[-1][2])
# 	# print(li5[4][2])
# 	f=open("F:/Desktop/test_data/result/"+lines[1][:-3]+"txt","a")
# 	# ava的坐标为左上角x,y坐标+宽高
# 	center_x=(float(li5[0])+float(li5[2])/2)/1920.0
# 	center_y=(float(li5[1])+float(li5[3])/2)/1080.0
# 	width=float(li5[2])/1920.0
# 	height=float(li5[3])/1080.0
# 	# print(li5[4][2]+" "+str(center_x)+" "+ str(center_y)+" "+str(width)+" "+str(height))
# 	f.write(str(li5[4][2])+" "+str(center_x)+" "+ str(center_y)+" "+str(width)+" "+str(height)+"\n")
# 	f.close()


