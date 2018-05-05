# 排序,<

def list_sort(lst):
    for i in range(1, len(lst)):  # 开始片段[0,1]已经排好了
        x = lst[i]
        j = i
        while j > 0 and x < lst[j - 1]:  # 将前面[0,i]从后往前和x比较，如果x小，那么lst[j-1]后移一位
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = x
