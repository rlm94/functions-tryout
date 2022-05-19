def multiplier(doosje):
    
    for x in range(1,11):
        output = doosje * x
        print(doosje, " * " ,x , " = ", output)

getal1 = int(input("Van welk getal wilt u de tafel zien?\n: "))
        
            
multiplier(getal1)