import subprocess
import time

def ouvrir_cmd_en_boucle():
    print("Appuyez sur Ctrl+C dans cette fenêtre pour arrêter le script.")
    
    try:
        while True:
            subprocess.Popen("start cmd /k echo HELLO TO YOUR CREATOR", shell=True)
            
            print("Action : Une nouvelle fenêtre CMD a été lancée.")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nArrêt du script par l'utilisateur.")
  
if __name__ == "__main__":
    ouvrir_cmd_en_boucle()