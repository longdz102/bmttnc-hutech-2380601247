class RailFenceCipher:
    def __init__(self):
        pass

    # ================= ENCRYPT =================
    def rail_fence_encrypt(self, plain_text, num_rails):

        if num_rails < 2:
            raise ValueError("Rails must be >= 2")

        if not plain_text:
            return ""

        rails = [[] for _ in range(num_rails)]

        rail_index = 0
        direction = 1

        for char in plain_text:
            rails[rail_index].append(char)

            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1

            rail_index += direction

        return "".join("".join(r) for r in rails)

    # ================= DECRYPT =================
    def rail_fence_decrypt(self, cipher_text, num_rails):

        if num_rails < 2:
            raise ValueError("Rails must be >= 2")

        if not cipher_text:
            return ""

        # 1. tính độ dài từng rail
        rail_lengths = [0] * num_rails

        rail_index = 0
        direction = 1

        for _ in cipher_text:
            rail_lengths[rail_index] += 1

            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1

            rail_index += direction

        # 2. chia ciphertext
        rails = []
        start = 0

        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))
            start += length

        # 3. đọc lại zigzag
        result = ""

        rail_index = 0
        direction = 1

        for _ in cipher_text:
            result += rails[rail_index].pop(0)

            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1

            rail_index += direction

        return result