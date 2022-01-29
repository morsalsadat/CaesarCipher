alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
 
def caesar(text, shift, direction):
  if direction == 'encode':
    encoded = ""
    for letter in text:
      if alphabet.index(letter) + shift > 26:
        encoded += alphabet[alphabet.index(letter) - 26 + shift]
      else:
        encoded += alphabet[alphabet.index(letter) + shift]
    print(f"The {direction}d message is: {encoded}")
  else:
    decoded = ""
    for letter in text:
      if alphabet.index(letter) - shift < 0:
        decoded += alphabet[alphabet.index(letter) + 26 - shift]
      else:
        decoded += alphabet[alphabet.index(letter) - shift]
    print(f"The {direction}d message is: {decoded}")

caesar(text, shift, direction)