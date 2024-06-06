def drawBox(size):
    if size < 1:
        return None

    # Printing first line
    print(" " * (size + 1) + '+' + '-' * size * 2 + '+')

    # Printing upper face
    for i in range(0,size):
        print(" " * (size - i) + "/" + " " * size * 2 + "/" + " " * i + "|")
    # Printing middle line
    print("+" + "-" * size * 2 + "+" + " " * size + "+")

    # Printing front face
    for i in range(0, size):
        print("|" + " " * size * 2 + "|" + " " * (size - i - 1) + "/")

    # Printing last line
    print("+" + "-" * size * 2 + "+")

drawBox(5)
