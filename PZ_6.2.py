#Дан список размера N. Найти номера тех элементов список, которые больше своего левого соседа, и количество таких элементов.
#Найденные номера выводить в порядке их убывания.
s = [3,5,4,3,6]
t = []
for i in range(len(s)-1):
  if s[i]<s[i+1]:
    print('shag=', i, '1=',s[i], '2=', s[i+1])
    t.append(i+1)
    print(t)
  else:
    print("Ничего")