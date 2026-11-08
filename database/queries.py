from datetime import datetime
import csv

def voeg_leerling_toe(connectie, leerling):
    """Zet een nieuw leerling-object in de database."""
    cursor = connectie.cursor()
    
    sql = "INSERT INTO Leerlingen (naam, adres, geboortedatum) VALUES (?, ?, ?)"
    waarden = (leerling.naam, leerling.adres, leerling.geboortedatum)
    
    cursor.execute(sql, waarden)
    connectie.commit()
    
    print(f"\n[Succes] {leerling.naam} is bewaard in de database!")
    
    
def toon_alle_leerlingen(connectie):
    """Haalt een lijst op van alle leerlingen in de database."""
    cursor = connectie.cursor()
    cursor.execute("SELECT id, naam FROM Leerlingen")
    rijen = cursor.fetchall()
    
    print("\n--- Lijst van geregistreerde leerlingen ---")
    for rij in rijen:
        print(f"ID: {rij[0]} | Naam: {rij[1]}")
    return rijen


def registreer_toestemming(connectie, leerling_id, toestemming, opmerking):
    """Slaat de toestemming van de ouders op in de tweede tabel."""
    cursor = connectie.cursor()
    
    sql = "INSERT INTO Toestemmingen (leerling_id, toestemming_ouders, opmerking) VALUES (?, ?, ?)"
    waarden = (leerling_id, toestemming, opmerking)
    
    cursor.execute(sql, waarden)
    connectie.commit()
    
    print("[Succes] De toestemming is geregistreerd in de database!")
    
    
def controleer_vertrek(connectie, leerling_id):
    """Controleert leeftijd en toestemming van een leerling."""
    cursor = connectie.cursor()
    
    sql = """
        SELECT Leerlingen.naam, Leerlingen.geboortedatum, Toestemmingen.toestemming_ouders 
        FROM Leerlingen 
        LEFT JOIN Toestemmingen ON Leerlingen.id = Toestemmingen.leerling_id 
        WHERE Leerlingen.id = ?
    """
    cursor.execute(sql, (leerling_id,))
    resultaat = cursor.fetchone()
    
    if resultaat == None:
        print("[Fout] Deze leerling is niet gevonden in de database.")
        return

    naam = resultaat[0]
    geboortedatum_tekst = resultaat[1]
    toestemming = resultaat[2]

    try:
        geboorte_datum = datetime.strptime(geboortedatum_tekst, "%d-%m-%Y")
        vandaag = datetime.now()
        leeftijd = vandaag.year - geboorte_datum.year - ((vandaag.month, vandaag.day) < (geboorte_datum.month, geboorte_datum.day))
    except:
        print("[Fout] De geboortedatum is verkeerd ingevuld. Gebruik het formaat dd-mm-jjjj.")
        return

    print(f"\n--- Resultaat voor {naam} ---")
    print(f"Leeftijd: {leeftijd} jaar oud")
    
    if toestemming == None:
        toestemming = "Nog niet ingevuld"
    print(f"Toestemming ouders: {toestemming}")
    
    if leeftijd >= 16 and toestemming == 'Ja':
        print(">> CONCLUSIE: Deze leerling mag het internaat verlaten!")
    else:
        print(">> CONCLUSIE: Deze leerling mag NIET vertrekken.")


def genereer_rapport(connectie):
    """Maakt een CSV-bestand van alle leerlingen die vandaag mogen vertrekken."""
    cursor = connectie.cursor()
    sql = """
        SELECT Leerlingen.naam, Leerlingen.geboortedatum 
        FROM Leerlingen 
        JOIN Toestemmingen ON Leerlingen.id = Toestemmingen.leerling_id 
        WHERE Toestemmingen.toestemming_ouders = 'Ja'
    """
    cursor.execute(sql)
    rijen = cursor.fetchall()
    mogen_vertrekken = []
    vandaag = datetime.now()
    
    for rij in rijen:
        naam = rij[0]
        geboortedatum_tekst = rij[1]
        
        try:
            geboorte_datum = datetime.strptime(geboortedatum_tekst, "%d-%m-%Y")
            leeftijd = vandaag.year - geboorte_datum.year - ((vandaag.month, vandaag.day) < (geboorte_datum.month, geboorte_datum.day))
            if leeftijd >= 16:
                mogen_vertrekken.append([naam, leeftijd])
        except:
            pass 
            
    bestandsnaam = "vertreklijst.csv"
    
    with open(bestandsnaam, mode='w', newline='') as bestand:
        schrijver = csv.writer(bestand, delimiter=';')
        schrijver.writerow(['Naam', 'Leeftijd (Jaren)']) 
        
        for leerling in mogen_vertrekken:
            schrijver.writerow(leerling)
            
    print(f"\n[Succes] Het rapport is klaargezet als '{bestandsnaam}' in je map!")         