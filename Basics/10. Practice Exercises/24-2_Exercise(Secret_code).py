# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code langugae

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end 
# now append three random characters at the starting and the end
# else:
# simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
# remove 3 random characters from start and end. Now remove the last letter and append it to the beignning 

'''
usr = input("Enter Your Message: ")
words = usr.split(" ")
coding = input("Enter '1' for ENCODE or '0' for DECODE: ")
coding = True if coding == '1' else False
if (coding):
    new_word = []
    for word in words:
        if (len(word) >= 3):
            random1 = 'abc'
            random2 = 'xyz'
            encode = random1 + word[1:] + word[0] + random2
            new_word.append(encode)
        else:
            new_word.append(word[::-1])
    print("Encoded Message: "," ".join(new_word))

else:
    new_word = []
    for word in words:
        if (len(word)):
            word = word[3:-3]
            encode = word[-1] + word[:-1]
            new_word.append(encode)
        else:
            new_word.append(word[::-1])
    print("Decoded Message: "," ".join(new_word))

'''


#==>> 'Random' values:

import random
import string

# Function to generate random 3-character strings for prefix and suffix
def generate_random_string(length=3):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Take user input for the original message
original_message = input("Enter the message: ")

# Ask the user whether they want to encode or decode
choice = input("Enter '1' to encode or '2' to decode the message: ")

if choice == '1':
    # Encoding the message
    words = original_message.split()
    encoded_words = []

    for word in words:
        if len(word) >= 3:
            # Generate random 3-character strings for prefix and suffix
            random_prefix = generate_random_string()
            random_suffix = generate_random_string()

            # Move the first letter to the end
            encoded_word = random_prefix + word[1:] + word[0] + random_suffix
            encoded_words.append(encoded_word)
        else:
            # Reverse the string for words with less than 3 characters
            encoded_words.append(word[::-1])

    # Join the encoded words into a string
    encoded_message = ' '.join(encoded_words)
    print("Encoded Message:", encoded_message)

elif choice == '2':
    # Decoding the message
    words = original_message.split()
    decoded_words = []

    for word in words:
        if len(word) >= 3:  
            # Remove the 3 random characters from the beginning and end
            word = word[3:-3]
            # Move the last letter to the front
            decoded_word = word[-1] + word[:-1]
            decoded_words.append(decoded_word)
        else:
            # Reverse the string for words with less than 3 characters
            decoded_words.append(word[::-1])

    # Join the decoded words into a string
    decoded_message = ' '.join(decoded_words)
    print("Decoded Message:", decoded_message)

else:
    print("Invalid choice. Please enter '1' to encode or '2' to decode.")
