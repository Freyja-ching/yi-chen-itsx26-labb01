# app/main.py
# IT-Security Labb 01 - Target Program for Risk Assessment

def main():
    print("Välkommen till enkla miniräknare!")
    print("Tillgängliga operationer: +, -, *, /")
    
    num1 = float(input("Skriv in ett första tal: "))
    num2 = float(input("Skriv in ett andra tal: "))
    op = input("Välj operation (+, -, *, /): ")
    
    if op == '+':
        res = num1 + num2
    elif op == '-':
        res = num1 - num2
    elif op == '*':
        res = num1 * num2
    elif op == '/':
        if num2 != 0:
            res = num1 / num2
        else:
            print("Fel: Kan inte dividera med noll!")
            return
    else:
        print("Ogiltig operation!")
        return

    print(f"Resultat: {res}")

if __name__ == "__main__":
    main()
