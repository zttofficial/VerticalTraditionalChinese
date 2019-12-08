#-*- encoding:utf-8 -*-
import re

#only available when all characters are Chinese now
def transfer(text):
    pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|？|。|、|；|‘|’|【|】|·|！| |…|（|）'
    split = re.split(pattern,text)
    split.reverse()
    lens = len(split)
    lines = len(max(split, key=len))
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
    text = input("Text:")
    transfer(text)

