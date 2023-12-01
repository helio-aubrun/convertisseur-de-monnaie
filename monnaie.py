from forex_python.converter import CurrencyRates
import json
import os

def convert(amount, from_c, to_c, rates):
    if from_c == to_c:
        return amount
    if from_c not in rates or to_c not in rates:
        return None
    rate = rates[to_c] / rates[from_c]
    converted_amount = amount * rate
    return converted_amount

def save_conv(history):
    with open('conversion_history.json', 'w') as file:
        json.dump(history, file)

def load_conversion_history():
    if os.path.exists('conversion_history.json'):
        with open('conversion_history.json', 'r') as file:
            return json.load(file)
    return []

def main():
    c = CurrencyRates()
    rates = c.get_rates('USD')
    conversion_history = load_conversion_history()
    while True:
        print("\nDevises disponibles:", ', '.join(rates.keys()))
        amount = float(input("Entrez le montant à convertir : "))
        from_currency = input("Entrez la devise source : ").upper()
        to_currency = input("Entrez la devise cible : ").upper()
        converted_amount = convert(amount, from_currency, to_currency, rates)
        if converted_amount is not None:
            print(f"{amount} {from_currency} équivaut à {converted_amount:.2f} {to_currency}")
            conversion_history.append({
                'amount': amount,
                'from_currency': from_currency,
                'to_currency': to_currency,
                'converted_amount': converted_amount
            })
            save_conv(conversion_history)
        else:
            print("Conversion impossible. Vérifiez les devises saisies.")
        add_another = input("Voulez-vous effectuer une autre conversion ? (Oui/Non) : ")
        if add_another.lower() != 'oui':
            break
if __name__ == "__main__":
    main()