
my_sq_list = [k**2 for k in range(10)]  # list comprehension

my_sq_list_2 = []
for el in range(10): # 0,1,2,3,4,5,6,7,8,9
    my_sq_list_2.append(el**2)

print(my_sq_list)
print(my_sq_list_2)