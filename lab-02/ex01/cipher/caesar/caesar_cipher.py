from . import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted_text = []

        for letter in text:

            # 👉 GIỮ NGUYÊN KHOẢNG TRẮNG / KÝ TỰ KHÁC
            if letter not in self.alphabet:
                encrypted_text.append(letter)
                continue

            letter_index = self.alphabet.index(letter)
            output_index = (letter_index + key) % alphabet_len
            encrypted_text.append(self.alphabet[output_index])

        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypted_text = []

        for letter in text:

            # 👉 GIỮ NGUYÊN KÝ TỰ KHÁC
            if letter not in self.alphabet:
                decrypted_text.append(letter)
                continue

            letter_index = self.alphabet.index(letter)
            output_index = (letter_index - key) % alphabet_len
            decrypted_text.append(self.alphabet[output_index])

        return "".join(decrypted_text)