s = set()
# print(type(s))
# l = [1, 2, 3, 4]
# s_from_list = set(l)
# print(s_from_list)
# print(type(s_from_list))
s.add(1)
s.add(2)
s.add(2)
print(s)
s2={2,3}
s1=s.union(s2)
#s1 = {4, 6}
print(s1)
print(s.isdisjoint(s1))

