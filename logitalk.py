from customtkinter import *

class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title("Logitalk")
        self.geometry("800x600")
        self.configure(fg_color="#1e1e1e")
        self.resizable(True, False)

        # Створення бокового меню
        self.menu_frame = CTkFrame(self, width=30, height=600, fg_color="#151515")
        self.menu_frame.pack_propagate(False)
        self.menu_frame.place(x=0, y=0)

        self.is_showMenu = False

        # Кнопка відкриття меню
        self.menu_btn = CTkButton(self, text="≡", font=('arial', 24),
                                  width=30, fg_color="#232323",
                                  command=self.toggle_menu)
        self.menu_btn.place(x=0, y=0)

        # Поле для чату
        self.chat_field = CTkScrollableFrame(self, width=740, height=480, fg_color="#202020")
        self.chat_field.place(x=40, y=50)

        # Поле для введення повідомлення
        self.message_entry = CTkEntry(self, placeholder_text='Введіть повідомлення...',
                                      height=40, width=680)
        self.message_entry.place(x=40, y=550)

        # Кнопка надсилання
        self.send_btn = CTkButton(self, text=">", width=50, height=40, command=self.send_message)
        self.send_btn.place(x=730, y=550)  # <-- було помилка: sent_btn

        # Для меню
        self.label = None
        self.entry = None

    # -------------------------------
    def toggle_menu(self):
        """Відкриття/закриття бокового меню"""
        if self.is_showMenu:
            # Закриваємо меню
            self.is_showMenu = False
            self.menu_btn.configure(text="≡", width=30)
            self.animate_menu(-5)
        else:
            # Відкриваємо меню
            self.is_showMenu = True
            self.menu_btn.configure(text="< MENU", width=200)
            self.animate_menu(5)

            # Створюємо контент у меню
            self.label = CTkLabel(self.menu_frame, text="Name",
                                  font=('arial', 24), text_color="#ABABAB")
            self.label.pack(pady=50)

            self.entry = CTkEntry(self.menu_frame, fg_color="#232323",
                                  placeholder_text="Enter text...")
            self.entry.pack(pady=10)

    # -------------------------------
    def animate_menu(self, step):
        """Анімація відкриття/закриття меню"""
        current_width = self.menu_frame.winfo_width()
        target_width = 200 if self.is_showMenu else 30

        if (step > 0 and current_width < target_width) or (step < 0 and current_width > target_width):
            self.menu_frame.configure(width=current_width + step)
            self.after(5, lambda: self.animate_menu(step))
        else:
            # Після закриття — прибираємо віджети
            if not self.is_showMenu:
                if self.label:
                    self.label.destroy()
                    self.label = None
                if self.entry:
                    self.entry.destroy()
                    self.entry = None

    # -------------------------------
    def send_message(self):
        """Надсилання повідомлення в чат"""
        text = self.message_entry.get().strip()
        if text:
            # Додаємо повідомлення у чат
            label = CTkLabel(self.chat_field, text=text, anchor="w", justify="left")
            label.pack(fill="x", padx=10, pady=5)
            self.message_entry.delete(0, 'end')


# -------------------------------
if __name__ == "__main__":
    logitalk = MainWindow()
    logitalk.mainloop()
