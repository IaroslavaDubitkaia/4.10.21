n = int(input('introduceti numarul de linii a matricei patrate '))
A = [[int(input()) for i in range(n)] for j in range(n)]
print = ('matricea introdusa')
for i in range(len(A)):
    print(A[i])
s1 = 0
for i in range(0,len(A)):
    s1+=A[i][i]
print(f'suma componentelor care se afla pe diagonala principala {s1}')
s2 = 0
for i in range(0,len(A)):
    s2+=A[len(A)-i-1][i]
print(f'suma componentelor care se afla pe diagonala secundara {s2}')
s3 = 0
for i in A:
    for j in i:
        if A.index(i)<i.index(j):
            s3+=j
print(f'suma componentelor care se afla mai sus de diagonala principala {s3}')
s4 = 0
for i in A:
    for j in i:
        if A.index(i)>i.index(j):
            s4+=j
print(f'suma componentelor care se afla mai jos de diagonala principala {s4}')
s5 = 0
for i in A:
    for j in i:
        if A.index(i)+i.index(j)<n-1:
            s5+=j
print(f'suma componentelor care se afla mai jos de diagonala secundara {s5}')
s6 = 0
for i in A:
    for j in i:
        if A.index(i)+i.index(j)>n-1:
            s6+=j
print(f'suma componentelor care se afla mai jos de diagonala secundara {s6}')