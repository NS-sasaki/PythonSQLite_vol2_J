# tkinterをインポート
import tkinter as tk
from tkinter import messagebox
# CRUD操作関数をインポート
import crud_functions as crud

# CRUDアプリケーションクラスを定義
class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD App with SQLite")

        self.email_var = tk.StringVar()
        self.username_var = tk.StringVar()

        # ウィジェットを作成し配置
        self.create_widgets()

    def create_widgets(self):
        # Emailラベルとエントリを作成
        tk.Label(self.root, text="Email").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        tk.Entry(self.root, textvariable=self.email_var, width=25).grid(row=0, column=1, padx=10, pady=5)

        # Usernameラベルとエントリを作成
        tk.Label(self.root, text="Username").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        tk.Entry(self.root, textvariable=self.username_var, width=25).grid(row=1, column=1, padx=10, pady=5)

        # ボタンを作成し配置
        button_width = 20
        tk.Button(self.root, text="Create", command=self.create_record, width=button_width).grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W+tk.E)
        tk.Button(self.root, text="Read by Email", command=self.read_record_by_email, width=button_width).grid(row=3, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W+tk.E)
        tk.Button(self.root, text="Update", command=self.update_record, width=button_width).grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W+tk.E)
        tk.Button(self.root, text="Delete", command=self.delete_record, width=button_width).grid(row=5, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W+tk.E)

    # レコード作成メソッド
    def create_record(self):
        email = self.email_var.get()
        username = self.username_var.get()
        if email and username:
            success = crud.create_record(email, username)
            if success:
                messagebox.showinfo("Success", "Record created successfully")
            else:
                messagebox.showerror("Error", "Email already exists")
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    # レコード読み取りメソッド
    def read_record_by_email(self):
        email = self.email_var.get()
        if email:
            record = crud.read_record_by_email(email)
            if record:
                self.username_var.set(record[1])
            else:
                messagebox.showerror("Error", "Record not found")
        else:
            messagebox.showerror("Error", "Please enter an email")

    # レコード更新メソッド
    def update_record(self):
        email = self.email_var.get()
        username = self.username_var.get()
        if email:
            if username:
                success = crud.update_record(email, username)
                if success:
                    messagebox.showinfo("Success", "Record updated successfully")
                else:
                    messagebox.showerror("Error", "Record not found")
            else:
                messagebox.showerror("Error", "Please fill in all fields")
        else:
            messagebox.showerror("Error", "Please enter an email")

    # レコード削除メソッド
    def delete_record(self):
        email = self.email_var.get()
        if email:
            crud.delete_record(email)
            self.email_var.set("")
            self.username_var.set("")
            messagebox.showinfo("Success", "Record deleted successfully")
        else:
            messagebox.showerror("Error", "Please enter an email")

# メインルーチン
if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDApp(root)
    root.mainloop()