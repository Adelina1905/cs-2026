from alphabet import ALLOWED_LETTERS, N, TO_UPPER

import unicodedata


class InputError(ValueError):
    """Raised when a key, keyword or text does not respect the rules."""


# ------------------------------------------------------------ validation
KEY_RULE = f"The key must be an integer from 1 to {N - 1}."

def parse_key(raw):
    """Key 1 must be an integer from 1 to N - 1 (1..30)."""
    raw = raw.strip()
    if not raw.lstrip("-").isdigit():
        raise InputError(f"'{raw}' is not an integer. {KEY_RULE}")
    key = int(raw)
    if not 1 <= key <= N - 1:
        raise InputError(f"{key} is out of range. {KEY_RULE}")
    return key


def prepare_text(raw):
    """Check the characters, convert to uppercase and remove the spaces."""
    raw = unicodedata.normalize("NFC", raw)
    result = []
    for position, ch in enumerate(raw, start=1):
        if ch == " ":
            continue
        if ch not in TO_UPPER:
            raise InputError(
                f"Invalid character '{ch}' at position {position}.\n"
                f"Only Romanian letters ({ALLOWED_LETTERS}) and spaces "
                f"are allowed.")
        result.append(TO_UPPER[ch])
    if not result:
        raise InputError("The text is empty. Enter at least one letter.")
    return "".join(result)


def prepare_keyword(raw):
    """Key 2: only Romanian letters, at least 7, converted to uppercase."""
    raw = unicodedata.normalize("NFC", raw.strip())
    result = []
    for position, ch in enumerate(raw, start=1):
        if ch not in TO_UPPER:
            shown = "space" if ch == " " else f"'{ch}'"
            raise InputError(
                f"Invalid character {shown} at position {position}.\n"
                f"The keyword may contain only Romanian letters "
                f"({ALLOWED_LETTERS}).")
        result.append(TO_UPPER[ch])
    if len(result) < 7:
        raise InputError(f"The keyword has {len(result)} letters. "
                         f"It must have at least 7 letters.")
    return "".join(result)


