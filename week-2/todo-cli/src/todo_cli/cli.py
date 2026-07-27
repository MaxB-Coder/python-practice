from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    done: bool = False
    priority: str = "medium"


@dataclass
class ToDoList:
    todos: list[Task] = field(default_factory=list)

    def add(self, title: str, priority: str = "medium") -> Task:
        task: Task = Task(title, priority=priority)
        self.todos.append(task)
        return task

    def all(self) -> None:
        if not self.todos:
            print("List is empty")
            return
        for i, task in enumerate(self.todos):
            print(
                "%s. [%s] %s (%s)"
                % ((i + 1), ("x" if task.done else " "), task.title, task.priority)
            )

    def complete(self, index: int) -> bool:
        if 1 <= index <= len(self.todos):
            task: Task = self.todos[index - 1]
            task.done = True
            return True
        return False

    def pending(self) -> list[Task]:
        return [task for task in self.todos if not task.done]


def main() -> None:
    todo_list = ToDoList()
    while True:
        raw = input("> ").strip()
        parts = raw.split(" ", 1)
        if parts[0] == "add":
            try:
                if not parts[1]:
                    print("Invalid command!")
                else:
                    task = todo_list.add(parts[1])
                    print(f"Added: {task.title}")
            except IndexError:
                print("Invalid command!")
        elif parts[0] == "all":
            todo_list.all()
        elif parts[0] == "complete":
            try:
                if parts[1].isdigit():
                    result = todo_list.complete(int(parts[1]))
                    if result:
                        print("Complete")
                    else:
                        print("Something went wrong!")
                else:
                    print("Invalid command!")
            except IndexError:
                print("Invalid command!")
        elif parts[0] == "quit":
            break
        else:
            print("Unknown command!")


if __name__ == "__main__":
    main()
