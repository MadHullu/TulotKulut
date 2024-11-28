def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Virhe, nollalla ei voi jakaa."
    return x / y

def calculator():
    print("Valitse laskutoimitus:")
    print("1. Yhteenlasku (+)")
    print("2. Vähennys (-)")
    print("3. Kertolasku (*)")
    print("4. Jakolasku (/)")

    choice = input("Syötä valintasi (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Syötä ensimmäinen luku: "))
        num2 = float(input("Syötä toinen luku: "))

        if choice == '1':
            print(f"Resultaatti: {add(num1, num2)}")
        elif choice == '2':
            print(f"Resultaatti: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Resultaatti: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Resultaatti: {divide(num1, num2)}")
    else:
        print("Virheellinen syöte.")

if __name__ == "__main__":
    calculator()
