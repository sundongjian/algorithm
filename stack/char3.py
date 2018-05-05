'''
表达式和计算
(3-5) * (6 +17*4)/3
/*-3 5 + 6 *17 4 3
3 5 - 6 17 4 * + * 3 /
'''
from stack.char1 import SStack
#后缀表达式的计算

def suf_exp_evaluator(exp):
    operators='+-*/'
    st=SStack()

    for x in exp:
        if x not in operators:
            st.push(x)
            continue

        if st.depth()<2:
            raise ValueError
        a=int(st.pop())
        b=int(st.pop())

        if x=='+':
            c=b+a
        elif x=='-':
            c=b-a
        elif x=='*':
            c=b*a
        elif x=='/':
            c=b/a
        else:
            break

        st.push(c)

    if st.depth()==1:
        return st.pop()
    raise ValueError


#中缀表达式到后缀表达式转换
def trans_infix_suffix(line):
    st=SStack()
    exp=[]
