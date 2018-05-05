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
property={'(':1,'+':3,'-':3,'*':5,'/':5}
infix_operators='+-*/'


def trans_infix_suffix(line):
    st=SStack()
    exp=[]

    for x in token(line):
        if x not in infix_operators:
            exp.append(x)
        elif st.is_empty() or x=='(':
            st.push(x)
        elif x==')':
            while not st.is_empty() and st.top() !='(':
                st.append(st.pop())
            if st.is_empty():
                raise ValueError
            st.pop()
        else:
            while (not st.is_empty() and property[st.top()]>=property[x]):#当top是*/，x是+-的时候，将top加入
                exp.append(st.pop())
            st.push(x)

    while not st.is_empty():
        if st.top()=='(':
            raise ValueError
        exp.append(st.pop())

    return exp


def token(line):
    '''
    本函数知识简单的生成器，不能处理一元操作符
    '''
    i,llen=0,len(line)
    while i<llen:
        while line[i].isspace():
            i+=1
        if i >llen:
            break
        if line[i] in infix_operators:
            yield line[i]
            i+=1
            continue

        j=i+1

        while (j<llen and not line[j].isspace() and line[j] not in infix_operators):
            if (line[j]=='e' or line[j]=='E') and (j+1<llen and line[j+1]=='-'):
                j+=1
            j+=1

        yield line[i,j]
        i=j





