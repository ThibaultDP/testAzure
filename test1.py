def main():
    try:
        # Vraag de gebruiker om de twee getallen in te voeren
        num1 = float(input("Voer het eerste getal in: "))
        num2 = float(input("Voer het tweede getal in: "))
        
        # Bereken de som van de twee getallen
        result = num1 + num2
        
        # Toon het resultaat aan de gebruiker
        print("De som van {} en {} is: {}".format(num1, num2, result))
        
    except ValueError:
        print("Ongeldige invoer. Zorg ervoor dat je geldige getallen invoert.")

if __name__ == "__main__":
    main()

