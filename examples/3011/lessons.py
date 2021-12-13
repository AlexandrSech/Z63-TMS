config = "switchport trunk allowed vlan 1,3,10,20,30,100"
# ['1', '3', '10', '20', '30', '100']

result = config.split(" ")[-1].split(",")

print(result)

exit()

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
replace = "GigabitEthernet"

# 1 найти слово FastEthernet
# 2 delete them
# 3 past GigabitEthernet

nat = nat.replace("FastEthernet", "GigabitEthernet")
print(nat)

mac = "AAAA:BBBB:CCCC"

mac = mac.replace(":", ".")
print(mac)

exit()


l = nat.split("FastEthernet")
res = ""
for i, v in enumerate(l):
    if i < len(l) - 1:
        res += v + replace
    else:
        res += v



print(res)

exit()

print(nat.split())
print(nat.split(" "))
print(nat.split("ACL"))
print(nat.split("o"))

name = "alex"
template = "hello " + name + ", how are  you?"
print(template)


l = ["alex", "sasha", "alexander", "sanya"]

for name in l:
    print("hello {}, how are  you?".format(name))
    print("hello {n}, {n} how {} are {} you? {}".format(1, 2, 123, n=name))
    print(f"hello {name}, how are  you?")


