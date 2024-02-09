class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = "[X]" if task["completed"] else "[ ]"
            print(f"{index}. {status} {task['task']}")

    def mark_task_completed(self, task_index):
        self.tasks[task_index]["completed"] = True

    def remove_task(self, task_index):
        del self.tasks[task_index]

if __name__ == "__main__":
    todo_list = TodoList()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.mark_task_completed(task_index)
        elif choice == "4":
            task_index = int(input("Enter task index to remove: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

