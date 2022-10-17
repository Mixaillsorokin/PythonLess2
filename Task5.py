# 5. Реализуйте алгоритм перемешивания списка.
spisok1=[1,2,3,4,5,6]
print(f'Исходный список ->{ spisok1}')
spisok2=[]
for i in spisok1:
    i-=1
    spisok2.insert(i-len(spisok1),spisok1[i])

print(f'Перемешанный список -> {spisok2}')