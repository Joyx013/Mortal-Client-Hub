import tkinter as tk

def toggle_mod(mod_name, btn):
    if btn.cget("bg") == "#1A1A1A":
        btn.config(bg="#A020F0", fg="white", text=f"{mod_name}: ON")
        print(f"[Mortal] Mod Attivata: {mod_name}")
    else:
        btn.config(bg="#1A1A1A", fg="#aaaaaa", text=f"{mod_name}: OFF")
        print(f"[Mortal] Mod Disattivata: {mod_name}")

def toggle_menu(event):
    if root.state() == 'withdrawn':
        root.deiconify()
    else:
        root.withdraw()

root = tk.Tk()
root.title("Mortal Client - Mod Manager")
root.geometry("600x850")
root.configure(bg='#080808')
root.withdraw()
root.bind_all("<Shift_R>", toggle_menu)

title = tk.Label(root, text="MORTAL UI", fg="#A020F0", bg="#080808", font=("Impact", 40))
title.pack(pady=30)

# LISTA CON I NOMI ORIGINALI DAI TUOI SCREENSHOT
# Questi nomi devono corrispondere ai file .jar che hai caricato
mods_list = [
    "Keystrokes-8.1.2 (1.8.9) 2",
    "BetterSprinting-1.8.9-v2.3.0",
    "OldAnimationsMod-Animations & Cosmetics_2.7.1-mc_Forge1.8.9",
    "Patcher-1.8.9 (1.8.9)",
    "OptiFine_1.8.9_HD_U_L5"
]

frame = tk.Frame(root, bg="#080808")
frame.pack(pady=10)

for mod in mods_list:
    btn = tk.Button(frame, text=f"{mod}: OFF", width=45, height=2, 
                   bg="#1A1A1A", fg="#aaaaaa", font=("Arial", 9, "bold"),
                   relief="flat", activebackground="#A020F0")
    btn.config(command=lambda m=mod, b=btn: toggle_mod(m, b))
    btn.pack(pady=8)

play_btn = tk.Button(root, text="AVVIA MORTAL CLIENT", width=30, height=2,
                    bg="#FFFFFF", fg="#A020F0", font=("Arial", 12, "bold"),
                    command=lambda: print("Avvio con le mod selezionate..."))
play_btn.pack(side="bottom", pady=40)

root.mainloop()
