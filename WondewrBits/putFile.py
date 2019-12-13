
import os
# import commands

fileList = os.listdir()
# print(fileList)

for name in fileList:
  type_str = name.split('.')
  # print(type_str)
  if len(type_str) > 1:
    if (not (type_str[0] == 'main')) and (type_str[1] == 'py'):
      print(name)
      os.system('ampy --port COM11 put ' + name)
      # print(t)
