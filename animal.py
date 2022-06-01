import sys

def default():
    print("hello")

def cat():
    print("Meow")

def main():
    if sys.argv[1] == 'cat':
        cat()
    else:
        default()

if __name__ == '__main__':
    main()
