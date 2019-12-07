#-*- encoding:utf-8 -*-
import re

def directTest(text):
    str = []
    for i in text:
        str.append(i)
        print(i)

def transfer(text):
    pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|？|。|、|；|‘|’|【|】|·|！| |…|（|）'
    split = re.split(pattern,text)
    split.reverse()
    lens = len(split)
    lines = len(max(split)) #len cannot get correct result for Chinese character 
    print(lines)
    space = []
    for a in split:
        d = lines - len(a)
        a += ("　" *d)
        space.append(a)
    str = "".join(space)
    s = ""
    for i in range(0, lines):
        for j in range(0, lens):
            s += str[i + j*lines] + ""
        s += "\n"
    print(s)

if __name__ == "__main__":        
    #text = input("Text:")
    text = "小陳同學，你好"
    transfer(text)

