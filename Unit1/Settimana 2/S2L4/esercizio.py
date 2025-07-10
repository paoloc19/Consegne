#Si scriva un programma in Python che in base alla scelta dellʼutente permetta di calcolare il perimetro 
#di diverse figure geometriche (scegliete pure quelle che volete voi)c

forma = input("scegli la figura che vuoi\n Quadrato-> 1\nCerchio-> 2\nRettangolo-> 3\n")
if forma == "1":
        lato = float(input("Scegli il lato del quadrato\n"))
        print(f"Il perimetro del tuo quadrato è {lato * 4} ")
elif forma == "2":
        raggio = float(input("Scegli il raggio\n"))
        print(f"Il perimetro del tuo cerchio è  {2 * raggio *3.14}")
elif forma == "3":
        base = float(input("Scegli la base\n"))
        altezza = float(input("Scegli l'altezza\n"))
        print(f"Il perimetro del tuo rettangolo è {base * 2 + altezza * 2}")
else: 
    print("Fai una scelta valida")       
