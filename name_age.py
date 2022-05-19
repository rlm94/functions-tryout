def welcome():

    question = True
    while question == True:
        name = input("Hoe heet u\n: ")
        age = input("Hoe oud bent u\n: ")
        if name == "stop" or age == "stop":     
            question = False
        else:
            print(f"Hallo {name}, je leeftijd is {age} jaar")

welcome()