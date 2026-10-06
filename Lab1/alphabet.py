# Table 2: the Romanian alphabet (n = 31), letter codes A = 0 ... Z = 30.
# The code of a letter is its index in this list.
ALPHABET = list("AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ")
LOWER = list("aăâbcdefghiîjklmnopqrsștțuvwxyz")
N = len(ALPHABET)

# Every accepted character mapped to its uppercase letter. The cedilla forms
# Ş/ş and Ţ/ţ are treated as the comma-below letters Ș and Ț.
TO_UPPER = {}
for upper, lower in zip(ALPHABET, LOWER):
    TO_UPPER[upper] = upper
    TO_UPPER[lower] = upper
TO_UPPER.update({"Ş": "Ș", "ş": "Ș", "Ţ": "Ț", "ţ": "Ț"})

ALLOWED_LETTERS = "A-Z, a-z, Ă ă, Â â, Î î, Ș ș, Ț ț"

def permuted_alphabet(keyword):
    """Keyword letters first (each once), then the rest in natural order."""
    order = []
    for letter in keyword + "".join(ALPHABET):
        if letter not in order:
            order.append(letter)
    return order