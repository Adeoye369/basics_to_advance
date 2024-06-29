import time, sys

# how many space to indent
indent = 0 

# Whether indent is increasing or not
indentIncreasing = True 

try:
    while True: # while main prog is runnig
        print(' ' * indent, end ='')
        print("***********")
        time.sleep(0.1) # pause for 0.1 of a second

        if indentIncreasing:
            # increase the number of spaces
            indent += 1
            if indent == 10:
                # change direction:
                indentIncreasing = False
        else:
            # Decrease the number of spaces:
            indent -= 1
            if indent == 0:
                # change direction:
                indentIncreasing = True


except KeyboardInterrupt: # When user press CTRL + C
    sys.exit()