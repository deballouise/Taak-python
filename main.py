def toon_menu():
    print("\n" + "="*30)
    print("       INTERNAAT AKSENT  ")
    print("="*30)
    print("1. Nieuwe leerling toevoegen")
    print("2. Toestemming registreren of wijzigen")
    print("3. Controleer vertrek (Woensdag check)")
    print("4. Genereer vertreklijst (Rapport)")
    print("5. Afsluiten")
    print("-" * 30)

def main():
    print("\n Welkom bij het leerlingenoverzicht van Internaat Aksent.")
    
    while True:
        toon_menu()
        keuze = input("Kies een actie (1-5): ")

        if keuze == '1':
            print("\n[!] Actie: Code om leerling toe te voegen komt hier.")
        elif keuze == '2':
            print("\n[!] Actie: Code om toestemming te wijzigen komt hier.")
        elif keuze == '3':
            print("\n[!] Actie: Code om vertrek te controleren komt hier.")
        elif keuze == '4':
            print("\n[!] Actie: Code om CSV/Excel rapport te maken komt hier.")
        elif keuze == '5':
            print("\nProgramma wordt afgesloten.")
            break
        else:
            print("\n[Fout] Ongeldige keuze. Typ een getal van 1 tot en met 5.")

if __name__ == "__main__":
    main()