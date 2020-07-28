import MeCab
import numpy as np
from collections import Counter
import re

tagger = MeCab.Tagger()

data = None
serch_word = None
array = []
array_extra = []

def extract_by_parse(sentence,word_p,word_n):
  nouns = []
  parsed=tagger.parse(sentence)
  for chunk in parsed.splitlines()[:-1]:
    (surface, feature) = chunk.split('\t')
    if (feature.split(',')[word_n]==word_p):
      nouns.append(surface)
  return nouns

def extract_by_check(sentence, serch_word):
  if re.search('('+serch_word+')', sentence): return True


def selectMode():
  select_mode = False
  while select_mode == False:
    print("1: ツイート品詞登場ランキングを表示します, 2: 特定の文字が含まれたツイートを検索します")
    select_m = input()
    if select_m == "1":
      print("ツイート品詞登場ランキングを表示します")
      select_mode = True
      return 1
    elif select_m == "2":
      print("特定の文字が含まれたツイートを検索します")
      select_mode = True
      return 2

def selectAccount():
  select_account = False
  while select_account == False:
    print("選んでください 1:メインアカウント 2:趣味アカウント 3:サブアカウント 4:いにしえのアカウント")
    select_f = input()
    if select_f == "1":
      data = "data/mainAccount/"
      select_account = True
    elif select_f == "2":
      data = "data/splatoonAccount/"
      select_account = True
    elif select_f == "3":
      data = "data/subAccount/"
      select_account = True
    elif select_f == "4":
      data = "data/oldAccount/"
      select_account = True
  return data

def selectType(data):
  select_type = False
  while select_type == False:
    print("ツイートorライク 1:Tweet 2:Like")
    select_t = input()
    if select_t == "1":
      data += "tweet.js"
      select_type = True
    elif select_t == "2":
      data += "like.js"
      select_type = True
  return data


def doExeFrequentWords(data):
  count_noun = Counter()
  c = 0
  select_part = False
  print("どの品詞を抽出しますか？")
  while select_part == False:
    print("選んでください 1:固有名詞 2:名詞 3:形容詞 4:動詞 5:助詞 6:助動詞 7:副詞")
    select_p = input()
    if select_p == "1":
      word_p = "固有名詞"
      word_n = 1
      select_part = True
    elif select_p == "2":
      word_p = "名詞"
      word_n = 0
      select_part = True
    elif select_p == "3":
      word_p = "形容詞"
      word_n = 0
      select_part = True
    elif select_p == "4":
      word_p = "動詞"
      word_n = 0
      select_part = True
    elif select_p == "5":
      word_p = "助詞"
      word_n = 0
      select_part = True
    elif select_p == "6":
      word_p = "助動詞"
      word_n = 0
      select_part = True
    elif select_p == "7":
      word_p = "副詞"
      word_n = 0
      select_part = True
  
  f=open(data, "r",  encoding = "utf-8")
  lines = f.readlines()
  for line in lines:
    line = line.replace(' ','')
    p = line.startswith('"full_text')
    q = line.startswith('"fullText')
    if p or q:
      line = line.replace('"full_text":"','').replace('"fullText":"','').replace('n','').replace('"','').replace(',','').replace('\\','')
      line = line[:line.find('https://t.co')]
      if line.startswith('RT@') or line.startswith('@'):
        continue
      noun = extract_by_parse(line,word_p,word_n)#名詞を取り出す
      for word in noun:
        count_noun[word] += 1

  count_noun = sorted(count_noun.items(), key=lambda x:x[1],reverse=True)
  print(data + '\n------'+ word_p +'result------')
  for key in count_noun:
    print(key)
    c+=1
    if c > 10: break


def doExeSerchWord(data):
  c = 0
  print('探す文字列を入力')
  serch_word = input()
  print(serch_word)

  f=open(data, "r",  encoding = "utf-8")
  lines = f.readlines()

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

  print(data + '\n----------------result----------------')
  for i in range(int(len(array_extra))):
    if i%2 == 1 and extract_by_check(array_extra[i], serch_word):
      print(array_extra[i-1] + "\n\t" + array_extra[i])
      c += 1
  
  print("\"" + serch_word + "\"を含むツイート件数：" + str(c) + " 件")




mode = selectMode()
data = selectAccount()

if mode == 1:
  data = selectType(data)
  doExeFrequentWords(data)
elif mode ==2:
  data += "tweet.js"
  doExeSerchWord(data)