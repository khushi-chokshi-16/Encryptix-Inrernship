
tasks= []
def AddTask():
    task = input("Enter the task:")
    tasks.append(task)
    print(f"Task {task} added.")

def listTasks():
    if not tasks:
        print("No tasks are available.")
    else:
        print("The tasks are:")
        for index,task in enumerate(tasks):
            print(f"Task #{index}.{task}")


def DeleteTask():
    listTasks()
    try:
        task_to_delete = int(input("Enter the # to delete:"))
        if task_to_delete >= 0 and task_to_delete < len(tasks):
            tasks.pop(task_to_delete)
            print(f"Task {task_to_delete} has been removed.")
        else:
            print(f"Task #{task_to_delete} was not found")
        
    except:
        print("Invalid input.")

if __name__ == "__main__":
    
    
    while(True):
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Show Tasks")
        print("4. Exit ")

        users_input = input("Enter your choice: ")

        if(users_input == "1"): 
            AddTask()
        elif(users_input == "2"):   
            DeleteTask()
        elif(users_input == "3"):
            listTasks()
        elif(users_input == "4"):
            break
        else:
            print("Invalid input.")
