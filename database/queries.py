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