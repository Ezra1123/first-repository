# import random

# word1 = input("please enter first word : ")
# word2 = input("please enter second word : ")

# password_length = int(input("How many chars of pass do you want (1-10) : "))

# full_word = word1 + word2
# password = ""
# print(full_word)

# for i in range(pass_length):

#     random_choice = random.randint(0, len(full_word)-1)

#     # print(full_word[random_choice])

#     password = password + full_word[random_choice]

# print(f"Here's yournnew {pass_length} char key : ",password)




import random

word1 = input("please enter first word : ")
word2 = input("please enter second word : ")

password_length = int(input("How many chars of pass do you want (1-10) : "))

full_word = word1 + word2
password = ""

for i in range(pass_length):

    while True:
        random_choice = random.randint(0, len(full_word)-1)

        if full_word[random_choice] not in password:
            break


    # print(full_word[random_choice])

    password = password + full_word[random_choice]

print(f"Here's yournnew {pass_length} char key : ",password)
