list_of_sq = [k**2 for k in range(21)]
gen_of_sq = (k**2 for k in range(21))


print(list_of_sq)
print(gen_of_sq)

for k in gen_of_sq:
    print(k)
