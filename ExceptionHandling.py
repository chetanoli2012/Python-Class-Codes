def to_int():
    while True:
        x = input()

        try:
            x = int(x)
            return x

        except ValueError:
            print("Error!")
to_int()
