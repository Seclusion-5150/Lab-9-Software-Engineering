def encode(password):
    encoded_password = ''.join(str((int(char) + 3) % 10) for char in password)
    return encoded_password

def decode(password):
    decoded_password = ''.join(str((int(char) - 3) % 10) for char in password)
    return decoded_password
    
def main():
    encoded_password = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif option == "2":
            if encoded_password :
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            else:
                print("No encoded password stored. Please encode a password first.")

        elif option == "3":

            break

if __name__ == '__main__':
    main()
