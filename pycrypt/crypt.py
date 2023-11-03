from lib_joe import *

def gap_rotor(char, gap):
    char_min = ord('a') if char_is_lower(char) else ord('A')
    gap = gap % 26
    return chr(((ord(char) - char_min + gap) % 26) + char_min)


def crypt_rotor(message, sequence_rotors):
    crypt_message = ""
    sequence_lenght = len(sequence_rotors)
    
    for i, letter in enumerate(message):
        gap = sequence_rotors[i % sequence_lenght]
        if char_is_letter(letter):
            crypt_message += gap_rotor(letter, gap)
        else:
            crypt_message += letter
    
    return crypt_message


