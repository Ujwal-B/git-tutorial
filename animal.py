import sys

def monkey():
    print("keekaw")

def default():
    print("hello")

def main():
    if sys.argv[1] == "monkey":
        monkey()
    else:
        default()

if __name__ == '__main__':
    main()
