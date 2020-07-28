import re
import numpy as np
from collections import Counter

array = []
array_hash = Counter()
select = False

print("likeされた数が多いツイートを表示します")
while select==False:
  print("選んでください 1:メインアカウント 2:趣味アカウント")
  select_f = input()
  if select_f == "1":
    data = "data/mainAccount/tweet.js"
    select = True
  elif select_f == "2":
    data = "data/splatoonAccount/tweet.js"
    select = True

f=open(data, "r",  encoding ="utf-8")
lines = f.readlines()
path_w = 'data/test_w_favor.txt'
with open(path_w, mode="w") as f2:
  for line in lines:
    line = line.replace(' ','')
    if line.startswith('"full_text'):
      line = line.replace(',','').replace('"','').replace('full_text:','')
      line = line[:line.find('https://t.co')]
      array.append(line)
    elif  line.startswith('"favorite_count'):
      line = line.replace(',','').replace('"','').replace('\n','').replace('favorite_count:','')
      line = int(float(line))
      array.append(line)
  unti = int(len(array)/2)
  for i in range(unti):
    if array[i*2+1].startswith('RT@') or array[i*2+1].startswith('@'): continue
    array_hash[array[i*2+1]] = array[i*2]



c = 0

array_hash = sorted(array_hash.items(), key=lambda x:x[1],reverse=True)

print('------result------')
for key in array_hash:
  print(key)
  c+=1
  if c > 10: break