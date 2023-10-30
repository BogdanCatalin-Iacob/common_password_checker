'''
Check the most common password in 100k passwords
'''


def check_password(password: str):
    '''
    Check the user password against the passwords list
    '''
    with open('passwords.txt', 'r', encoding='utf-8') as file:
        common_paswords: list[str] = file.read().splitlines()

    for i, common_pasword in enumerate(common_paswords, start=1):
        if password == common_pasword:
            print(f'{password} is a common password: (#{i})')
            return

    print(f'{password} is Unique!')


def main():
    '''
    Accepts user password input
    '''
    user_input: str = input('Enter your desired password: ')
    check_password(user_input)


if __name__ == '__main__':
    main()
