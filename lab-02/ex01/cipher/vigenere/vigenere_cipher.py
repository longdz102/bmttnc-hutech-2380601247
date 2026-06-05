class VigenereCipher:
    def __init__(self):
        pass

    # ================= VALIDATE KEY =================
    def validate_key(self, key):
        if not key or not key.isalpha():
            raise ValueError("Key must be alphabetic (A–Z only)")
        return key.upper()

    # ================= ENCRYPT =================
    def vigenere_encrypt(self, plain_text, key):

        key = self.validate_key(key)

        encrypted_text = ""
        key_index = 0

        for char in plain_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)]) - ord('A')

                if char.isupper():
                    encrypted_text += chr(
                        (ord(char) - ord('A') + key_shift) % 26 + ord('A')
                    )
                else:
                    encrypted_text += chr(
                        (ord(char) - ord('a') + key_shift) % 26 + ord('a')
                    )

                key_index += 1
            else:
                encrypted_text += char

        return encrypted_text

    # ================= DECRYPT =================
    def vigenere_decrypt(self, cipher_text, key):

        key = self.validate_key(key)

        decrypted_text = ""
        key_index = 0

        for char in cipher_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)]) - ord('A')

                if char.isupper():
                    decrypted_text += chr(
                        (ord(char) - ord('A') - key_shift) % 26 + ord('A')
                    )
                else:
                    decrypted_text += chr(
                        (ord(char) - ord('a') - key_shift) % 26 + ord('a')
                    )

                key_index += 1
            else:
                decrypted_text += char

        return decrypted_text