while True:
    print("что вы хотите сделать?")
    print("1. ввести числро")
    print("0. выйти")
    try:
        num = int(input("введите номер"))
    except:
        print("это не число")
    if num == 1:
        try:
            nui = int(input("введите число"))
            print("ваше число:", nui)
        except:
            print("это не число")
    elif num == 0:
        break





