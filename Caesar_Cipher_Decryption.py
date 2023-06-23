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
