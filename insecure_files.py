import os

def read_file():
    filename = input('Enter the filename to read: ')
    # No validation — attacker can type  ../../etc/passwd
    with open(filename, 'r') as file:
        print(file.read())

def delete_file():
    filename = input('Enter filename to delete: ')
    # No check — can delete any file on the system
    os.remove(filename)
    print(f'{filename} deleted!')

def execute_command():
    command = input('Enter shell command: ')
    # Allows ANY command — rm -rf, cat /etc/shadow, etc.
    os.system(command)

choice = input('1) Read  2) Delete  3) Execute: ')
if   choice == '1': read_file()
elif choice == '2': delete_file()
elif choice == '3': execute_command()
