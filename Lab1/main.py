from alphabet import ALPHABET, N, permuted_alphabet
from cipher import decrypt, encrypt
from validation import InputError, parse_key, prepare_keyword, prepare_text

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

def run_task(two_keys):
    operation = ask_choice("Operation - (e)ncrypt or (d)ecrypt: ", ["e", "d"])
    label = "Key 1" if two_keys else "Key"
    key = ask(f"{label} (integer 1-{N - 1}): ", parse_key)

    alphabet = ALPHABET
    if two_keys:
        keyword = ask("Key 2 (keyword, at least 7 Romanian letters): ",
                      prepare_keyword)
        alphabet = permuted_alphabet(keyword)
        print(f"Keyword:           {keyword}")
        print(f"Original alphabet: {''.join(ALPHABET)}")
        print(f"Permuted alphabet: {''.join(alphabet)}")

    if operation == "e":
        text = ask("Message: ", prepare_text)
        print(f"Prepared message:  {text}")
        print(f"Ciphertext:        {encrypt(text, key, alphabet)}")
    else:
        text = ask("Ciphertext: ", prepare_text)
        print(f"Prepared text:     {text}")
        print(f"Decrypted message: {decrypt(text, key, alphabet)}")

def main():
    print("=== Caesar cipher - Romanian alphabet (n = 31) ===")
    while True:
        print()
        print("1. Caesar cipher (Task 1.1)")
        print("2. Caesar cipher with a keyword permutation (Task 1.2)")
        print("0. Exit")
        choice = ask_choice("Choose: ", ["1", "2", "0"])
        if choice == "0":
            print("Bye!")
            break
        run_task(two_keys=(choice == "2"))


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
