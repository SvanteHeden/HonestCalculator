# write your code here

x = 0.0
y = 0.0
oper = ""
good_opers = "+, -, *, /"
memory = 0.0


def user_input():
    global x
    global y
    global oper

    print("Enter an equation")

    calc = input().split()

    x = calc[0]
    oper = calc[1]
    y = calc[2]


def check_xy():
    global x
    global y
    global memory

    if x == "M":
        x = memory
    if y == "M":
        y = memory

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
        return True
    else:
        return False


def check_oper():
    global oper
    global good_opers

    if oper in good_opers:
        return False
    else:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        return True


def check_user_input():
    while check_xy():
        user_input()
        while check_oper():
            user_input()


def computation():
    global oper
    global x
    global y

    x = float(x)
    y = float(y)

    if oper == "+":
        result = x + y
        return str(result)
    elif oper == "-":
        result = x - y
        return str(result)
    elif oper == "*":
        result = x * y
        return str(result)
    elif oper == "/" and y != 0:
        result = x / y
        return str(result)
    else:
        print("Yeah... division by zero. Smart move...")
        return 0


def retry_msg():
    global memory
    global result

    i = 0
    msg_list = ["Are you sure? It is only one digit! (y / n)",
                "Don't be silly! It's just one number! Add to the memory? (y / n)",
                "Last chance! Do you really want to embarrass yourself? (y / n)"]

    while i < 3:
        if i <= 2:
            print(msg_list[i])
            answer = input()

        if answer == "y":
                i += 1
        elif answer == "n":
            return False
        else:
            continue

    if i == 3:
        return True

def store_result():
    global result
    global memory

    while True:
        print("Do you want to store the result? (y / n):")

        answer = input()

        if answer == "y":
            if is_one_digit(result):
                if retry_msg():
                    memory = result
                else:
                    memory = result
            else:
                memory = result
            return True
        elif answer == "n":
            return False
        else:
            continue


def continue_calculations():
    while True:
        print("Do you want to continue calculations? (y / n):")

        answer = input()

        if answer == "y":
            return True
        if answer == "n":
            return False
        else:
            continue


def is_one_digit(v):
    if -10 < float(v) < 10 and float(v).is_integer():
        return True
    else:
        return False


def check_lazy():
    global x
    global y
    global oper

    msg = ""

    if x == "M":
        x = memory
    if y == "M":
        y = memory

    x = float(x)
    y = float(y)

    if is_one_digit(float(x)) and is_one_digit(float(y)):
        msg = msg + " ... lazy"
    if x == 1 or y == 1 and oper == "*":
        msg = msg + " ... very lazy"
    if (x == 0 or y == 0) and (oper == "*" or oper == "+" or oper == "-"):
        msg = msg + " ... very, very lazy"
    if msg != "":
        msg = "You are" + msg
        print(msg)


while True:
    # Checks the user input
    user_input()

    check_user_input()

    check_lazy()

    # Does the computation
    while not computation():
        check_user_input()
        user_input()
        check_lazy()
        check_user_input()

    result = computation()

    print(result)

    store_result()

    if continue_calculations():
        continue
    else:
        break
