import tkinter as tk
from tkinter import ttk

class TaskTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Tracker")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=1, fill="both")

        self.frames = {}
        for category in ["Легкие задачи", "Средние задачи", "Тяжелые задачи"]:
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=category)
            self.frames[category] = frame

        self.tasks = {
            "Легкие задачи": [("Добыть 10 рубинов", "новая"), ("Зачистить 1 подземелье", "новая")],
            "Средние задачи": [("Добыть 30 рубинов", "новая"), ("Зачистить 2 подземелья", "новая")],
            "Тяжелые задачи": [("Добыть 100 рубинов", "новая"), ("Зачистить 3 подземелья", "новая")],
        }

        self.create_ui()
        self.start_timer()

    def create_ui(self):
        for category, frame in self.frames.items():
            for task, status in self.tasks[category]:
                self.create_task_ui(frame, category, task, status)

    def create_task_ui(self, parent, category, task, status):
        frame = ttk.Frame(parent)
        frame.pack(fill="x", padx=5, pady=5)

        task_label = tk.Label(frame, text=task)
        task_label.pack(side="left", padx=5)

        status_var = tk.StringVar(value=status)
        status_combobox = ttk.Combobox(frame, textvariable=status_var)
        status_combobox['values'] = ("новая", "в процессе", "завершена")
        status_combobox.pack(side="left", padx=5)

        update_button = tk.Button(frame, text="Обновить", command=lambda: self.update_status(category, task, status_var.get()))
        update_button.pack(side="left", padx=5)

    def update_status(self, category, task, new_status):
        for i, (t, status) in enumerate(self.tasks[category]):
            if t == task:
                self.tasks[category][i] = (t, new_status)
                print(f"Задача '{task}' в категории '{category}' обновлена до статуса '{new_status}'")
                break

    def reset_tasks(self):
        for category in self.tasks:
            for i, (task, _) in enumerate(self.tasks[category]):
                self.tasks[category][i] = (task, "новая")
        print("Все задачи сброшены до статуса 'новая'")
        self.refresh_ui()

    def refresh_ui(self):
        for category, frame in self.frames.items():
            for widget in frame.winfo_children():
                widget.destroy()
            for task, status in self.tasks[category]:
                self.create_task_ui(frame, category, task, status)

            def start_timer(self):
                self.reset_tasks()
                self.root.after(60000, self.start_timer)  # 60000 milliseconds = 1 minute

if __name__ == "__main__":
     root = tk.Tk()
     app = TaskTracker(root)
     root.mainloop()