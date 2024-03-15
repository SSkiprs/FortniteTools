import os

def main():
    # Get the current directory
    current_directory = os.getcwd()

    # Check if "FortniteToolsMain.py" exists in the current directory
    if os.path.exists(os.path.join(current_directory, "FortniteToolsMain.py")):
        print("Found 'FortniteToolsMain.py' in the current directory.")
    else:
        print("Could not find 'FortniteToolsMain.py' in the current directory.")

if __name__ == "__main__":
    main()
