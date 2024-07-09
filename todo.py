# Simple ToDo List Commandline App
# Written following https://www.youtube.com/watch?v=aEIHZDv_23U
# A quick and dirty ToDo app we can expand upon later
tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"The task '{task}' was added successfully.")

def showTasks():
    if not tasks:
        print("There are currently no tasks. \n")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}: {task}")

def deleteTask():
    showTasks()
    try:
        taskToDelete = int(input("Please enter the index of the task to delete: "))
        if index >= 0 and index < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task #{taskToDelete} was successfully removed.")
        else:
            print(f"Task #{taskToDelete} could not be found.")
    except:
        print("Invalid input")

if __name__ == "__main__":
    print("Welcome to the to do list")
    while True:
        print("\n")
        print("Please select an option:")
        print("------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if(choice == "1"):
            addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            showTasks
        elif(choice == "4"):
            break
        else:
            print("Choice is invalid. Please try again.")

    print("Goodbye. Thanks for using the app.")
