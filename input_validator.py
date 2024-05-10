def choice_validator(start, end, menu):
    while True:
        print(menu)
        try:
            choice=int(input("Enter choice: "))
            if start<=choice<=end:
                return choice
            else:
                print("\nERROR: Wrong choice")
        except:
            print("\nERROR: Wrong choice")

def string_validator(input_string):
    while True:
        s=input(input_string)
        if s.trim()=="":
            print("\nERROR: this field cannot be empty")
        return s


def int_validator(input_string):
    while True:
        try:
            s=int(input(input_string))
            return s
        except:
            print("\nERROR: invalid integer")

def id_retry(input_string):
    while True:
        s=input(input_string)
        if s=="y" or s=="Y":
            return 1
        if s=="n" or s=="N":
            return 0
        else:
            print("ERROR: Wrong choice")