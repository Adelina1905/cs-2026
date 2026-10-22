from alphabet import ALLOWED_LETTERS, TO_UPPER

import unicodedata


class InputError(ValueError):
    """Raised when a key or text does not respect the rules."""


def prepare_text(raw):
    """Check the characters, remove the spaces and convert to uppercase."""
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


def prepare_key(raw):
    """The key: only Romanian letters, at least 7, converted to uppercase."""
    raw = unicodedata.normalize("NFC", raw.strip())
    result = []
    for position, ch in enumerate(raw, start=1):
        if ch not in TO_UPPER:
            shown = "space" if ch == " " else f"'{ch}'"
            raise InputError(
                f"Invalid character {shown} at position {position}.\n"
                f"The key may contain only Romanian letters "
                f"({ALLOWED_LETTERS}).")
        result.append(TO_UPPER[ch])
    if len(result) < 7:
        raise InputError(f"The key has {len(result)} letters. "
                         f"It must have at least 7 letters.")
    return "".join(result)
