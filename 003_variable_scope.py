

def fun1():
    global val_in_fun1
    val_in_fun1 = "fun1() value"
    fun2()

def fun2():
    print ("val  ",val_in_fun1)

fun1()
print("Global val = ", val_in_fun1)
