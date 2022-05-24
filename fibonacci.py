def fiboNacci(doos):
    count = 0
    doosje1 = -1
    doosje2 = 1
    uitkomst = 0
    
    while  count < doos:
        
        uitkomst = doosje1 + doosje2
        doosje1 = doosje2
        doosje2 = uitkomst

        count += 1

    return uitkomst


lst = []

for _ in range(1,22):
    lst.append(fiboNacci(_))
    
print(lst)

