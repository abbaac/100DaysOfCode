from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(switch, string, shift_number):
    token = []
    if switch == "decode":
        shift_number *= -1
    for i in list(string):
        if i in alphabet:
            token.append(alphabet[(alphabet.index(i)+shift_number)%26])           
        else:
            token.append(i)
    print(f"The {switch}d text is " + "".join(token))

    
print(logo)
redo = True
while redo == True:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)
    choice = input("\nWould you like to go again yes/no: ").lower()
    if choice != "yes":
        redo = False
print("Goodbye")
