from flask import Flask, render_template, request

from ex01.cipher.caesar import CaesarCipher
from ex01.cipher.playfair import PlayFairCipher
from ex01.cipher.railfence import RailFenceCipher
from ex01.cipher.vigenere import VigenereCipher

app = Flask(__name__)

# ================= HOME =================
@app.route("/")
def home():
    return render_template("index.html")


# ================= CAESAR =================
@app.route("/caesar")
def caesar():
    return render_template("caesar.html")


@app.route("/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form.get("inputPlainText", "")
    key = request.form.get("inputKeyPlain", "")

    if not text:
        return "Plain text required"

    if not key.isdigit():
        return "Key must be number (0–25)"

    key = int(key)

    if key < 0 or key > 25:
        return "Key must be in range 0–25"

    cipher = CaesarCipher()
    return f"Encrypted: {cipher.encrypt_text(text, key)}"


@app.route("/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form.get("inputCipherText", "")
    key = request.form.get("inputKeyCipher", "")

    if not key.isdigit():
        return "Key must be number (0–25)"

    key = int(key)

    if key < 0 or key > 25:
        return "Key must be in range 0–25"

    cipher = CaesarCipher()
    return f"Decrypted: {cipher.decrypt_text(text, key)}"


# ================= PLAYFAIR =================
@app.route("/playfair")
def playfair_page():
    return render_template("playfair.html")


@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form.get("inputPlainText", "")
    key = request.form.get("inputKeyPlain", "")

    if not text:
        return "Plain text required"

    if not key or not key.isalpha():
        return "Key must contain only letters A–Z"

    key = key.upper()

    cipher = PlayFairCipher()
    return f"Encrypted: {cipher.playfair_encrypt(text, key)}"


@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form.get("inputCipherText", "")
    key = request.form.get("inputKeyCipher", "")

    if not key or not key.isalpha():
        return "Key must contain only letters A–Z"

    key = key.upper()

    cipher = PlayFairCipher()
    return f"Decrypted: {cipher.playfair_decrypt(text, key)}"


# ================= RAIL FENCE =================
@app.route("/railfence")
def railfence_page():
    return render_template("railfence.html")


@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    text = request.form.get("inputPlainText", "")
    key = request.form.get("inputKeyPlain", "")

    if not key.isdigit():
        return "Key must be number"

    key = int(key)

    if key < 2:
        return "Rails must be >= 2"

    cipher = RailFenceCipher()
    return f"Encrypted: {cipher.rail_fence_encrypt(text, key)}"


@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    text = request.form.get("inputCipherText", "")
    key = request.form.get("inputKeyCipher", "")

    if not key.isdigit():
        return "Key must be number"

    key = int(key)

    if key < 2:
        return "Rails must be >= 2"

    cipher = RailFenceCipher()
    return f"Decrypted: {cipher.rail_fence_decrypt(text, key)}"


# ================= VIGENERE =================
@app.route("/vigenere")
def vigenere_page():
    return render_template("vigenere.html")


@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form.get("inputPlainText", "")
    key = request.form.get("inputKeyPlain", "")

    if not text:
        return "Plain text required"

    if not key or not key.isalpha():
        return "Key must be alphabetic (A–Z)"

    key = key.upper()

    cipher = VigenereCipher()
    return f"Encrypted: {cipher.vigenere_encrypt(text, key)}"


@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form.get("inputCipherText", "")
    key = request.form.get("inputKeyCipher", "")

    if not key or not key.isalpha():
        return "Key must be alphabetic (A–Z)"

    key = key.upper()

    cipher = VigenereCipher()
    return f"Decrypted: {cipher.vigenere_decrypt(text, key)}"


# ================= RUN =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)