#Comment devenir developpeur 
import webbrowser
from pycenter import center
from pystyle import Colorate, Colors
from os import system


title="""

$$\                       $$\               $$\ $$\         $$$$$$$\                            
\__|                      $$ |              $$ |$$ |        $$  __$$\                           
$$\ $$$$$$$\   $$$$$$$\ $$$$$$\    $$$$$$\  $$ |$$ |        $$ |  $$ | $$$$$$\ $$\    $$\       
$$ |$$  __$$\ $$  _____|\_$$  _|   \____$$\ $$ |$$ |$$$$$$\ $$ |  $$ |$$  __$$\\$$\  $$  |      
$$ |$$ |  $$ |\$$$$$$\    $$ |     $$$$$$$ |$$ |$$ |\______|$$ |  $$ |$$$$$$$$ |\$$\$$  /       
$$ |$$ |  $$ | \____$$\   $$ |$$\ $$  __$$ |$$ |$$ |        $$ |  $$ |$$   ____| \$$$  /        
$$ |$$ |  $$ |$$$$$$$  |  \$$$$  |\$$$$$$$ |$$ |$$ |        $$$$$$$  |\$$$$$$$\   \$  /         
\__|\__|  \__|\_______/    \____/  \_______|\__|\__|        \_______/  \_______|   \_/     



"""
print(Colorate.Horizontal(Colors.blue_to_red, center(title)))

# Acceder au service pour devenir devellopeur
print(Colorate.Horizontal(Colors.blue_to_green, f"1.Télécharger Python"))
print(Colorate.Horizontal(Colors.blue_to_green, f"2.Télécharger Pycharm"))
print(Colorate.Horizontal(Colors.blue_to_green, f"3.Télécharger Visual Studio Code"))
print(Colorate.Horizontal(Colors.blue_to_green, f"4.Télécharger Discord"))
print(Colorate.Horizontal(Colors.blue_to_green, f"5.Mon Github :)"))

#python 
def python():
    print("https://www.python.org/downloads/release/python-383/")
    webbrowser.open("https://www.python.org/downloads/release/python-383/")
    


#pycharm
def Pycharm():
    print("https://www.jetbrains.com/pycharm/download/#section=windows")
    webbrowser.open("https://www.jetbrains.com/pycharm/download/#section=windows")

def Visual_Studio_Code():
    print("https://code.visualstudio.com/Download")
    webbrowser.open("https://code.visualstudio.com/Download")

def Discord():
    print("https://discord.com/download")
    webbrowser.open("https://discord.com/download")

# github
def Github():
    print("https://github.com/Prasax-Dev")
    webbrowser.open("https://github.com/Prasax-Dev")

run=True
while run:
    k=input(Colorate.Horizontal(Colors.blue_to_green, f"Choisir la partie: "))
    if k=="1":
        python()
    if k=="2":
        Pycharm()
    if k=="3":
        Visual_Studio_Code()
    if k=="4":
        Discord()
    if k=="5":
        Github()
   