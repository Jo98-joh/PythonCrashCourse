from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open ('key.key', 'wb') as key_file:
#         key_file.write(key)

def load_key():
    file = open('key.key','rb')
    key = file.read()
    file.close()
    return key


Masterpwd = input('What is the master password? ')
key = load_key() +  Masterpwd.encode()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user , passw  = data.split('|')
            print( 'User: ', user, '| Password: ',str(fer.decrypt(passw.encode())))
            
def add():
    name = input('Account Name:  ')
    pwd = input('Password:  ')
    
    with open ('password.txt', 'a') as f:
        f.write(name + '|' + str(fer.encrypt(pwd.encode())) + '\n')

while True:
    mode = input ('Would you like to add a new password or view exiting one (view, add), press q to quit:   ').lower()
    if mode == 'q' :
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode.')
        continue