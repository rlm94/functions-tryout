input1 = int(input("Van welk getal wilt u de tafel zien?\n: "))

def multiplier(input1):
    
    for x in range(1,11):
        output = input1 * x
        print(input1, " * " ,x , " = ", output)

        
            
multiplier(input1)