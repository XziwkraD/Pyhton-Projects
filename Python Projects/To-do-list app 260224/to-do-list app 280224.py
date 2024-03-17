list = []

from to_do_list_classes_290224 import Task, ToDoList

todolist = ToDoList()

while True:

    print("1. Add task (e.g 01, 02...)")
    print("2. Edit task")
    print("3. Remove task")
    print("4. Mark task's completion")
    print("5. View Tasks")
    print("6. Exit")

    choice = input("Enter your choice(1-6): ")
    while not choice.isnumeric():
            print("The choice is invalid. please re-enter a number!")
            choice = input("Enter your choice(1-6): ")

    if choice == "1":
        todolist.add_task()

    if choice == "2":
        todolist.edit_task()

    if choice == "3":
        todolist.remove_task()

    if choice == "4":
         todolist.completion()
    
    if choice == "5":
         todolist.view_tasks()

    if choice == "6":
         print("Cya! :)")
         break



# add double digit task_num
# Auto assign task_num