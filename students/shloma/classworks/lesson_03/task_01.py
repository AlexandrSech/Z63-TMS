def decimal_to_binary(n):
    return bin(n).replace("0b", "")


ip = "192.168.3.12"
ips = list(map(int, ip.split(".")))

[print(str(i).ljust(10), end="") for i in ips]
print()
[print(str(decimal_to_binary(j)).ljust(10), end="") for j in ips]