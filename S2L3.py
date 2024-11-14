print("Ciao! Ora scopriremo il nome della tua futura band!")
risposta = input("Sei pronto? (si/no): ")
if risposta == "si":
    continuare = True
else:
    continuare = False 
if continuare:
    print("Molto bene!")
else:
    print("Non diventerai mai una rockstar. Addios")
    exit()

risposta1=input("Il primo passo è inserire il nome del tuo animale domestico! Spero tu ne abbia uno. (si/no): ")
if risposta1 =="si":
    continuare = True
else:
    continuare = False
if continuare:
    print("Daje, continuiamo!")
else:
    print("Se non ce l'hai rubane uno e ritorna.")
    exit()
nome = input("Come si chiama? ")
print("Non male come nome " + nome, "!")

print("Ora ci siamo quasi! Come si chiama il luogo da cui vieni?")
luogo = input("")
print("Il nome della tua band è compiuto. Ciao "+nome + luogo, "!")

