'''
排序顺序表的实现
'''
#s,t是两个按照大小排列的集合，求交集

def intersection(s,t):
    r = []
    i = 0
    j = 0
    while i <len(s) and j<len(t):
        if s[i]<t[j]:
            i+=1
        elif t[j] <s[i]:
            j+=1
        else:
            r.append(s[i])
            i+=1
            j+=1

#位向量实现，是一种特殊的集合实现技术。和贝叶斯里的邮件分类有点像。将所有元素放在一个集合，子集中，1表示有
'''
python中的dict和set的实现
负载因子a=散列表中当时的实际数据项数/散列表的基本存储区能容纳的元素个数
dict类型的对象采用散列技术实现，初创或者很小字典是，分配8个元素空间，当负载因子超过2/3时，自动更换更大存储
区，将已经保存的内容重新
散列到新的存储区，如果当前字典不是很大，用四倍十几元素分配新存储区，当超过50000时候，改为实际元素两倍分配
python规定dict的关键码，以及set和frozenset的元素都只能是不变的对象，是为了保证散列表的完整性。内部有hash
函数计算散列值
'''
