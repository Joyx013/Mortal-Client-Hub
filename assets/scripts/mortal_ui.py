import tkinter as tk

def toggle_mod(mod_name, btn):
    if btn.cget("bg") == "#1A1A1A":
        btn.config(bg="#A020F0", fg="white", text=f"{mod_name}: ON")
    else:
        btn.config(bg="#1A1A1A", fg="#aaaaaa", text=f"{mod_name}: OFF")

def toggle_menu(event):
    if root.state() == 'withdrawn':
        root.deiconify()
    else:
        root.withdraw()

root = tk.Tk()
root.title("Mortal Client Manager")
root.geometry("600x700")
root.configure(bg='#080808')
root.withdraw() 
root.bind_all("<Shift_R>", toggle_menu)

title = tk.Label(root, text="MORTAL CLIENT", fg="#A020F0", bg="#080808", font=("Impact", 45))
title.pack(pady=20)

# --- INFO MOD FISSE (Sempre Attive) ---
# Patcher e Optifine vengono caricate automaticamente dal launcher
static_info = tk.Label(root, text="Patcher & Optifine: CARICATE", fg="#555555", bg="#080808", font=("Arial", 9, "bold"))
static_info.pack()

# --- SEZIONE MOD SELEZIONABILI ---
mod_frame = tk.LabelFrame(root, text=" Mod Selezionabili ", fg="#A020F0", bg="#080808", font=("Arial", 10, "bold"), padx=20, pady=20)
mod_frame.pack(pady=20)

# Qui mettiamo solo quelle che vuoi accendere/spegnere
mods_to_show = [
    "Keystrokes-8.1.2 (1.8.9) 2",
    "BetterSprinting-1.8.9-v2.3.0",
    "OldAnimationsMod-Animations & Cosmetics_2.7.1-mc_Forge1.8.9"
]

for mod in mods_to_show:
    btn = tk.Button(mod_frame, text=f"{mod}: OFF", width=45, height=2, 
                   bg="#1A1A1A", fg="#aaaaaa", font=("Arial", 9),
                   relief="flat", activebackground="#A020F0")
    btn.config(command=lambda m=mod, b=btn: toggle_mod(m, b))
    btn.pack(pady=8)

# --- STATUS RESOURCE PACK ---
rp_label = tk.Label(root, text="Custom GUI: Mortal-ResourcePack ATTIVO", fg="#00FF00", bg="#080808", font=("Arial", 9, "italic"))
rp_label.pack(pady=10)

play_btn = tk.Button(root, text="AVVIA MORTAL CLIENT", width=30, height=2,
                    bg="#FFFFFF", fg="#A020F0", font=("Arial", 12, "bold"),
                    command=lambda: print("Lancio in corso con Patcher, Optifine e Mod scelte..."))
play_btn.pack(side="bottom", pady=40)

root.mainloop()
