def main():
    height = get__height()
    for i in range(height):
        print("#" * (i + 1))

def get__height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0:
                return n
        except ValueError:
            print("Retry")



main()