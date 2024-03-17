class Task:
    def __init__(self, task_num, description, due_date, priority, completed): #blueprint for creating task objects
        self.task_num = task_num
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed
        self.new_task = [task_num, description, due_date, priority, self.completed]

    def display(self):
        print(self.task_num)
        print(self.description)
        print(self.due_date)
        print(self.priority)

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        num = input("Enter the task number: ")
        while not num.isnumeric():
            print("The task number entered is invalid. please re-enter a number!")
            num = input("Enter the task number: ")
        description = input("Enter task description: ")
        due_date = input("Enter task due date: ")
        priority = input("Enter task priority(high/medium/low): ").lower()
        completed = False
        my_task = Task(num, description, due_date, priority, completed)
        self.tasks.append(my_task)
        Task.display(my_task)
        print("Your task has been added!")

    def remove_task(self):
        while True:
            remove_num = input("Enter the task number: ")
            while not remove_num.isnumeric():
                print("The task number entered is invalid. please re-enter a number!")
                remove_num = input("Enter the task number: ")
            remove_num = int(remove_num)# Convert the task number to an integer
            found_task = None
            for item in self.tasks: 
                if remove_num == int(item.task_num):
                    found_task = item
                    break

            if found_task is not None: # Check if the task with the specified number exists
                self.tasks.remove(item)
                print("Task successfully removed :)")
                break

            else:
                print("Task not found :(")
                redo = input("Would you like to try again? (yes/no): ").lower()
                if redo != "yes":
                    break

    def edit_task(self):
        while True:
            edit_num = input("Enter the task number: ")
            while not edit_num.isnumeric():
                print("The task number entered is invalid. please re-enter a number!")
                edit_num = input("Enter the task number: ")
            edit_num = int(edit_num)# Convert the task number to an integer
            found_task = None
            for item in self.tasks:
                if edit_num == int(item.task_num): 
                    found_task = item
                    break

            if found_task is not None: # Check if the task with the specified number exists
                print("Task details: ")
                print(f"Description: {found_task.description}")
                print(f"Due Date: {found_task.due_date}")
                print(f"Priority: {found_task.priority}")

                new_description = input("Enter new description (press enter to keep current): ")
                new_due_date = input("Enter new due date (press enter to keep current): ")
                new_priority = input("Enter new priority (press enter to keep current): ")

                if new_description:
                    found_task.description = new_description
                if new_due_date:
                    found_task.due_date = new_due_date
                if new_priority:
                    found_task.priority = new_priority

                print("Task updated successfully :)")
                print(self.view_tasks)
                break
        
            else:
                print("Task not found :(")
                redo = input("Would you like to try again? (yes/no): ").lower()
                if redo != "yes":
                    break

    def completion(self):
        while True:
            complete_num = input("Enter the task number: ")
            while not complete_num.isnumeric():
                print("The task number entered is invalid. please re-enter a number!")
                complete_num = input("Enter the task number: ")
            complete_num = int(complete_num)# Convert the task number to an integer
            found_task = None
            for item in self.tasks:
                if complete_num == int(item.task_num): 
                    found_task = item
                    break
            if found_task is not None:
                completedyesno = input("Have you completed the task (yes/no)? ").lower
                if completedyesno != "no":
                    removal = input("Would you like to remove the task (yes/no)? ")
                    if removal != "no":
                        self.tasks.remove(item)
                        print("Task successfuly removed:)")
                        break
            else:
                redo = input("Would you like to try again? (yes/no): ").lower()
                if redo != "yes":
                    break

    def priority(self):
        prior_dict = {'high': 1,
                      'medium': 2,
                      'low': 3}
        print(self.tasks.sorted(key= lambda x: prior_dict.get(x.priority, 0)))
        

    def view_tasks(self):
        prior_dict = {'high': 1,
                      'medium': 2,
                      'low': 3}
        self.tasks.sort(key= lambda x: prior_dict.get(x.priority, 0))
        if len(self.tasks) == 0:
            print("You do not currently have any tasks!")
        else:
            for index, elements in enumerate(self.tasks, start=1):
                print(f"{index}. {elements.description} \n- Due: {elements.due_date} \n- Priority: {elements.priority}")