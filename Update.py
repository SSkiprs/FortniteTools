import os
import subprocess
import sys

def main():
    current_directory = os.getcwd()

    fortnite_main_file = os.path.join(current_directory, "FortniteToolsMain.py")

    if os.path.exists(fortnite_main_file):
        print("Found 'FortniteToolsMain.py' in the current directory.")
        
        subprocess.Popen(["python", fortnite_main_file])
        
        sys.exit()
    else:
        print("Could not find 'FortniteToolsMain.py' in the current directory.")

if __name__ == "__main__":
    main()
