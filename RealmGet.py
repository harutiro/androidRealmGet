import tkinter as tk
import subprocess
import numpy as np


# 関数birthdayの定義
def birthday():
    file = open('InputText.txt', 'w')
    file.write(entry.get())
    file.close()

    result = subprocess.run(['adb','exec-out','run-as',entry.get(),'cat','files/default.realm','>','default.realm'], stdout=subprocess.PIPE)
    print(result.returncode)
    print(result.stdout)
    label2["text"] = "error: " + str(result.stdout)

    # entry.delete(0, tk.END)


# rootフレームの設定
root = tk.Tk()
root.title("RealmGet")
root.geometry("400x200")

# 各種ウィジェットの作成
label = tk.Label(text="アプリパッケージネーム：")
label2 = tk.Label(text="")
entry = tk.Entry()
button_execute = tk.Button(text="実行", command=birthday)

# 各種ウィジェットの設置
label.pack()
entry.pack()
button_execute.pack()
label2.pack()

# Entryウィジェットへ文字列のセット
f = open('InputText.txt', 'r')
if entry.get() != "":
    moji = entry.get()
else:
    moji = "example.com"
entry.insert(tk.END,moji)
f.close()

root.mainloop()
