tasks = []
while True:
    print("---TODO СПИСОК---")
    print("1. покказать задачи")
    print("2. добавить задачу")
    print("3. удалить задачу")
    print("4. выйти")
    choice = input("выбери действие")
    if choice == "1":
        if not tasks:
            print("список задач пуст")
        else:
            print("ваши задачи :")
            for i, task in enumerate(tasks, start=1):
                print(i, task)
    if choice =="2":
