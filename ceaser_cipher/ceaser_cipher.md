# Caesar Cipher

The **Caesar cipher** is one of the simplest and most widely known encryption techniques. It is a type of **substitution cipher** in which each letter in the plaintext is shifted a certain number of places down or up the alphabet.

For example, with a shift of `3`:
- `A` becomes `D`
- `B` becomes `E`
- `Z` becomes `C` (wrapping around the alphabet using modulo)

## How it works
1. Take each letter in the input text.
2. Find its position in the alphabet.
3. Add the shift amount to the position.
4. Use modulo to wrap around if the new position exceeds the alphabet length.
5. Replace the original letter with the new shifted letter.

## Why use it
- Demonstrates the basic concept of encryption.
- Helps understand modular arithmetic in programming.
- Useful as an introductory example in cryptography.

## Example in Python
```python
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plain_text, shift_amount):
    cipher = ""
    for letter in plain_text.lower():
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            cipher += alphabet[new_position]
        else:
            cipher += letter
    return cipher

text = "Zebra"
shift = 3
print(encrypt(text, shift))  # Output: "cheud"
