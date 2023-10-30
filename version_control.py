def menu():
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit")
    print()


def encode(user_encode):
    encoded_str = ""
    int_list = []
    for i in user_encode:
        int_list += i
    for item in int_list:
        a = int(item) + 3
        encoded_str += str(a)
    return encoded_str


def decode(encoded_str):  # this is the code written by Ajay Sommi
    decoded_str = ""
    int_list = []
    for i in encoded_str:
        int_list += i
    for item in int_list:
        a = int(item) - 3
        decoded_str += str(a)
    return decoded_str


if __name__ == "__main__":
    on = True
    while on:
        menu()
        user_option = int(input("Please enter an option: "))
        if user_option == 1:
            user_encode = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
            encoded_password = encode(user_encode)

        elif user_option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        elif user_option == 3:
            on = False
