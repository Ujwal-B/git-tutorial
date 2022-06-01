import sys

def donkey():
    print("*Insert Donkey Sounds*")

def default():
    print("hello")

def main():
    if sys.argv[1] == 'donkey':
        donkey()
    else:
        default()

if __name__ == '__main__':
    main()
