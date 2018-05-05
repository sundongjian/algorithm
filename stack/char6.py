# 迷宫的递归求解
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 四个方向


def mark(maze, pos):  # 给迷宫maze的位置表上pos表示到过了
    maze[pos[0][pos[1]]] = 2


def passable(maze, pos):
    return maze[pos[0][pos[1]]] == 0


def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end:
        print('pos:', pos, end=' ')
        return True
    for i in range(4):
        nexp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        if passable(maze, nexp):
            if find_path(maze, nexp, end):
                print(pos, end=' ')
                return True
    return False


# 迷宫的回溯求解
def print_path(end, pos, st):
    print(pos)
    for i in (0, st.depth() + 1):
        print(i, end=' ')


from stack.char1 import SStack


def maze_solve(maze, start, end):
    if start == end:
        print(start)
        return
    st = SStack()
    mark(maze, start)
    st.push((start, 0))
    while not st.is_empty():
        pos, nxt = st.pop()
        for i in range(0, 4):
            nexp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        if nexp == end:
            print_path(end, pos, st)
        elif passable(maze, nexp):
            st.push((pos, i + 1))
            mark(maze, pos)
            st.push((nexp, 0))
            break
    print('no path')


# 基于队列的迷宫求解
from stack.char5 import SQueue


def maze_solve_queue(maze, start, end):
    if start == end:
        print('path find')
        return
    qu = SQueue()
    mark(maze, start)
    qu.enqueue(start)
    while not qu.is_empty():
        pos = qu.dequeue()
        for i in range(0, 4):
            nexp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        if passable(maze, nextp):
            if nexp == end:
                print('find the path')
                return
            mark(maze, nexp)
            qu.enqueue(nexp)
    print('no path')
