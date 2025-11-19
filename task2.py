from collections import deque


def is_palindrome(string: str):
    """
    Checks if the input string is a palindrome.
    Ignore spaces and is case-insensitive.
    """
    normalized = ''.join(c.casefold() for c in string if c.isalnum())

    char_deque = deque(normalized)

    # Check symbols in both ends
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True


test_strings = [
    "A man a plan a canal Panama",
    "racecar",
    "hello",
    "Was it a car or a cat I saw",
    "ротор",
    "привіт",
    "Я несу гусеня"
]

for s in test_strings:
    result = "is" if is_palindrome(s) else "is not"
    print(f'"{s}" {result} a palindrome.')
