
def display_tasks(tasks):
    print("\n=== Your To-Do List ===")

    if not tasks:
        print("No tasks added yet.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['name']} - {status}")


def main():
    tasks = []

    while True:
        print("\n=== To-Do List Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            name = input("Enter the task: ").strip()

            if name:
                tasks.append({
                    "name": name,
                    "completed": False
                })
                print("Task added successfully!")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            display_tasks(tasks)

            if tasks:
                try:
                    number = int(input("Enter the task number to complete: "))

                    if 1 <= number <= len(tasks):
                        tasks[number - 1]["completed"] = True
                        print("Task marked as completed!")
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid whole number.")

        elif choice == "4":
            display_tasks(tasks)

            if tasks:
                try:
                    number = int(input("Enter the task number to delete: "))

                    if 1 <= number <= len(tasks):
                        removed_task = tasks.pop(number - 1)
                        print("Deleted task:", removed_task["name"])
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid whole number.")

        elif choice == "5":
            print("Thank you for using the To-Do List Manager!")
            break

        else:
            print("Invalid choice. Please select from 1 to 5.")


if __name__ == "__main__":
    main()
