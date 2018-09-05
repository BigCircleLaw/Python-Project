import os
import re
# import csv

# os.path.join('C:', 'Users', '79455', 'pythonshishi', 'masterTX.txt')
while True:
    print('请输入文件的绝对路径：')
    filePath = input()
    if not os.path.isfile(filePath):
        print('请输入正确的绝对路径，', end='')
        continue
    break

soucreFile = open(filePath, 'r')
txtLines = soucreFile.readlines()
soucreFile.close()
fileDir = os.path.dirname(filePath)
fileName = os.path.basename(filePath)
# print(fileDir)
# print(fileName)
fileSplit = fileName.split('.')
# print(fileSplit)
dataRegex = re.compile(r'(\d\.\d{6}).*(0x[\d A-F][\d A-F])')
targetfile = open(
    fileDir + '\\' + fileSplit[0] + '_revision' + '.' + fileSplit[1], 'w+')
for txtline in txtLines:
    mo = dataRegex.search(txtline)
    if mo is not None:
        if mo.group(2) == '0xFF':
            if targetfile.tell() > 0:
                targetfile.seek(targetfile.tell() - 1)
                temp = targetfile.read()
                if temp[-1] != '\n':
                    targetfile.write('\n')
            targetfile.write(mo.group(1) + '  ')
        if mo.group(2) == '0xFE':
            targetfile.write(mo.group(2) + '\n')
        else:
            targetfile.write(mo.group(2) + ', ')
targetfile.close()
