import re
import numpy as np
from collections import Counter
import MeCab

array = []
c = 0
tagger = MeCab.Tagger()
array_extra = []

def extract_by_check(sentence):
  if re.search('('+serch_word+')', sentence): return True


print('探す文字列を入力')
serch_word = input()
print(serch_word)

f1=open("data/mainAccount/tweet.js", "r",  encoding ="utf-8")
lines = f1.readlines()

for line in lines:
  line = line.replace(' ','')
  if line.startswith('"full_text'):
    line = line.replace(',','').replace('"','').replace('\\n','').replace('full_text:','')
    line = line[:line.find('https://t.co')]
    array.append(line)
  elif  line.startswith('"created_at'):
    line = line.replace(',','').replace('"','').replace('\n','').replace('created_at:','')
    array.append(line)

for i in range(int(len(array))):
  if array[i].startswith('RT@') or array[i].startswith('@'):
    array_extra.pop(-1)
    continue
  array_extra.append(array[i])

print('----------------result----------------')
for i in range(int(len(array_extra))):
  if i%2 == 1 and extract_by_check(array_extra[i]):
    print(array_extra[i-1] + "\n\t" + array_extra[i])
    c += 1

print("\"" + serch_word + "\"を含むツイート件数：" + str(c) + " 件")