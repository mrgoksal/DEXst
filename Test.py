import tkinter as tk
from tkinter import ttk

# Создание главного окна
root = tk.Tk()
root.title("Простая форма")
root.geometry("400x600")

# Создание холста с прокручиваемой областью
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Размещение холста и прокрутки в главном окне
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


# Поле ввода текста
ttk.Label(scrollable_frame, text="Введите текст:").grid(row=10, column=0, padx=10, pady=10, sticky='w')
text_entry = ttk.Entry(scrollable_frame)
text_entry.grid(row=20, column=1, padx=10, pady=10, sticky='ew')

# Поле с выбором
ttk.Label(scrollable_frame, text="Выберите опцию:").grid(row=21, column=0, padx=10, pady=10, sticky='w')
combo = ttk.Combobox(scrollable_frame, values=["Опция 1", "Опция 2", "Опция 3"])
combo.grid(row=21, column=1, padx=10, pady=10, sticky='ew')

# Кнопка
button = ttk.Button(scrollable_frame, text="Нажмите")
button.grid(row=22, column=0, columnspan=2, padx=10, pady=20, sticky='ew')

# Установка пропорционального расширения столбцов
scrollable_frame.columnconfigure(0, weight=1)
scrollable_frame.columnconfigure(1, weight=2)

# Запуск главного цикла
root.mainloop()
