import os

class TodoAppCLI:
    def __init__(self, filename="todo.txt"):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        """
        Loads tasks from the file or creates the file if it doesn't exist.
        """
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                pass  # Create the file
        with open(self.filename, "r") as file:
            self.tasks = [line.strip() for line in file.readlines()]

    def save_tasks(self):
        """
        Saves the current tasks to the file.
        """
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def list_tasks(self):
        """
        Displays all tasks with their statuses.
        """
        if not self.tasks:
            print("\nYour to-do list is empty.")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                status = "✔ Done" if task.startswith("[X] ") else "⏳ Pending"
                print(f"{i}. {task} ({status})")

    def add_task(self):
        """
        Adds a new task to the list.
        """
        task = input("\nEnter the task you want to add: ").strip()
        if task:
            self.tasks.append(task)
            self.save_tasks()
            print("Task added successfully.")
        else:
            print("Task cannot be empty.")

    def edit_task(self):
        """
        Edits an existing task.
        """
        self.list_tasks()
        try:
            task_number = int(input("\nEnter the task number you want to edit: "))
            if 1 <= task_number <= len(self.tasks):
                new_task = input("Enter the new task description: ").strip()
                if new_task:
                    self.tasks[task_number - 1] = new_task
                    self.save_tasks()
                    print("Task updated successfully.")
                else:
                    print("Task cannot be empty.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def delete_task(self):
        """
        Deletes a task from the list.
        """
        self.list_tasks()
        try:
            task_number = int(input("\nEnter the task number you want to delete: "))
            if 1 <= task_number <= len(self.tasks):
                deleted_task = self.tasks.pop(task_number - 1)
                self.save_tasks()
                print(f"Task '{deleted_task}' deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def mark_task_done(self):
        """
        Marks a task as done.
        """
        self.list_tasks()
        try:
            task_number = int(input("\nEnter the task number you want to mark as done: "))
            if 1 <= task_number <= len(self.tasks):
                task = self.tasks[task_number - 1]
                if not task.startswith("[X] "):
                    self.tasks[task_number - 1] = f"[X] {task}"
                    self.save_tasks()
                    print("Task marked as done.")
                else:
                    print("Task is already marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def clear_tasks(self):
        """
        Clears all tasks from the list.
        """
        confirm = input("Are you sure you want to clear all tasks? (yes/no): ").strip().lower()
        if confirm == "yes":
            self.tasks = []
            self.save_tasks()
            print("All tasks cleared.")
        else:
            print("Operation canceled.")

    def menu(self):
        """
        Displays the menu and handles user input.
        """
        while True:
            print("\n--- To-Do List Manager ---")
            print("1. View Tasks")
            print("2. Add Task")
            print("3. Edit Task")
            print("4. Delete Task")
            print("5. Mark Task as Done")
            print("6. Clear All Tasks")
            print("7. Exit")
            try:
                choice = int(input("Choose an option: "))
                if choice == 1:
                    self.list_tasks()
                elif choice == 2:
                    self.add_task()
                elif choice == 3:
                    self.edit_task()
                elif choice == 4:
                    self.delete_task()
                elif choice == 5:
                    self.mark_task_done()
                elif choice == 6:
                    self.clear_tasks()
                elif choice == 7:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    app = TodoAppCLI()
    app.menu()
