#Made by 990623432
def whichDiet():
    method1 = int(input("Welke methode kies jij (1) koolhydraten vrij (2) spartaans of (3) eet de helft?\n: "))
    if method1 == 1:
        carbFree()
    elif method1 == 2:
        spartan()
    elif method1 == 3:
        eatHalf()

def carbFree():

    print("je heb de koolhydraten vrije methode gekozen")
    eat1 = int(input("je hebt 3 dagen getraint je hebt wel een pizza verdient hoor Ja(1) of Nee(2)\n: "))
    if eat1 == 1:
        print("Jij gaat het niet halen jongen")
    elif eat1 == 2:
        print("Goed zo geen junk food")
        answer = int(input("probeer je de nieuwe energybar die wordt uitgedeeld bij de sportschool voor Ja(1) of Nee(2)\n: "))
        if answer == 1:
            print("Hoe kan je ook vallen voor zo een duidelijke val")
        elif answer == 2:
            print("Goed zo hou deze instelling aan")
        else:
            print("kom op maak een keuze met (1)Ja of (2)Nee")
    else:
        print("kom op maak een keuze met (1)Ja of (2)Nee")


def spartan():

    print("je hebt de spartaanse methode gekozen")
    eat2 = int(input("je hebt zojuist 5 dagen achter elkaar getraint je verdient wel een cheatday hoor (1)Ja of (2)Nee?"))
    if eat2 == 1:
        print("je heb een heftige maaltijd achter de rug met teveel calorieën dat moet je aanpakken ")
        answer = int(input("ga je nu twee uur fietsen(1) of de marathon(2) lopen"))
        if answer == 1:
            answer = int(input("je heb een lekke band waardoor je kan kiezen voor zelfreparatie(1) of fietsenmaker(2)"))
            if answer == 1:
                print("je binnenband heeft 5 gaatjes en je hebt maar twee plakkertjes bij je dus kan je niet aan genoeg beweging komen")
            elif answer == 2:
                print("de fietsenmaker duurde te lang waardoor je je motivatie bent kwijtgeraakt")
            else:
                print("hou maar op je instelling is niet goed ingesteld")
        elif answer == 2:
            print("je heb de marathon behaald en daarmee 65% van je doel behaald ga zo door")
            answer = int(input("we swappen de dieet in de laatste periode kies voor sapdieet(1) of soepdiet(2)"))
            if answer == 1:
                print("helaas heb je maar 95% van je doel behaald dus je bent maar 28.5 kilo af ")
            elif answer == 2:
                print("helaas door de soepdieet ben je meer brood gaan eten om te vullen en dus heb je niet je doel behaald")
            else:
                print("ik neem aan dat dit toch niks voor jou is kap er maar mee")
        else:
            print("kom op maak nou een keuze en verspeel mijn tijd niet")
    elif eat2 == 2:
        print("goed zo hou deze instelling en probeer de mobicep fatburner aan")
        answer = int(input("Gaat u beginnen met de fatburner kies voor Ja(1) of nee(2)"))
        if answer == 1:
            print("goed zo")
        elif answer == 2:
            print("dan maar niet")
        answer == int(input("ben je bereid om veganist te worden Ja(1) of nee(2)"))
        if answer == 1:
            print("goeie zet van je nu zal je zeker je doel behalen")
            if 1 > 0:
                print("KOM OP")
                print("nog even doorzetten je doel is bijna behaald")
                print("kom op nog een paar dagen te gaan")
                print("GEFELICITEERD je heb je doel behaald")
        elif answer == 2:
            print("jammer dit zal je terug pakken aan het einde")
    else:
        ("vul (1)ja of (2)nee in")
   
   
def eatHalf():

    print("je hebt de eet de helft methode gekozen")
    eat3 = input("je gaat er goed tegen aan je heb wel een hele broodje verdiendt Ja(1) of nee(2)")
    if eat3 == 1:
        print("geef maar op")
    elif eat3 == 2:
        print("misschien is er nog hoop voor jou")
    else:
        print("vul (1)ja of (2)nee in")
    if eat3 == "stop":
        print("ABC ik kap er mee")
    else:
        print("je bent lui ik snap het")

whichDiet()