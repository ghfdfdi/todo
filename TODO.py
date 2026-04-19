from random import choice

tasks =[]
#пустой список
while True:
    print("\nTODO СПИСОК")
    print(" 1. показать задачи")
    print("2. добавить задачу")
    print("3. удалить задачу")
    print("4. выйти")
    #цикл благодоря которому программа не закроется после одного действия и список для выбора действий

    choice = input('выбери действие')
    if choice == '1':
        if not tasks:
            print("список задач пуст")
        else:
            print("\nВыши задачи ")
            for i, task in enumerate(tasks, start=1):
                print(i, task)
    #если задачи не были введены покажет первый принт, 19 строка for это цикл for i in tasks enumerate нумерует и выполняет действие для каждой задачи в списке tasks
    elif choice == "2":
        task = input("введите задачу ")
        if task == "":
            print("ошика пустая задача")
        else:
            tasks.append(task)
            print("задача добавленна")
            #.append это фуункция списка которая означает добавить в конец
    elif choice == "3":
        if not tasks:
            print("список пуст")
        else:
            print("\nваши задачи")
            for i, task in enumerate(tasks, start=1):
                print(i, task)
            num = int(input("введите задачи для удаления"))
            if 0 < num <= len(tasks):
                tasks.pop(num - 1)
                print("задача удалена")
            else:
                print("неверный номер")
            #38 строка= если число больще нуля и не больше длины списка то len = кол во задач в списка, .pop= удаление
    elif choice == "4":
        print("пока")
        break
    else:
        print("неверный выбор")
        #task=1 tasks=несколько НЕ ПУТАТЬ










