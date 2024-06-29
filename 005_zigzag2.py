import time, sys

# how many space to indent
indent = 0 
fac = 1

# Whether indent is increasing or not
indentIncreasing = True 
# mulfactor = 11

try:
    while True: # while main prog is runnig

        if indentIncreasing:
            print(' ' * (indent*indent), end ='')
            print("***********")
            time.sleep(0.1) # pause for 0.1 of a second

            # increase the number of spaces
            indent += 1
            if indent == 10:
                # change direction:
                indentIncreasing = False
        else:
            print(' ' * ((indent*indent) - (1- (fac*fac))),  end ='')
            print("***********")
            time.sleep(0.1) # pause for 0.1 of a second

            # Decrease the number of spaces:
            indent -= 1
            fac += 1
            
            if indent == 0:
                # change direction:
                indentIncreasing = True
                fac = 1


except KeyboardInterrupt: # When user press CTRL + C
    sys.exit()