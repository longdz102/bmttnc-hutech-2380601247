ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

class PlayFairCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    # ================= MATRIX =================
    def create_playfair_matrix(self, key):
        key = key.upper().replace("J", "I")

        seen = set()
        matrix = []

        for char in key:
            if char in self.alphabet and char not in seen:
                matrix.append(char)
                seen.add(char)

        for char in self.alphabet:
            if char not in seen:
                matrix.append(char)

        return [matrix[i:i+5] for i in range(0, 25, 5)]

    # ================= FIND =================
    def find_letter_coords(self, matrix, letter):
        letter = letter.upper()
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == letter:
                    return r, c
        return -1, -1   # 🔥 tránh crash

    # ================= PREPARE TEXT =================
    def prepare_text(self, text):
        text = text.upper().replace("J", "I")
        text = "".join([c for c in text if c.isalpha()])

        result = ""
        i = 0

        while i < len(text):
            a = text[i]
            b = text[i+1] if i+1 < len(text) else "X"

            if a == b:
                result += a + "X"
                i += 1
            else:
                result += a + b
                i += 2

        if len(result) % 2 != 0:
            result += "X"

        return result

    # ================= ENCRYPT =================
    def playfair_encrypt(self, plain_text, key):
        matrix = self.create_playfair_matrix(key)
        text = self.prepare_text(plain_text)

        result = ""

        for i in range(0, len(text), 2):
            a, b = text[i], text[i+1]

            r1, c1 = self.find_letter_coords(matrix, a)
            r2, c2 = self.find_letter_coords(matrix, b)

            if r1 == -1 or r2 == -1:
                continue

            if r1 == r2:
                result += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]

            elif c1 == c2:
                result += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]

            else:
                result += matrix[r1][c2] + matrix[r2][c1]

        return result

    # ================= DECRYPT =================
    def playfair_decrypt(self, cipher_text, key):
        matrix = self.create_playfair_matrix(key)
        text = cipher_text.upper()

        result = ""

        for i in range(0, len(text), 2):
            a, b = text[i], text[i+1]

            r1, c1 = self.find_letter_coords(matrix, a)
            r2, c2 = self.find_letter_coords(matrix, b)

            if r1 == -1 or r2 == -1:
                continue

            if r1 == r2:
                result += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]

            elif c1 == c2:
                result += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]

            else:
                result += matrix[r1][c2] + matrix[r2][c1]

        return result