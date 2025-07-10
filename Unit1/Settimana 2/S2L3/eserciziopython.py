# Esercizio: Scrivere un programma in Python che genera un nome per una band musicale utilizzando due input forniti dall'utente:
#  la città di origine e il nome del proprio animale domestico.

def nomeBand (città, animale):
    return f"Il nome della tua band potrebbe essere: {città} {animale}"

città = input("Inserisci il nome della città: ")
animale = input("Inserisci il nome del tuo animale  domestico: ")

print(nomeBand(città, animale))




