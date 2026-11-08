def voeg_leerling_toe(connectie, leerling):
    """Zet een nieuw leerling-object in de database."""
    cursor = connectie.cursor()
    
    sql = "INSERT INTO Leerlingen (naam, adres, geboortedatum) VALUES (?, ?, ?)"
    waarden = (leerling.naam, leerling.adres, leerling.geboortedatum)
    
    cursor.execute(sql, waarden)
    connectie.commit()
    
    print(f"\n[Succes] {leerling.naam} is bewaard in de database!")