logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet_upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
direction = input("Type whether to encode to incrypt or Decode to decrypt\n").lower()
text = input("What statement do you want to encode or decode\n")
shift = int(input("what shift amount do you want to apply to your code\n"))
def ceaser(direction, text, shift):
    #if the shift number is greater than 26 then the modulus of the shift by 26 is the new shift number
    if shift > 26:
        shift = shift % 26  
    def encrypt(text, shift):
    #in the text, we have to figure out the position of the letters in the alphabet
    #afterward we have to figure out the position of the letter in the alphabet
    #from there, we have to add the index of the given letter + 5
        position = 0
        encrypted = ""
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift
                new_letter = alphabet[new_position]
                encrypted += new_letter
            elif char in alphabet_upper:
                position = alphabet_upper.index(char)
                new_position = position + shift
                new_letter = alphabet_upper[new_position]
                encrypted += new_letter
            else:
                encrypted += char
        print(encrypted)
    def decrypt(text, shift):
        position = 0
        decrypted = ""
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position - shift
                new_letter = alphabet[new_position]
                decrypted += new_letter
            elif char in alphabet_upper:
                position = alphabet_upper.index(char)
                new_position = position - shift
                new_letter = alphabet_upper[new_position]
                decrypted += new_letter
            else:
                decrypted += char
        print(decrypted)
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("invalid_choice")
ceaser(direction, text, shift)
cont = input("do you wish to continue\n").lower() 
while cont == "yes":
    direction = input("Type whether to encode to incrypt or Decode to decrypt\n").lower()
    text = input("What statement do you want to encode or decode\n").lower()
    shift = int(input("what shift amount do you want to apply to your code\n"))
    ceaser(direction, text, shift)
    cont = input("do you wish to continue\n").lower()
if "no" == cont:
    print("goodbye")  
     