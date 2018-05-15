'''
kmp算法，不回溯
 假设当pnext[i-1]时等于k-1，那么再为前缀和模式串本身都再算进各自的下一个字符pk和pi。若pk==pi，
 则自然是最大相同前后缀增加一个字符所以pnext[i]=k。若不相等，就意味着当前的前缀是无论如何也无法和后缀相同了。
 此时就应该退而求其次，试图在前缀中寻找一个更短的前缀看看能否靠这个短前缀加上一个字符来得到相同的后缀。
 这里需要注意的是，因为i-1长度下模式串的前后缀时相同的，当我取到那个短前缀（也就是前缀的前缀）时应该意识到其应该也是和后缀的后缀
 （也就是某个短一些的以pi-1结尾的子串）完全相同的。所以通过这个前缀+一个字符的模式来寻找后缀的后缀+pi的方法是正确的。
'''

def matching_KMP(t,p,pnext):
    j,i=0,0
    n,m=len(t),len(p)
    while j<n and i<m:
        if i==-1 or t[j]==p[i]:
            j,i=j+1,i+1
        else:
            i=pnext[i]
    if i==m:
        return j-i
    return -1

def gen_pnext(p):
    i,k,m=0,-1,len(p)#i表示p中元素位置
    pnext=[-1]*m
    while i<m-1:
        if k==-1 or p[i]==p[k]:
            i,k=i+1,k+1
            pnext[i]=k
            print('*',i,k)
        else:
            print('#',k,end=' ')
            k=pnext[k]#退到更短的相同前缀
            print(i,k)
    return pnext


a='abcabcabcaabc'
print(gen_pnext(a))