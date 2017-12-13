a = [[1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0]]

"""a = [[0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1]]"""
    
n = len(a); m = len(a[0])

ans = [0]*n
ans_l = [0]*n; ans_r = [0]*n; ans_h = [0]*n
d = [[0]*m for i in range(n)] # допматрица, хранящая для каждого элемента кол-во единиц над ним, включая его самого

for i in range(n):
    for j in range(m):  
        if i == 0:
            d[i][j] = a[i][j]
        else:
            if a[i][j] == 1:
                d[i][j] = d[i-1][j]+1
                
    # максимальная площадь прямоугольника под гистограммой
    A = d[i]
    A = [-1] + A
    A.append(-1)
    k = len(A)
    stack = [0] # увеличивающийся стек

    for t in range(k):
		# последний элемент в стеке хранит первый элемент слева, которого значение допматрица меньше текущего
        while A[t] < A[stack[-1]]:
            h = A[stack.pop()]
            area = h*(t-stack[-1]-1)
            ans[i] = max(ans[i], area)
            if area == ans[i]:
                ans_l[i] = stack[-1]
                ans_r[i] = t-2
                ans_h[i] = h
        stack.append(t)

i = ans.index(max(ans)) # ищем максимум решения задачи о макс. площади прямоугольника (см. выше) для каждой строки

# координаты в 0-base системе
lt = [i-ans_h[i]+1, ans_l[i]] #левый верхний угол
print(lt)
ld = [i, ans_l[i]]            #левый нижний угол
print(ld)
rt = [i-ans_h[i]+1, ans_r[i]] #правый верхний угол
print(rt)
rd = [i, ans_r[i]]            #правый нижний угол
print(rd)