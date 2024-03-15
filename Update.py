import os
import subprocess
import sys

def main():
    # Get the current directory
    current_directory = os.getcwd()

    # Construct the path to "FortniteToolsMain.py"
    fortnite_main_file = os.path.join(current_directory, "FortniteToolsMain.py")

    # Check if "FortniteToolsMain.py" exists in the current directory
    if os.path.exists(fortnite_main_file):
        print("Found 'FortniteToolsMain.py' in the current directory.")
        
        # Run the Python script
        subprocess.Popen(["python", fortnite_main_file])
        
        # Close the current script
        sys.exit()
    else:
        print("Could not find 'FortniteToolsMain.py' in the current directory.")

if __name__ == "__main__":
    main()
