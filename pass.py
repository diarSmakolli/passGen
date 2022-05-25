import random


chars = "abdefghijklmmmopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVXYYZ123456!$%&#`)"

while 1:
    password_len = int(input("Sheno gjatesine e passwordit: "))
    password_count = int(input("Sa passwords deshironi: "))
    for n in range(0, password_count):
        password = ""
        for n in range(0, password_len):
            password_char = random.choice(chars)
            password  = password + password_char
        print("Here is your password: ", password)
        exit()
