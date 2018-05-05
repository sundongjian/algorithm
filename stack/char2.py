from stack.char1 import SStack

'''
括号匹配检查问题
'''


def check_parens(text):
    parents = '(){}[]'
    open_parents = '({['
    oppsite = {')':'(',"]":'[','}':'{'}

    def parentsheses(text):
        i,text_len=0,len(text)
        while True:
            while i<len(text) and text[i] not in parents:
                i+=1
            if i >=text_len:
                return
            yield text[i],i
            i+=1

    ss=SStack()

    for pr,i in parentsheses(text):
        if pr in open_parents:
            ss.push(pr)
        elif ss.pop() !=oppsite[pr]:
            print('匹配错误%s'% pr)
            return False
    print('匹配正确，括号正确')
    return True








