import string
import getpass
def main():

    def check_pass_word_strength():
        password = getpass.getpass("Enter the password")
        strength = 0
        remarks = ''
        lower_count = upper_count = num_count = wspace_count = special_count = 0

        for char in list(password):
            if char in string.ascii_lowercase:
                lower_count += 1

            elif char in string.ascii_uppercase:
                upper_count += 1
            elif char in string.digits:
                num_count += 1
            elif char == ' ':
                wspace_count += 1
            else:
                special_count += 1

        if lower_count >= 1:
            strength += 1
        if upper_count >= 1:
            strength += 1
        if num_count >= 1:
            strength += 1
        if wspace_count >= 1:
            strength += 1
        if special_count >= 1:
            strength += 1
        
        if strength == 1:
            remarks = ('Bad Password, change asap')
        elif strength == 2:
            remarks = ('Weak Password, change asap')
        elif strength == 3:
            remarks = ('Password Middling, change please')
        elif strength == 4:
            remarks = ('Password Acceptable')
        elif strength == 5:
            remarks = ('Password is Strong')

        print('Your password has :-')
        print(f'{lower_count} lower case letters')
        print(f'{upper_count} upper case letters')
        print(f'{num_count} number of digits')
        print(f'{wspace_count} whitespace chars')
        print(f'{special_count} special chars')
        print(f'Password Score: {strength / 5}')
        print(f'Remarks: {remarks}')

    def check_pwd(another_pw = False):
        valid = False
        if another_pw:
            choice = input(
                "Test your Strength? password/'s (y/n)"
            )
        else:
            choice = input(
                "Test your Strength? password/'s (y/n)"
                )
            
        while not valid:
            if choice.lower() == 'y':
                return True
            elif choice.lower() == 'n':
                print('Exiting...')
                return False
            else:
                print('Invalid Input Try Again. \n')
            break

    if __name__ == '__main__':
        print('==== Wilkommen to Password Strength Check! ====')
        check_pw = check_pwd()
        while check_pw:
            check_pass_word_strength()
            check_pw = check_pwd(True)
main()