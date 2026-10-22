from alphabet import ALPHABET, CODE
from cipher import decrypt, encrypt
from validation import InputError, prepare_key, prepare_text

def ask(prompt, parser):
    """Ask again and again until the parser accepts the value."""
    while True:
        try:
            return parser(input(prompt))
        except InputError as error:
            print("  Error: " + str(error).replace("\n", "\n         "))

def ask_choice(prompt, choices):
    while True:
        value = input(prompt).strip().lower()
        if value in choices:
            return value
        print(f"  Error: choose one of: {', '.join(choices)}.")

def show_table(text, key, result):
    repeated = "".join(key[i % len(key)] for i in range(len(text)))
    print("Text:  " + " ".join(f"{letter:>2}" for letter in text))
    print("Key:   " + " ".join(f"{letter:>2}" for letter in repeated))
    print("       " + " ".join(f"{CODE[letter]:>2}" for letter in text))
    print("       " + " ".join(f"{CODE[letter]:>2}" for letter in repeated))
    print("       " + " ".join(f"{CODE[letter]:>2}" for letter in result))
    print("Out:   " + " ".join(f"{letter:>2}" for letter in result))

def run_task(operation):
    key = ask("Key (at least 7 Romanian letters): ", prepare_key)
    if operation == "e":
        text = ask("Message: ", prepare_text)
        result = encrypt(text, key)
        show_table(text, key, result)
        print(f"Prepared message:  {text}")
        print(f"Ciphertext:        {result}")
    else:
        text = ask("Ciphertext: ", prepare_text)
        result = decrypt(text, key)
        show_table(text, key, result)
        print(f"Prepared text:     {text}")
        print(f"Decrypted message: {result}")

def main():
    print("=== Vigenère cipher - Romanian alphabet (n = 31) ===")
    print("Alphabet: " + "".join(ALPHABET))
    while True:
        print()
        print("1. Encrypt")
        print("2. Decrypt")
        print("0. Exit")
        choice = ask_choice("Choose: ", ["1", "2", "0"])
        if choice == "0":
            print("Bye!")
            break
        run_task("e" if choice == "1" else "d")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
