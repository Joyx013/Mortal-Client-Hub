import tkinter as tk

# Funzione per cambiare lo stato del tasto (ON/OFF)
def toggle_mod(mod_name, btn):
    if btn.cget("bg") == "#1A1A1A": # Se è spento
        btn.config(bg="#A020F0", fg="white", text=f"{mod_name}: ON")
        print(f"[Mortal Client] {mod_name} ATTIVATA")
    else: # Se è acceso
        btn.config(bg="#1A1A1A", fg="#aaaaaa", text=f"{mod_name}: OFF")
        print(f"[Mortal Client] {mod_name} DISATTIVATA")

# Funzione per mostrare/nascondere il menu con RSHIFT
def toggle_menu(event):
    if root.state() == 'withdrawn':
        root.deiconify() # Mostra la finestra
    else:
        root.withdraw()  # Nasconde la finestra

root = tk.Tk()
root.title("Mortal Client GUI")
root.geometry("600x800")
root.configure(bg='#080808')

# La finestra parte nascosta (si apre solo premendo RSHIFT)
root.withdraw()

# COLLEGIAMO IL TASTO RSHIFT
root.bind_all("<Shift_R>", toggle_menu)

# Titolo della GUI
title = tk.Label(root, text="MORTAL GUI", fg="#A020F0", bg="#080808", font=("Impact", 35))
title.pack(pady=30)

# Lista delle Mod
mods = ["FPS", "KEYSTROKES", "PING", "TOGGLE SPRINT", "COSMETICS", "REACH DISPLAY"]

# Creazione dei tasti grandi (250x60 circa)
for mod in mods:
    btn = tk.Button(root, 
                   text=f"{mod}: OFF", 
                   width=25, 
                   height=2, 
                   bg="#1A1A1A", 
                   fg="#aaaaaa", 
                   font=("Arial", 12, "bold"),
                   relief="flat",
                   activebackground="#A020F0")
    
    # Associa la funzione al click
    btn.config(command=lambda m=mod, b=btn: toggle_mod(m, b))
    btn.pack(pady=10)

# Istruzione in fondo
info = tk.Label(root, text="Premi RSHIFT per chiudere", fg="#444444", bg="#080808", font=("Arial", 10))
info.pack(side="bottom", pady=20)

print("Mortal Client in esecuzione...")
print("-> Premi il tasto SHIFT a destra (RSHIFT) per aprire il menu delle mod!")

root.mainloop()
