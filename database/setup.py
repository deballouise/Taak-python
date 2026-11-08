import sqlite3
import configparser

class InternaatDatabase:
    def __init__(self):
        # 1. Lees het instellingenbestand uit
        config = configparser.ConfigParser()
        config.read('config.ini')
        
        # 2. Haal de locatie van de database op uit de sectie [database]
        self.db_locatie = config['database']['db_locatie']
        self.connectie = None

    def maak_connectie(self):
        """Maakt verbinding met de SQLite database."""
        try:
            # Connect maakt het bestand automatisch aan als het nog niet bestaat
            self.connectie = sqlite3.connect(self.db_locatie)
            print(f"[Succes] Verbonden met database op: {self.db_locatie}")
            return self.connectie
        except sqlite3.Error as foutmelding:
            print(f"[Fout] Kan niet verbinden met de database: {foutmelding}")
            return None

    def sluit_connectie(self):
        """Sluit de verbinding af."""
        if self.connectie:
            self.connectie.close()
            print("[Info] Databaseverbinding gesloten.")