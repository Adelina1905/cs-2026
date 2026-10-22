from alphabet import ALPHABET, CODE, N

def vigenere(text, key, sign):
    """Shift letter i by the code of key letter i mod len(key)."""
    out = []
    for i, letter in enumerate(text):
        k = CODE[key[i % len(key)]]
        out.append(ALPHABET[(CODE[letter] + sign * k) % N])
    return "".join(out)


def encrypt(text, key):
    return vigenere(text, key, 1)       # c = (m + k) mod n


def decrypt(text, key):
    return vigenere(text, key, -1)      # m = (c - k) mod n
