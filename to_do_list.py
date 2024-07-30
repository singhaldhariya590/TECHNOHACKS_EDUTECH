import pickle
import os

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = "completed" if self.completed else "pending"
        return f"[{status}] {self.description}"

class To_do_list_manager:
    def __init__(self, filename='todo_list.pkl'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, description):
        self.tasks.append(Task(description))
        self.save_tasks()

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

    def mark_task_completed(self, index):
        try:
            self.tasks[index - 1].completed = True
            self.save_tasks()
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, index):
        try:
            del self.tasks[index - 1]
            self.save_tasks()
        except IndexError:
            print("Invalid task number.")

    def save_tasks(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.tasks, file)

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        return []

def print_menu():
    print("\nTo-Do List Manager")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit\n")

def main():
    manager = To_do_list_manager()

    while True:
        print_menu()
        choice = input("\nChoose an option: ")

        if choice == '1':
            description = input("\nEnter task description: ")
            manager.add_task(description)
        elif choice == '2':
            manager.list_tasks()
        elif choice == '3':
            try:
                index = int(input("\nEnter task number to mark as completed: "))
                manager.mark_task_completed(index)
            except ValueError:
                print("\nPlease enter a valid number.")
        elif choice == '4':
            try:
                index = int(input("\nEnter task number to delete: "))
                manager.delete_task(index)
            except ValueError:
                print("\nPlease enter a valid number.")
        elif choice == '5':
            print("\nExiting...Goodbye!! ")
            break
        else:
            print("\nInvalid choice, please select a number from the menu.")

if __name__ == "__main__":
    main()
