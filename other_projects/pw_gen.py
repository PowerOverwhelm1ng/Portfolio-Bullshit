import secrets
import string

def create_pass_word(pwd_length = 12):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars
    pwd = ""
    pwd_strong = False

    while not pwd_strong:
        pwd = ""
        for i in range(pwd_length):
            pwd += secrets.choice(alphabet)

        if any(char in special_chars for char in pwd) and sum(char.isdigit() for char in pwd)>=2:
            pwd_strong = True

    return pwd
if __name__ == '__main__':
    print(create_pass_word(12))

