lst = list()
result_list = list()
count = 0
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
for i in range(len(lst)):
    count = lst[i]
    if (count < 30) and (count % 3 == 0):
        result_list.append(lst[i])
print(result_list)
 