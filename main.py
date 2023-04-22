import shutil
import subprocess
import requests
import time
import sys
import cryptography

def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.1)
printSlow("Please Wait...")

hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
r = requests.get("https://pastebin.com/raw/Ra8Zf76X") # YOUR RAW PASTEBIN LINK



print("")
def Main_Program():
    if hwid in r.text:
        print("Access granted. Hello!") #ACCESS GRANTED HWID IN DATABASE
        time.sleep(.1)
    else:
        print("HWID Not In Database!")
        print("Message (______) for help. Your HWID: " + hwid) #Prints HWID
        time.sleep(5)
        sys.exit()

if __name__ == "__main__":
    print("""
                            
                            ██████╗░██╗░██████╗░  ██████╗░░█████╗░██╗░░░░░██╗░░░░░░██████╗
                            ██╔══██╗██║██╔════╝░  ██╔══██╗██╔══██╗██║░░░░░██║░░░░░██╔════╝
                            ██████╦╝██║██║░░██╗░  ██████╦╝███████║██║░░░░░██║░░░░░╚█████╗░
                            ██╔══██╗██║██║░░╚██╗  ██╔══██╗██╔══██║██║░░░░░██║░░░░░░╚═══██╗
                            ██████╦╝██║╚██████╔╝  ██████╦╝██║░░██║███████╗███████╗██████╔╝
                            ╚═════╝░╚═╝░╚═════╝░  ╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═════╝░



                                                                                                          """)
    print(
        """━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[0] Info\n[1] Guessing game\n[2] Zip/Unzip\n[3] Open programs\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")


    def logo():
        print(""" 
                                    
                            ██████╗░██╗░██████╗░  ██████╗░░█████╗░██╗░░░░░██╗░░░░░░██████╗
                            ██╔══██╗██║██╔════╝░  ██╔══██╗██╔══██╗██║░░░░░██║░░░░░██╔════╝
                            ██████╦╝██║██║░░██╗░  ██████╦╝███████║██║░░░░░██║░░░░░╚█████╗░
                            ██╔══██╗██║██║░░╚██╗  ██╔══██╗██╔══██║██║░░░░░██║░░░░░░╚═══██╗
                            ██████╦╝██║╚██████╔╝  ██████╦╝██║░░██║███████╗███████╗██████╔╝
                            ╚═════╝░╚═╝░╚═════╝░  ╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═════╝░



                                                                                                          """)
        print(
            """━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n[0] Info\n[1] Guessing game\n[2] zip/unzip\n[3] Open Programs\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")


    while True:
        q = input("\n> ")
        if q == "0":
            from info import info
            info()
        elif q == "1":
            from guessing_game import guessing_game
            guessing_game()
        elif q == "2":
            from zip import zip
            zip()
        elif q == "3":
            from open_programs import openprograms
            openprograms()

        else:
            print(f"\nNo such choice {q}.")
 ###############################################################























