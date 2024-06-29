import random, sys

def get_magic_answer(ans_num):

        # quit magic
        if ans_num == 999:
             sys.exit()
        elif ans_num > 5:
             print("type no 1 to 5 or 999 to exit")
        while True:
            if ans_num == 1:
                return "You will be the first and not last"
            elif ans_num == 2:
                return " Second born will be the first"
            elif ans_num == 3:
                return " Go and sin no more "
            elif ans_num == 4:
                return " You are the solution to your problem"
            elif ans_num == 5:
                return " You have a skeleton in your cupboard"
                


# user_num = int(input("What your lucky no (1 - 5) or 999 to exit?"))
# print(get_magic_answer(user_num))