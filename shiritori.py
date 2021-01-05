import random
import jaconv

shiritoriFlg = True
beforeWord = 'シリトリ'

def returnLastChar(word):
    r = word[-1]
    if (r=='ー'):
        print('ー！')
        return word[-2]
    r = upperChar(r)
    return r

def upperChar(s):
    smallChar = {'ャ':'ヤ','ュ':'ユ','ョ':'ヨ','ァ':'ア','ィ':'イ','ゥ':'ウ','ェ':'エ','ォ':'オ'}
    for k, v in smallChar.items():
        if(s == k):
            return v
    return s

def returnFirstChar(word):
    return word[0]

def returnWord(r):
    f=open("data/shiritoriData.csv", "r",  encoding ="utf-8")
    lines = f.readlines()
    for line in lines:
        line = line.split(',')
        if(line[0] != r):
            continue
        else:
            num = random.randint(1, len(line)-1)
            return line[num]

def shiritoriReturn(f,s):
    firstChar = returnLastChar(f)
    secondChar = returnFirstChar(s)
    nextChar = returnLastChar(s)
    print(firstChar,secondChar)
    if(nextChar == 'ン'):
        return str(1) + ',ゲームオーバー'
    if(firstChar==secondChar):
        return str(0) + ',' + returnWord(nextChar).rstrip()
    return str(1) + ',' + s

print('しりとりを始めるよ、"しりとり"！')

while(shiritoriFlg):
    text = input()
    text = jaconv.hira2kata(text)
    judge, beforeWord = shiritoriReturn(beforeWord, text).split(',')
    print(judge,beforeWord)
    if(int(judge) == 1):
        break