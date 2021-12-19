with open("/home/alexey/test.txt", "r") as file:
    st=[i for i in file]
    ts=list()
    [ts.append(f"{ind} - {s.strip()}")for ind, s in enumerate(st, 1)]
    print(ts)
    
