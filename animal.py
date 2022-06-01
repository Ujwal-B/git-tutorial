import sys

def dog():
    print("Woof")

def monkey():
    print("keekaw")

def default():
    print("hello")

def cat():
    print("Meow")

def main():
    if sys.argv[1] == 'cat':
        cat()
    elif sys.argv[1] == 'dog':
        dog()
    elif sys.argv[1] == "monkey":
        monkey()
    else:
        default()

if __name__ == '__main__':
    main()
