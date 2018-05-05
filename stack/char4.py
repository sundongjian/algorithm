'''
程序运行栈
|  0| - | 1 |
| 1 | 1 |  1|
| 2 | 1 | 2 |
| 3 | 2 | 6 |
| n| fa | res |
如图,res是返回给上一层的结果，fa是接收到上一层的结果，
用一个运行栈，对每次调用都在这个栈上为之开辟一个区域，称为一个函数帧
'''

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

'''
任何一个递归定义的函数，都可以通过引入一个栈保存中间结果的方式，翻译为一个非递归过程。
对应的，任何一个包含循环的程序都可以翻译为一个不包含循环的递归函数
'''
#简单递归转栈,当然只存了n没存res，属于不完整栈
from stack.char1 import SStack
def norec_fact(n):
    res=1
    st=SStack()
    while n>0:
        st.push(n)
        n-=1
    while not st.is_empty():
        res*=st.pop()
    return res

'''
背包问题，总重weight，共有W0-W(n-1)
不选n-1件，knap(weight,n-1)的解就是knap(weight,n)的解
如果选择，那么knap(weight-w(n-1)，n-1)有解，其解加上最后一件就是knap(weight,n)的解
'''
def knap_rec(weight,wlist,n):
    if weight==0:
        return True
    if weight <0 or (weight>0 and n<1):
        return False
    if knap_rec(weight-wlist[n-1],wlist,n-1):
        print('item'+str(n)+':',wlist[n-1])
        return True
    if knap_rec(weight,wlist,n-1):
        return True
    else:
        return False

#转为栈