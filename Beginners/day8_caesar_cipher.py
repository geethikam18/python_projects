from day8_caesar_cipher_logo import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




'''
def encrypt(t,s):
    cipher_text = ""
    for char in t:
        pos = alphabet.index(char)
        new_pos = pos + s
        new_char = alphabet[new_pos]
        cipher_text += new_char
    print(f"The encoded text is {cipher_text}\n")


def decode(t, s):
    plain_text = ""
    for char in t:
        pos = alphabet.index(char)
        new_pos = pos - s
        new_char = alphabet[new_pos]
        plain_text += new_char
    print(f"The decoded text is {plain_text}\n")


if direction == "encode":
    encrypt(t = text, s = shift)
elif direction == "decode":
    decode(t=text, s=shift)

'''

def caesar(start, s, dir):
    end = ""
    if dir == 'decode':
        s *= -1
    for char in start:
        if char in alphabet:
            pos =  alphabet.index(char)
            new_pos = pos + s
            end += alphabet[new_pos]
        else:
            end += char

    print(f"The {dir}d text is {end}\n")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift %= 26

    caesar(start = text, s = shift, dir = direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n" )
    if result == 'no':
        should_continue = False
        print("Goodbye")


