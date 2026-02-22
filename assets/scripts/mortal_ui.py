import tkinter as tk

def toggle_mod(mod_name, btn):
    if btn.cget("bg") == "#1A1A1A":
        btn.config(bg="#A020F0", fg="white", text=f"{mod_name}: ON")
        print(f"[Mortal] {mod_name} ATTIVATA")
    else:
        btn.config(bg="#1A1A1A", fg="#aaaaaa", text=f"{mod_name}: OFF")
        print(f"[Mortal] {mod_name} DISATTIVATA")

def toggle_menu(event):
    if root.state() == 'withdrawn':
        root.deiconify()
    else:
        root.withdraw()

root = tk.Tk()
root.title("Mortal Client - Light Version")
root.geometry("500x600")
root.configure(bg='#080808')

# Nascondi all'avvio (Apri con RSHIFT)
root.withdraw()
root.bind_all("<Shift_R>", toggle_menu)

title = tk.Label(root, text="MORTAL UI", fg="#A020F0", bg="#080808", font=("Impact", 40))
title.pack(pady=50)

# Unico tasto per Keystrokes
mod = "KEYSTROKES"
btn_keystrokes = tk.Button(root, text=f"{mod}: OFF", width=25, height=2, 
                          bg="#1A1A1A", fg="#aaaaaa", font=("Arial", 14, "bold"),
                          relief="flat", activebackground="#A020F0")

btn_keystrokes.config(command=lambda: toggle_mod(mod, btn_keystrokes))
btn_keystrokes.pack(pady=20)

# Tasto Avvio
play_btn = tk.Button(root, text="PLAY MORTAL CLIENT", width=30, height=2,
                    bg="#FFFFFF", fg="#A020F0", font=("Arial", 12, "bold"),
                    command=lambda: print("Avvio con Keystrokes..."))
play_btn.pack(side="bottom", pady=50)

root.mainloop()
