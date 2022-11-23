s = "badc"
t = "baba"
x = zip(s,t)

x_tuple = tuple(x)
x_list = list(x)


Map_s=dict()
Map_t=dict()


for i,j in x_tuple:
    Map_s[i] = j
    Map_t[j] = i


print(Map_s)
print(Map_t)

compare_s =[]
compare_t =[]

for i in s:
    print(Map_s[i])
    compare_s.append(Map_s[i])

for i in t:
    print(Map_t[i])
    compare_t.append(Map_t[i])


print(compare_s)
print(compare_t)
# print(list(t))

print((compare_s==list(t)) and (compare_t==list(s)))