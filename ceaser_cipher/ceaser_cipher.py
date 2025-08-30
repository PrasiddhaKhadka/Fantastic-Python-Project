
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = str(input('Type "encode" to encrypt, type "decode" to decrypt:\n'))
text = str(input('Type your message:\n'))
shift = int(input('Type the shift number:\n'))


def encrypt(plain_text,shift_amount):
    cipher = ""
    for letter in plain_text:
        if letter not in alphabet:
            cipher += letter
        else: 
            position = alphabet.index(letter)

        
            new_position = position + shift_amount
            # for handling overflow
            new_position = new_position % len(alphabet)
            new_letter = alphabet[new_position]
            cipher += new_letter
    print(f"The encoded text is {cipher.capitalize()}")


def decrypt(cipher_text,shift_amount):
    plain = ""
    for letter in cipher_text:
        if letter not in alphabet:
            plain += letter
        else:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            # for handling overflow
            new_position = new_position % len(alphabet)
            new_letter = alphabet[new_position]
            plain += new_letter
    print(f"The decoded text is {plain.capitalize()}")


while True:
    if direction == "encode":
        encrypt(plain_text=text.lower(),shift_amount=shift)
        break
    elif direction == "decode":
        decrypt(cipher_text=text.lower(),shift_amount=shift)
        break
    else:
        print("Please type 'encode' or 'decode'")
        direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')