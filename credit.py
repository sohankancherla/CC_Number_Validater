def main():
    try:
        cc_number = str(int(input("Card Number: ")))
        if not 13 <= len(cc_number) <= 16:
            print("INVALID")
        elif not checksum(cc_number):
            print("INVALID")
        else:
            card_brand = brand(cc_number)
            print(card_brand)
    except ValueError:
        print("Incorrect format, please do not include any spaces or dashes between the numbers")
    return

# Luhn's Alogrithim to check if a credit card num is valid
def checksum(cc_number):
    sum = 0
    for i in range(len(cc_number)-2, -1, -2):
        product = str(int(cc_number[i]) * 2)
        for digit in product:
            sum += int(digit)
    
    for j in range(len(cc_number)-1, -1, -2):
        sum += int(cc_number[j])
    if sum % 10 == 0:
        return True
    return False

def brand(cc_number):
    if cc_number[:2] in ["34", "37"] and len(cc_number) == 15:
        return "AMEX"
    elif cc_number[:2] in ["51", "52", "53", "54", "55"] and len(cc_number) == 16:
        return "MASTERCARD"
    elif cc_number[0] == "4" and 13 <= len(cc_number) <= 16:
        return "VISA"
    else:
        return "INVALID"

main()
