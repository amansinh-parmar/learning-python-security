def welcome():
    usr = input("Enter your name: ")
    print(f"Hello {usr}, Welcome to import module.")

# print(__name__)
if __name__ == "__main__":                # Using __name__ = "__main__" to only executated that particular function. 
    welcome()