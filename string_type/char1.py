'''
ADT String:
    String(self,sseq)
    is_empty(self)
    len(self)
    char(self,index)
    substr(self,a,b)#取得子串
    match(self,string)#找到该串出现的第一个位置
    concat(self,string)#拼接
    subst(self,str1,str2)#替换
'''

#朴素字符串匹配方法
def navie_match(t,p):
    m,n=len(p),len(t)
    i,j=0,0
    while i<m and j<n:
        if p[i]==t[j]:
            i+=1
            j+=1
        else:
            i,j=0,j-i+1
    if i==m:
        return j-i
    return -1