k=0
f=open('0907.txt')
for i in f:
    temp=i[:4:]
    temp=temp.split(',')
    temp=float(temp[0])+float(temp[1])/10
    if temp<=37.0:
        if 'KNIFE' not in i and 'BOMB' not in i and 'WEAPON' not in i:
            if i.count('TICKET')>=1 and i.count('PASSPORT')==1 and i.count('MEDICALMASK')>=1:
                if (len(i)-4)<=1024:
                    k+=1
print(k)
#Ответ: 13
