import random
import string

def generate_password(length, complexity):
    chars = string.ascii_letters
    if complexity == 'medium':
        chars += string.digits
    elif complexity == 'high':
        chars += string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    length = int(input('Enter password length: '))
    complexity = input('Enter password complexity (low/medium/high): ')
    password = generate_password(length, complexity)
    print('Your new password is:', password)

if __name__ == '__main__':
    main()
