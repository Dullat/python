import os

tasks = []

def clear_term():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except Exception as e:
        print("error: {e}")

def add_task(title, note, deadline):
    task_id = len(tasks) + 1
    task = {
            "id" : task_id,
            "title" : title,
            "note" : note,
            "deadline" : deadline
    }

    tasks.append(task)

def get_new_task_data():
    title = str(input("enter title:"))
    note = str(input("enter note:"))
    deadline = str(input("enter a deadline:"))
    add_task(title, note, deadline)

def delete_task():
    delete_id = int(input("Enter a task id to delete the task:"))
    if delete_id > len(tasks):
        input("Invalid id, press Enter to return back...")
        return

    for task in tasks:
        if task["id"] == delete_id:
            tasks.remove(task)
            print("Deleted successfully.....")
            break

def show_task():
    show_id = int(input("Enter a task id to show the task:"))
    if show_id > len(tasks):
        input("Invalid id, press Enter to return back...")
        return
    for task in tasks:
        if task["id"] == show_id:
            print("id:",task["id"], "\ntitle:", task["title"], "\nnote:", task["note"], "\ndeadline:", task["deadline"])
            input("Enter to go back...")

def list_title():
    clear_term()
    print("list of all the tasks by id / title:")
    for task in tasks:
        print(task["id"], ":", task["title"])
    operation = int(input("Enter operation value:\n## 1 to show ## 2 to delete ## 3 to Go back ##\n::"))
    if operation == 1:
        show_task()
    elif operation == 2:
        delete_task()
    elif operation == 3:
        return
    else:
        input("Invalid id, press Enter to return back...")
        return


def main():
    while True:
        
        clear_term()
        print(" 1 to add new task")
        print(" 2 to list all tasks")
        choice = int(input("enter your choice: "))

        if(choice == 1):
            get_new_task_data()
        if(choice == 2):
            list_title()


if __name__ == "__main__":
    main()
