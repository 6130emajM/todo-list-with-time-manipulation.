class ToDoList:
    def __init__(self):
        self.tasks = []
        self.deleted_tasks = []
        self.paused = False

    def add_task(self, task):
        if not self.paused:
            self.tasks.append(task)
            print(f"Task '{task}' added.")
        else:
            print("Time is paused. Cannot add tasks.")

    def view_tasks(self):
        if not self.paused:
            if self.tasks:
                print("Tasks:")
                for idx, task in enumerate(self.tasks, 1):
                    print(f"{idx}. {task}")
            else:
                print("No tasks in the list.")
        else:
            print("Time is paused. Cannot view tasks.")

    def delete_task(self, task_number):
        if not self.paused:
            if 0 < task_number <= len(self.tasks):
                task = self.tasks.pop(task_number - 1)
                self.deleted_tasks.append(task)
                print(f"Task '{task}' deleted.")
            else:
                print("Invalid task number.")
        else:
            print("Time is paused. Cannot delete tasks.")

    def rewind_time(self):
        if self.deleted_tasks:
            task = self.deleted_tasks.pop()
            self.tasks.append(task)
            print(f"Task '{task}' restored.")
        else:
            print("No tasks to restore.")

    def pause_time(self):
        self.paused = not self.paused
        state = "paused" if self.paused else "resumed"
        print(f"Time is now {state}.")

    def fast_forward_time(self):
        if not self.paused:
            if self.tasks:
                print(f"Next task: {self.tasks[0]}")
            else:
                print("No tasks in the list.")
        else:
            print("Time is paused. Cannot view tasks.")

def main():
    todo_list = ToDoList()
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Rewind Time")
        print("5. Pause Time")
        print("6. Fast Forward Time")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            try:
                task_number = int(input("Enter task number to delete: "))
                todo_list.delete_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            todo_list.rewind_time()
        elif choice == '5':
            todo_list.pause_time()
        elif choice == '6':
            todo_list.fast_forward_time()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()