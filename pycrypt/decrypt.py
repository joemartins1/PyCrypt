from lib_joe import *

def gap_rotor(char, gap):
    char_min = ord('a') if char_is_lower(char) else ord('A')
    gap = gap % 26
    return chr(((ord(char) - char_min + gap) % 26) + char_min)


def gap_rotor_inverse(char, gap):
    return gap_rotor(char, -gap)


def decrypt_rotor(crypted_message, sequence_rotors):
    decrypted_message = ""
    sequence_lenght = len(sequence_rotors)
    
    for i, letter in enumerate(crypted_message):
        gap = sequence_rotors[i % sequence_lenght]
        if char_is_letter(letter):
            decrypted_message += gap_rotor_inverse(letter, gap)
        else:
            decrypted_message += letter
    
    return decrypted_message


