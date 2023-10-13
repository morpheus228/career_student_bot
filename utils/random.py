import random
import string


def generate_str(length = 10) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))