#  an algorithm to decrypt internal messages using Caesar's Cipher.
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesars_cipher(ciphertext: str, right_shift: bool=True, key: int=3) -> str:
    ''' 
    This functions decrypts a ciphertext.;
    - ciphertext : message to be decrypted.
    - right_shift : specifies the direction of decryption. By default the shift is to the right.
    - key : specifies the number of steps to move from the current index.
    
    '''
    plaintext = ''
    
    ciphertext = ciphertext.upper()   
    if right_shift == True:                                                
        for letter in ciphertext:
            if letter in alphabet:                                        # Checks the letters in the ciphertext
                new_pos = (alphabet.index(letter) + key) % 26             # Returns the reminder of the division by 26
                plaintext += alphabet[new_pos]
            else:
                plaintext += letter  
    else:
        for letter in ciphertext:                                          # Performs the left shift
            if letter in alphabet:        
                new_pos = (alphabet.index(letter) - key) % 26
                plaintext += alphabet[new_pos]
            else:
                plaintext += letter

    return plaintext
                                              
