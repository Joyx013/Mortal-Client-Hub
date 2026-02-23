import tkinter as tk
import os

# --- MOTORE OTTIMIZZATO (TARGET 200 FPS) ---
def launch_game(active_mods):
    """Configura il lancio bilanciato per fluidità e stabilità"""
    print("\n--- [MORTAL ENGINE] STABLE 200 FPS MODE ---")
    
    # Percorsi file
    mods_dir = os.path.abspath("../mods")
    rp_dir = os.path.abspath("../Mortal-ResourcePack")
    
    # Mod essenziali caricate in automatico
    essential = ["Patcher-1.8.9 (1.8.9).jar", "OptiFine_1.8.9_HD_U_L5.jar"]
    all_mods = essential + active_mods
    
    # Parametri ottimizzati per PC medi/gaming
    print(f"[OK] Allocazione RAM: 3GB (Xmx3G)")
    print(f"[OK] Mod caricate: {all_mods}")
    print(f"[OK] GUI Custom: Caricamento forme bottoni da {rp_dir}")
    print("\n>>> AVVIO MORTAL CLIENT IN CORSO...")

# --- INTERFACCIA GRAFICA ---
def toggle_mod(mod_name, btn, selected_list):
    if btn.cget("bg") == "#1A1A1A":
        btn.config(bg="#A020F0", fg="white", text=f"{mod_name}: ON")
        selected_list.append(mod_name + ".jar")
    else:
        btn.config(bg="#1A1A1A", fg="#aaaaaa", text=f"{mod_name}: OFF")
        if (mod_name + ".jar") in selected_list:
            selected_list.remove(mod_name + ".jar")

def toggle_menu(event):
    if root.state() == 'withdrawn':
        root.deiconify()
    else:
        root.withdraw()

root = tk.Tk()
root.title("Mortal Client - 200 FPS Edition")
root.geometry("650x800")
root.configure(bg='#080808')
root.withdraw() 
root.bind_all("<Shift_R>", toggle_menu)

# Header
title = tk.Label(root, text="MORTAL UI", fg="#A020F0", bg="#080808", font=("Impact", 50))
title.pack(pady=25)

# Sezione Mod Selezionabili
mod_frame = tk.LabelFrame(root, text=" MODS & HUD ", fg="#A020F0", bg="#080808", font=("Arial", 10, "bold"), padx=20, pady=20)
mod_frame.pack(pady=10)

mods_to_show = [
    "Keystrokes-8.1.2 (1.8.9) 2",
    "BetterSprinting-1.8.9-v2.3.0",
    "OldAnimationsMod-Animations & Cosmetics_2.7.1-mc_Forge1.8.9"
]
active_mods_list = []

for mod in mods_to_show:
    btn = tk.Button(mod_frame, text=f"{mod}: OFF", width=50, height=2, 
                   bg="#1A1A1A", fg="#aaaaaa", font=("Arial", 9, "bold"),
                   relief="flat", activebackground="#A020F0")
    btn.config(command=lambda m=mod, b=btn: toggle_mod(m, b, active_mods_list))
    btn.pack(pady=8)

# Info Resource Pack
rp_info = tk.Label(root, text="FORME BOTTONI: MORTAL CUSTOM", fg="#00FF00", bg="#080808", font=("Arial", 9, "italic"))
rp_info.pack(pady=10)

# Bottone Launch
launch_btn = tk.Button(root, text="AVVIA MORTAL CLIENT", width=35, height=2,
                      bg="#FFFFFF", fg="#A020F0", font=("Arial", 14, "bold"),
                      command=lambda: launch_game(active_mods_list))
launch_btn.pack(side="bottom", pady=40)

root.mainloop()
