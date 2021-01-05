import re
from expression import *

tweets = []

def selectAccount():
    select_account = False
    while select_account == False:
        print("選んでください 1:メインアカウント 2:趣味アカウント 3:サブアカウント 4:いにしえのアカウント")
        select_f = input()
        if select_f == "1":
            data = "data/mainAccount/tweet.js"
            select_account = True
        elif select_f == "2":
            data = "data/splatoonAccount/tweet.js"
            select_account = True
        elif select_f == "3":
            data = "data/subAccount/tweet.js"
            select_account = True
        elif select_f == "4":
            data = "data/oldAccount/tweet.js"
            select_account = True
    return data


def doExpressTweet(data):
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
            tweets.append(line)
    return tweets

account = selectAccount()
array = doExpressTweet(account)

print(array)
returnExpressionScore(array)
