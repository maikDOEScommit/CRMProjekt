# Dein Kundenmanagement-System

kunden = {} # Ein Dictionary zum Speichern der Kunden. Schlüssel: Kundenname, Wert: Dictionary mit Details

def kunden_anzeigen():
    # Überprüfe, ob das 'kunden'-Dictionary leer ist
    if not kunden:
        print("Der Katalog ist leer.")
        return # Beende die Funktion hier, wenn keine Kunden vorhanden sind

    print("\n--- Deine Kundenliste ---")
    # Iteriere über alle Kunden im Dictionary
    for name, details in kunden.items():
        print(f"Name: {name}")
        # Verwende .get(), um 'N/A' anzuzeigen, falls ein Detail fehlt
        print(f"  E-Mail: {details.get('email', 'N/A')}")
        print(f"  Telefon: {details.get('telefon', 'N/A')}")
        print("-------------------------")

# Test der Funktion (diese Zeile wird später durch ein Menü ersetzt)
# kunden_anzeigen()

