class MyTodoList():
    def __init__(self):
        # Initialize my_todos as an instance variable
        self.my_todos = []
        print("Your new todo list has been created!")

    def add_todo(self):
        todo = str(input('Enter your todo to add: '))
        self.my_todos.append(todo)
        print(f"'{todo}' has been added.")
    
    def view_todo(self):
        if not self.my_todos:
            print("Your todo list is empty.")
        else:
            print("\n--- Your Todo List ---")
            for index, todo in enumerate(self.my_todos):
                print(f"{index + 1}. {todo}")
            print("----------------------")
        return self.my_todos # Still return the list, useful for other operations
    
    def remove_todo(self):
        if not self.my_todos:
            print("No todos to remove. Your list is empty.")
            return

        self.view_todo() # Show the user what they can remove
        try:
            item_to_remove_input = input('Enter the todo you want to remove (or its number): ')
            
            # Try to remove by index first
            if item_to_remove_input.isdigit():
                index_to_remove = int(item_to_remove_input) - 1
                if 0 <= index_to_remove < len(self.my_todos):
                    removed_todo = self.my_todos.pop(index_to_remove)
                    print(f"'{removed_todo}' has been removed.")
                else:
                    print("Invalid number. Please enter a valid number from the list.")
            # If not a number, try to remove by exact string match
            elif item_to_remove_input in self.my_todos:
                self.my_todos.remove(item_to_remove_input)
                print(f"'{item_to_remove_input}' has been removed.")
            else:
                print(f"'{item_to_remove_input}' was not found in your todo list.")
        except ValueError:
            print("Invalid input. Please enter the exact todo or its number.")



def run_todo_app():
    my_list = MyTodoList() # Create one instance of your todo list

    while True:
        print("\n--- Todo List Menu ---")
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Remove Todo")
        print("4. Exit")
        print("----------------------")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            my_list.add_todo()
        elif choice == '2':
            my_list.view_todo()
        elif choice == '3':
            my_list.remove_todo()
        elif choice == '4':
            print("Exiting Todo List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

run_todo_app()