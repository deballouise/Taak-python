from database.setup import InternaatDatabase
from models.leerling import Leerling
from database.queries import voeg_leerling_toe, toon_alle_leerlingen, registreer_toestemming, controleer_vertrek

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
    print("\nWelkom bij het leerlingenoverzicht van Internaat Aksent.")
    
    db_manager = InternaatDatabase()
    db_manager.maak_connectie()
    db_manager.maak_tabellen()
    
    while True:
        toon_menu()
        keuze = input("Kies een actie (1-5): ")

        if keuze == '1':
            print("\n--- Nieuwe Leerling Inschrijven ---")
            invoer_naam = input("Wat is de naam? ")
            invoer_adres = input("Wat is het adres? ")
            invoer_datum = input("Wat is de geboortedatum (bijv. 15-05-2010)? ")
            nieuwe_leerling = Leerling(invoer_naam, invoer_adres, invoer_datum)
            voeg_leerling_toe(db_manager.connectie, nieuwe_leerling)
            
        elif keuze == '2':
            print("\n--- Toestemming Registreren ---")
            toon_alle_leerlingen(db_manager.connectie)

            print("-" * 30)
            invoer_id = input("Typ het ID van de leerling: ")
            invoer_toestemming = input("Mag deze leerling vertrekken? (Ja/Nee): ")
            invoer_opmerking = input("Opmerking (bijv. 'Na 13u', of laat leeg): ")        
            registreer_toestemming(db_manager.connectie, invoer_id, invoer_toestemming, invoer_opmerking)
            
        elif keuze == '3':
            print("\n--- Controleer Vertrek ---")
            toon_alle_leerlingen(db_manager.connectie)

            print("-" * 30)
            invoer_id = input("Typ het ID van de leerling die wil vertrekken: ")
            controleer_vertrek(db_manager.connectie, invoer_id)
            
        elif keuze == '4':
            print("\n[!] Actie: Code om CSV/Excel rapport te maken komt hier.")
        elif keuze == '5':
            print("\nProgramma wordt afgesloten.")
            db_manager.sluit_connectie()
            break
        else:
            print("\n[Fout] Ongeldige keuze. Typ een getal van 1 tot en met 5.")

if __name__ == "__main__":
    main()