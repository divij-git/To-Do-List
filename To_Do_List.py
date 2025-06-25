#The display menu function will print out the options the user can interact with
def display_menu():
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Tasks")
    print("4. Delete Tasks") 
    print("5. Exit") 

#Initialize a list for my list of tasks
tasks = ['Join meeting', 'Exercise', 'Email Professor', 'Read Textbook']
#This function will allow a user to add a task to the list
def add_task():
    task = input("Add your task here: ")
    tasks.append(task)
    print("Task added successfully")

#This function lets the users view their tasks. 
def view_tasks():
    if not tasks:
        print("Looks like youre done for the day")
    else:
        task_string = ", ".join(tasks)
        print(f"\nToday you have these tasks: {task_string}")

#This function will let users edit the tasks
def edit_tasks():
    if not tasks:
        print("No tasks to edit for now.")
        return
    print("\nPick a task to edit")
    for n, task in enumerate(tasks, 1):
        print(f"{n}. {task}")
    chosen_task = int(input("Enter the number of the task you would like to edit: "))
    if 1 <= chosen_task <= len(tasks):
        new_task = input("Write your new task here: ")
        tasks[chosen_task - 1] = new_task
        print("Task has been updated")
    else:
        print("Invalid task number. Try again")

#Finally this function will give the option to delete the chosen task
def delete_task():
    if not tasks:
        print("No tasks to delete for now.")
        return
    print("\nPick a task to delete")
    for n, task in enumerate(tasks, 1):
        print(f"{n}. {task}")
    task_chosen = int(input("Enter the number of the task you would like to delete: "))
    if 1 <= task_chosen <= len(tasks):
        del tasks[task_chosen - 1]
        print("Task Deleted Succesfully")
    else:
        print("Invalid task number. Try Again")

#My main code logic
while True:
    display_menu()
    choice = input("What would you like to do? ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        edit_tasks()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Thank you, have a nice day.")
        break
    else:
        print("Seems like you have picked an invalid choice. Please enter one of the options 1-5.")

    
