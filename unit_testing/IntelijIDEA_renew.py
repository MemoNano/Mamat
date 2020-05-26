import os
import platform
import subprocess
import sys

i = "win" if platform.system() == 'Windows' else "mac"
if i == "mac":
    print("...")
    eval = "cd ~/Library/Preferences/IntelliJIdea*/eval && pwd && rm -rf *"
    os.system(eval)

elif i == "win":
    p = subprocess.Popen(["powershell.exe",
                          "cd ~\.IntelliJIdea*\config\eval; ls; rm idea*  "],
                         stdout=sys.stdout)
    p.communicate()
    print("Intellij on Windows was renewed.")

else:
    print("Nothong was changed \n...Exiting...")
    exit
