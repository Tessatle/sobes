f=open('file.txt')
n=int(f.readline())
mas=[]
flag=0
m=[]
already=''
k=1
ch=0
for i in f.readline().split():
    mas.append(int(i))
for i in range(n):
    for j in range(k, i+1+mas[i]):
        if str(j+1) not in already:
            m.append([i+1, j+1])
            already+=str(j+1)+' '
            k=j+1
        if j+1==len(mas):
            flag=1
            break
    if flag==1:
        break
print(len(m))
for i in m:
    print(f'{i[0]} {i[1]}')
#Смог решить только так
