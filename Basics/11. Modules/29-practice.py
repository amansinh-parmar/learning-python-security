#--> Writ a function which generates a six digit/character random_user_id
#-> Practice Task: 1
#   print(random_user_id());
#   '1ee33d'


import random
import string

def random_usr_id():
    print("Your random six digit password:") 
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

print(random_usr_id())