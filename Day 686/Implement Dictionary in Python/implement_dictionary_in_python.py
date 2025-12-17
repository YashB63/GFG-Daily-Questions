keys = input().split()
values = map(int, input().split())
my_dict = dict(zip(keys, values))
k, v = input().split()

my_dict[k] = int(v)
print("Inserted")

d = input()

if(d in my_dict):
    del my_dict[d]
    print("Deleted")
else:
    print(-1)

p = input()

if(my_dict.get(p)):
    print(f"Marks of {p} is {my_dict[p]}")
else:
    print(-1)