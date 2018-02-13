def read():
    n, p = [int(num) for num in input().split()]
    
    course = []
    for i in range(n):
        course_id, semester = [int(num) for num in input().split()]
        course.append([course_id, semester])
    
    parent = [[] for i in range(n)]
    child = [[] for i in range(n)]
    for i in range(p):
        course_to_take, finished_course = [int(num) for num in input().split()]
        parent[course_to_take].append(finished_course)
        child[finished_course].append(course_to_take)
    return n, p, course, parent, child

def DFS(idx, child, ans, mark, cycle):
    mark[idx] = 1
    for i in child[idx]:
        if mark[i] == 1:
            ans[0] = True
        elif mark[i] == 0:
            DFS(i, child, ans, mark, cycle)
    mark[idx] = -1
    cycle.append(idx)

def check_cycle(n, child, parent):
    mark = [0] * n
    cycle = []
    ans = [False]
    for idx in range(len(mark)):
        if mark[idx] == 0 and len(parent[idx]) == 0:
            DFS(idx, child, ans, mark, cycle)
    if ans[0] == True or not len(cycle):
        return True
    else:
        return False

def schedule(n, course, child, parent):
    take_list = []
    ans = []
    meet_prereq = []
    for idx in range(len(parent)):
        if not len(parent[idx]):
            meet_prereq.append(idx)

    semester_needed = 0
    while len(take_list) < n:
        tmp = []
        copied_meet_prereq = meet_prereq[:]
        for i in copied_meet_prereq:
            if course[i][1] == semester_needed % 2 or course[i][1] == 2:
                meet_prereq.remove(i)
                take_list.append(i)
                tmp.append(i)
                for j in child[i]:
                    parent[j].remove(i)
                    if len(parent[j]) == 0:
                        meet_prereq.append(j)
        ans.append(tmp)
        semester_needed += 1

    print(float(semester_needed)/2)
    for i in range(len(ans)):
        if not len(ans[i]):
            print(-1)
        else:
            print(' '.join(str(cls) for cls in ans[i]))
    
if __name__ == '__main__':
    n, p, course, parent, child = read()
    if check_cycle(n, child, parent):
        print(-1)
    else:
        schedule(n, course, child, parent)