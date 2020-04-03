text = str(input("Welcome! Please, enter the text which you want to use: "))
def menu():
    print("[˘˘˘˘˘˘˘˘CAESAR CIPHER MENU˘˘˘˘˘˘˘˘]")
    choice = input("""
Which option do you want to use?
A: Encode text
B: Decode text
                    
> Please enter your choice: """)
    if choice == "A" or choice == "a":
        print('Your encoded text: ', Ceaser(text))
    elif choice == "B" or choice == "b":
        print("Your decoded text: \n", NOT_Ceaser(text).replace(":", " "))


def Ceaser(text):
    final = ""
    text = text.lower()
    edg = 3
    for i in range(len(text)):
        if ord(text[i]) > 122 - edg:
            final += chr(ord(text[i]) + edg - 26)
        else:
            final += chr(ord(text[i]) + edg)
    return final

def NOT_Ceaser(text):
    final = ""
    edg = 3
    edg0 = edg % 26
    for i in range(len(text)):
        sign = text[i]
        if (ord(sign) - edg0 < 97):
            final += chr(ord(sign) - edg0 + 26)
        else:
            final += chr(ord(sign) - edg0)
    final = final.replace("Y", "?")
    final = final.replace("F", ",")
    final = final.replace("H", ".")
    final = final.replace(";", '!')
    return final

menu()


