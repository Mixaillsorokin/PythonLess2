# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

N=int(input('Введите N : '))
list=[]
for i in range(-N-1,N):
    i+=1
    list.append(i)
print(list)
f = open('file.txt','r')
res = 1
for l in f:
    l=int(l)
    if l > len(list):
        print(f' Нет {l} позиции в этом списке')
    else:
        res*=list[l]
    print(list[l] , end=',')
        
f.close()

print(f'Произведение элементов на указанных позициях -> {res}')
