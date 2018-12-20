#coding=utf-8
import os
import shutil
import sys

OUTPUT_DIR = 'data/txt/'  #相对路径
OBJ_OUTPUT_DIR = 'data/obj/'  #相对路径,注意此时不需要创建这个文件夹，copytree不允许目标路径提前存在

shutil.copytree(OUTPUT_DIR, OBJ_OUTPUT_DIR)

f=os.listdir(OUTPUT_DIR)
f.sort()
print(f)

try:
	for filename in f:
	    portion = os.path.splitext(filename)#分离文件名字和后缀
	    newname = portion[0]+".obj"#要改的新后缀
	    # print(OBJ_OUTPUT_DIR + newname)
	    filename = OBJ_OUTPUT_DIR + filename
	    newname = OBJ_OUTPUT_DIR + newname
	    os.rename(filename,newname)
	    print(filename,'======>',newname)
except: 
	pass
	
    
 