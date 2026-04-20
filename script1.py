tasks = []
while True:
    print("---TODO СПИСОК---")
    print("1. покказать задачи")
    print("2. добавить задачу")
    print("3. удалить задачу")
    print("4. выйти")
    try:
        choice = int(input("выбери действие "))
    except:
        print("введите число")
        continue


    if choice == 1:
        if not tasks:
            print("список задач пуст")
        else:
            print("ваши задачи :")
            for i, task in enumerate(tasks, start=1):
                print(i, task)
    elif choice == 2:

        task = input("введите задачу: ")
        if task == "":
            print("задача пустая напиши что нибудь")
        else:
            tasks.append(task)
            print("задача добавленна")
    elif choice == 3 :
        if not tasks:
            print("задач нет")
        else:

            for i, task in enumerate(tasks, start=1):
                print(i, task)
                num = int(input("введите задачи для ужаления"))

                if 0 < num <= len(tasks):
                    tasks.pop(num - 1)
                    print("задача удалена")
    elif choice == 4:
        print("пока")
        break
    else:
        print("неверный номер")







