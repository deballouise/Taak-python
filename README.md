# Taak-python



Doel:

Programma om het overzicht te behouden op wie op woensdagnamiddag het internaat mag verlaten.
Dit gebeurt op basis van de leeftijd van de leerlingen en op basis van de toestemming die de ouders al dan niet gegeven hebben in het begin van het schooljaar.





Basisfuncties:

* Nieuwe leerling toevoegen (met naam, adres en geboortedatum)
* Toestemming van de ouders registreren (opties Ja of Nee; opmerking)
* Controle per leerling (uitrekenen leeftijd en controleren van toestemming van ouders)
* Rapport genereren van alle leerlingen met toestemming





Hoe het project zelf installeren:

* Clone de repository naar je lokale machine.



* Virtual Environment:

&#x20;  Maak een venv aan (`python -m venv venv`) en activeer deze. Installeer eventuele benodigdheden via `pip install -r requirements.txt`.



* Instellingenbestand (Belangrijk!):

&#x20;  In de hoofdmap vind je het bestand `config\_example.ini`. Maak in deze map zelf een nieuw bestand aan genaamd `config.ini`. 

&#x20;  Kopieer de structuur van het voorbeeld en vul het lokale pad naar jouw gewenste database-locatie in. (Het `config.ini` bestand en de `.db` bestanden worden genegeerd door Git).



* Uitvoeren:

&#x20;  Start het programma door `python main.py` uit te voeren in de terminal. De applicatie zal zelf de tabellen aanmaken in de SQLite database als deze nog niet bestaan.

