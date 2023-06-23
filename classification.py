import shutil
import os
import time
from numba import jit
path = r"C:\Users\iljoogns\Desktop\ng_image_list.txt" #불량 텍스트파일 경로
pathlist = [] #불량데이터 경로
originFullPath = [] #불량데이터가 있는 원본경로
originPath = r"D:\copiedData"
ngfolder = r"C:\Users\iljoogns\Desktop\NG"
okfolder = r"C:\Users\iljoogns\Desktop\OK"

# 텍스트파일 읽어서 리스트에 추가#
f = open(path, 'r')
while True:
    line = f.readline()
    if not line:
        break
    pathlist.append(line.replace("\n",''))
f.close()

#텍스트파일에 D:\\copiedData 경로 추가
for n in pathlist:
    originFullPath.append(originPath + n)
print(originFullPath)


##### 불량검출하는 부분 #####
for rootpath, subpath, filename in os.walk(originPath):
    for n in range(len(originFullPath)): #불량풀경로 하나씩 돔
        if rootpath == originFullPath[n]: #원본경로에 있는 경로랑 불량경로랑 일치하면
            for j in pathlist: #불량경로 하나씩 돔
                if j in rootpath:
                    shutil.copytree(rootpath, ngfolder+"{}".format(j))


okList = [] #불량폴더에 있는 폴더들의 경로가 들어있는 리스트
okFullList = []  #okList에서 D:\\copiedData 경로 추가된 리스트
##### 양품검출하는 부분 #####
for rootpath, subpath, filename in os.walk(ngfolder): #불량폴더 순회
    if "_" in rootpath: # rootpath에 문자열 "_"가 있으면 경로추가
        okList.append(str(rootpath).replace("C:\\Users\\iljoogns\\Desktop\\NG",""))
        okFullList.append(str(rootpath).replace("C:\\Users\\iljoogns\\Desktop\\NG",originPath))
print("양품경로",okList)
print("양품전체경로",okFullList)

for rootpath, subpath, filename in os.walk(originPath): #원본경로 전체 순회
    for n in range(len(okFullList)): #불량데이터가 있는 경로랑 원본경로랑 비교해서 일치하면 불량데이터 추가 안함
        if okFullList[n] == rootpath:
            break
    else:#일치 안하는것들중에 문자열 _ 가 포함된 경로들 전부 복사(양품)
        if rootpath.find("_") != -1:
            shutil.copytree(rootpath, okfolder + str(rootpath).replace(originPath,""))


































