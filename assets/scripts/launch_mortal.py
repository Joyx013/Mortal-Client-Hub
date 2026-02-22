import os
import subprocess

def avvia_gioco(mod_selezionate):
    # Percorsi delle cartelle (Python calcola dove si trovano i file)
    cartella_mods = os.path.abspath("../mods")
    cartella_resource_pack = os.path.abspath("../Mortal-ResourcePack")
    
    print("--- MORTAL CLIENT ENGINE ---")
    print(f"Iniezione Forme Bottoni da: {cartella_resource_pack}")
    
    # Mod che partono SEMPRE
    mod_fisse = [
        "Patcher-1.8.9 (1.8.9).jar", 
        "OptiFine_1.8.9_HD_U_L5.jar"
    ]
    
    # Lista finale delle mod da caricare
    lista_finale = mod_fisse + mod_selezionate
    
    print(f"Mod che verranno caricate: {lista_finale}")
    
    # LUNEDÌ AL PC: Qui inseriremo il comando 'subprocess.run' 
    # che lancia effettivamente Minecraft con la RAM dedicata.
    print("Sistema pronto. In attesa di connessione al PC...")

if __name__ == "__main__":
    # Test di sicurezza: se lanci lo script da solo, simula un avvio vuoto
    avvia_gioco([])
