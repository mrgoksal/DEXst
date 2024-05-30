import tkinter as tk
from tkinter import messagebox


# Функция проверки авторизации
def authorize():
    username = entry_username.get()
    password = entry_password.get()

    if username == "Admin" and password == "Admin":
        messagebox.showinfo("Успех", "Вы успешно вошли в систему")
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")


# Создание главного окна
root = tk.Tk()
root.title("Форма авторизации")

# Метки и поля ввода
tk.Label(root, text="Логин").grid(row=0, column=0)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

tk.Label(root, text="Пароль").grid(row=1, column=0)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)

# Кнопка входа
login_button = tk.Button(root, text="Войти", command=authorize)
login_button.grid(row=2, columnspan=2)

# Запуск главного цикла
root.mainloop()
