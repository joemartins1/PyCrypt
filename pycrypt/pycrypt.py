from lib_joe import *
from crypt import *
from decrypt import *

def ascii():
    print("""
__________        _________                        __   
\______   \___.__.\_   ___ \_______ ___.__._______/  |_ 
 |     ___<   |  |/    \  \/\_  __ <   |  |\____ \   __|
 |    |    \___  |\     \____|  | \/\___  ||  |_> >  |  
 |____|    / ____| \______  /|__|   / ____||   __/|__|  
           \/             \/        \/     |__|         
PyCrypt made by Joe\n---------------------------------------------------------\n""")


def main():
    clear()
    sequence = []
    print("""
__________        _________                        __   
\______   \___.__.\_   ___ \_______ ___.__._______/  |_ 
 |     ___<   |  |/    \  \/\_  __ <   |  |\____ \   __|
 |    |    \___  |\     \____|  | \/\___  ||  |_> >  |  
 |____|    / ____| \______  /|__|   / ____||   __/|__|  
           \/             \/        \/     |__|         
Welcome to PyCrypt made by Joe\nPress enter to continue""")
    input()
    clear()
    ascii()
    number_sequence = int(input("Enter the rotor sequence number : "))
    for i in range(0, number_sequence):
        element = int(input(f"Enter the rotor sequence {i+1}: "))
        sequence.append(element)  
    clear()

    ascii()
    menu_choice = int(input("1 - Encrypt\n2 - Decrypt\n3 - Show rotors sequence\nPress your choice: "))
    if menu_choice == 1:
        clear()
        ascii()
        encrypt_choice = int(input("1 - Encrypt Direct Message\n2 - Encrypt Txt Message\n"))
        if encrypt_choice == 1:
            message = input("Enter message to encrypt: ")
            crypted_message = crypt_rotor(message, sequence)
            print("Encrypted message :", crypted_message)
        elif encrypt_choice == 2:
            txt = input("Enter a filename dest: ")
            message = read_txt(txt)
            crypted_message = crypt_rotor(message, sequence)
            write_txt("crypted_message.txt", crypted_message)
            print("Encrypted message in 'crypted_message.txt'")
        input("Press enter to continue")
        main()

    elif menu_choice == 2:
        clear()
        ascii()
        decrypt_choice = int(input("1 - Decrypt Direct Message\n2 - Decrypt Txt Message\n"))
        if decrypt_choice == 1:
            crypted_message = input("Enter message to decrypt: ")
            decrypted_message = decrypt_rotor(crypted_message, sequence)
            print("Decrypted message :", decrypted_message)
        elif decrypt_choice == 2:
            txt = input("Enter a filename dest: ")
            crypted_message = read_txt(txt)
            decrypted_message = decrypt_rotor(crypted_message, sequence)
            write_txt("decrypted_message.txt", decrypted_message)
            print("Decrypted message in 'decrypted_message.txt'")
        input("Press enter to continue")
        main()

    elif menu_choice == 3:
        clear()
        ascii()
        print("Rotors sequence : ", sequence)
        input("Press enter to continue")
        main()
    
    else:
        clear()
        print("Wrong choice")
        input("Press enter to continue")
        main()
    
main()