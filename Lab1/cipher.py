from alphabet import ALPHABET

def shift(text, key, alphabet=ALPHABET):
    """Replace every letter x by the letter with code (x + key) mod n.

    The codes come from the position of the letter in `alphabet`, never from
    ASCII/Unicode values. A negative key gives decryption.
    """
    code = {letter: index for index, letter in enumerate(alphabet)}
    n = len(alphabet)
    out = []
    for letter in text:
        y = (code[letter] + key) % n
        if y < 0:          # Python's % is never negative, kept for clarity
            y += n
        out.append(alphabet[y])
    return "".join(out)


def encrypt(text, key, alphabet=ALPHABET):
    return shift(text, key, alphabet)        # c = (x + k) mod n


def decrypt(text, key, alphabet=ALPHABET):
    return shift(text, -key, alphabet)       # m = (y - k) mod n
