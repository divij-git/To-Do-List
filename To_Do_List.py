#The display menu function will print out the options the user can interact with
def display_menu():
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Tasks")
    print("4. Delete Tasks") 
    print("5. Exit") 
#Create a class of nodes that will be our tasks
class TaskNode:
    def __init__(self,task=None):
        self.task = task
        self.next = None
#Create a linked list for tasks
class TaskList:
    def __init__(self):
        self.head = None
#Append function to add tasks to task list
    def append(self):
        task = input("Add your task here: ")
        new_task = TaskNode(task)
        if self.head is None:
            self.head = new_task
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_task
        print("Task added successfully")
#Length function will let me know how many items in the list
    def num_of_tasks(self):
        cur = self.head
        total = 0
        while cur is not None:
            total += 1
            cur = cur.next
        return total
#display function to display all tasks in list
    def view_tasks(self):
        elems = []
        cur_node = self.head
        while cur_node != None:
            elems.append(cur_node.task)
            cur_node = cur_node.next
        if not elems:
            print("Looks like you're done for the day!")
        else:
            print("\nToday you have these tasks: ")
            for n, TASK in enumerate(elems, 1):
                print(f"{n}. {TASK}")
#Erase Function to delete a task at a certain index
    def erase(self, index):
        if index >= self.num_of_tasks():
            print("Error: 'Erase' Index out of range!")
            return
        if index == 0:
            self.head = self.head.next
            return
        cur = self.head
        cur_idx = 0
        while cur is not None and cur.next is not None:
            if cur_idx == index - 1:  # Stop one before the target
                cur.next = cur.next.next
                return
            cur = cur.next
            cur_idx += 1
#Delete Function to delete task with erase
    def delete_task(self):
        if self.head is None:
            print("No tasks to delete for now.")
            return

        print("\nPick a task to delete:")
        cur = self.head
        idx = 1
        while cur:
            print(f"{idx}. {cur.task}")
            cur = cur.next
            idx += 1

        try:
            choice = int(input("Enter the number of the task you would like to delete: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        total_tasks = self.num_of_tasks()
        if 1 <= choice <= total_tasks:
            self.erase(choice - 1)   
            print("Task deleted successfully.")
        else:
            print("Invalid task number. Try again.")

#Now a function to edit tasks
    def edit_task(self):
        if self.head is None:
            print("No tasks to edit right now.")
            return
        print("\nPick a task to edit: ")
        cur = self.head
        idx = 1
        while cur:
            print(f"{idx}. {cur.task}")
            cur = cur.next
            idx += 1
        try:
            choice = int(input("Enter the number of the task you would like to edit: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        total_tasks = self.num_of_tasks()
        if 1 <= choice <= total_tasks:
            cur = self.head
            for i in range(choice - 1):
                cur = cur.next
            Edited_Task = input("Write your new task here: ")
            cur.task = Edited_Task
            print("Task has been updated")
        else:
            print("Invalid Task Number. Try Again")



#Main Code Logic
my_list = TaskList()
while True:
    display_menu()
    User_Choice = input("What would you like to do? ")
    if User_Choice == '1':
        my_list.append()
    elif User_Choice == '2':
        my_list.view_tasks()
    elif User_Choice == '3':
        my_list.edit_task()
    elif User_Choice == '4':
        my_list.delete_task()
    elif User_Choice == '5':
        print("Thank you, have a nice day.")
        break
    else:
        print("Seems like you have picked an invalid choice. Please enter one of the options 1-5.")
