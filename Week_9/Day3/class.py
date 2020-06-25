my_password = "monkey"
passwords_file = open(
    "/Users/user/Desktop/DevelopersInstitute/Week_9/Day3/12.txt", "r")
passwords_content = passwords_file.readlines()

passwords_content = passwords_file.readlines()
for pwd in passwords_content:
    pwd = pwd.strip()
    if pwd == my_password:
        print("Change your password!!!")


# '''txt = "Hello world I like python because it's the best language in the world and also it's a super beautiful snake I really love it, good bye"
# txt = str(txt.split())


# f = open("demofile2.txt", "a")
# f.write(txt)
# f.close()'''
# import os
# name = input("Give me the name of the file: ")
# f = open(f'{name}.txt', "a")
# while True:
#     txt = input("What do you want to write? ")
#     f.write(txt+'\n')
#     if txt == "stop":
#         break


# '''with open(filename + '.txt', 'a') as f:
#     while True:
#         f.write'''

# os.getcwd()
