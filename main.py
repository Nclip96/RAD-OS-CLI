import os
import webview
import subprocess
import json
import time

if not os.path.exists('tour.py'): # creates the tour.py file (tour.py is created here to keep the files required to download as low as possible.)
    with open('tour.py', 'w') as f:
        f.write('import time\n')
        f.write('print("Welcome to RAD OS! Would you like to take a tour? (y/n)")\n')
        f.write('time.sleep(0.1)\n')
        f.write('tour = input()\n')
        f.write('if tour == "y":\n')
        f.write('    time.sleep(0.1)\n')
        f.write('    print("RAD OS is a simple command-line operating system with basic file management and web browsing capabilities.")\n')
        f.write('    time.sleep(0.1)\n')
        f.write('    print("You can use commands like \'browse duckduckgo\', \'view files\', \'cat <filename>\', and more!")\n')
        f.write('    time.sleep(0.1\n)')
        f.write('    print("Type \'help\' to see a list of available commands.")\n')
        f.write('    time.sleep(0.1)\n')
        f.write('    print("Enjoy your experience with RAD OS!")\n')
        f.write('    time.sleep(0.1)\n')
        f.write('if tour == "n":\n')
        f.write('    time.sleep(0.1)\n')
        f.write('    print("Tour has been skipped. Enjoy your experience with RAD OS!")\n')

if not os.path.exists('test.txt'): # creates a test file for testing commands that edit/read files.
    with open('test.txt', 'w') as f:
        f.write('Hello World!')

def ensure_data_json(): # creates the main json file for storing simple things that need to be remembered by the OS. If data.json is deleted, it won't break anything, but it will reset the OS state.
    if not os.path.exists('data.json'):
        with open('data.json', 'w') as f:
            json.dump({'TourComplete': False,}, f)

ensure_data_json()

with open('data.json', 'r') as file:
    data = json.load(file)
    if not data.get('TourComplete'):
        subprocess.run(['python', 'tour.py'])
        data['TourComplete'] = True
        with open('data.json', 'w') as file:
            json.dump(data, file)


while True: # duckduckgo browsing command
    command = input("RAD OS-+> ")
    if command == "browse duckduckgo":
        webview.create_window("Browser", "https://duckduckgo.com", width=800, height=600)
        webview.start()

    elif command == "browse google":  # google browsing command
        webview.create_window("Browser", "https://google.com", width=800, height=600)
        webview.start()

    elif command == "browse":  # browses with your default browser
        with open('data.json', 'r') as file:
            data = json.load(file)
            fav_browser = data.get('FavBrowser', 'duckduckgo')
            if fav_browser == "duckduckgo":
                webview.create_window("Browser", "https://duckduckgo.com", width=800, height=600)
            elif fav_browser == "google":
                webview.create_window("Browser", "https://google.com", width=800, height=600)
            elif fav_browser == "bing":
                webview.create_window("Browser", "https://bing.com", width=800, height=600)
            elif fav_browser == "yahoo":
                webview.create_window("Browser", "https://yahoo.com", width=800, height=600)
            else:
                print("No favorite browser set. Please set a favorite browser.")
        webview.start()

    elif command == "browse bing":  # ugly bing browsing command
        webview.create_window("Browser", "https://bing.com", width=800, height=600)
        webview.start()

    elif command == "browse yahoo":  # yahoo browsing command
        webview.create_window("Browser", "https://yahoo.com", width=800, height=600)
        webview.start()

    elif command == "launch proxy":  # launches a web proxy because why not
        webview.create_window("Proxy", "https://www.croxyproxy.com", width=800, height=600)
        webview.start()

    elif command == "view files":  # shows all files in directory (The "OS" is really just a basic program. It can not browse other directories.)
        print("Files in RAD OS filesystem:")
        for filename in os.listdir():
            print(f"  {filename}")

    elif command.startswith("cat "):  # the command we all know and love, reads out the file put next to it.
        filename = command[4:].strip()
        if filename and os.path.isfile(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                print(f.read())
        else:
            print("File not found.")

    elif command.startswith("write "): # cat but it creates instead of reading.
        parts = command[6:].split(" ", 1)
        if len(parts) == 2:
            filename, content = parts
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)

    elif command.startswith("edit "): # edits upon files already written
        filename = command[5:].strip()
        if filename and os.path.isfile(filename):
            with open(filename, 'r+', encoding='utf-8') as f:
                print(f"Current content of {filename}:")
                print(f.read())
                new_content = input("Enter new content: ")
                f.seek(0)
                f.write(new_content)
                f.truncate()

    elif command == "clear": # clears the terminal. things can get cluttered!
        print("\033c", end="")

    elif command == "help":  # shows all available commands.
        print("Available commands:")
        time.sleep(0.1)
        print("  browse duckduckgo - Open DuckDuckGo in a browser window")
        time.sleep(0.1)
        print("  browse google - Open Google in a browser window")
        time.sleep(0.1)
        print("  browse bing - Open Bing in a browser window")
        time.sleep(0.1)
        print("  browse yahoo - Open Yahoo in a browser window")
        time.sleep(0.1)
        print("  launch proxy - Open CroxyProxy in a browser window")
        time.sleep(0.1)
        print("  view files - List files in the RAD OS filesystem")
        time.sleep(0.1)
        print("  cat <filename> - Display the contents of a file")
        time.sleep(0.1)
        print("  write <filename> <content> - Write content to a file")
        time.sleep(0.1)
        print("  edit <filename> - Edit the contents of a file")
        time.sleep(0.1)
        print("  clear - Clear the terminal screen")
        time.sleep(0.1)
        print("  help - Show this help message")
        time.sleep(0.1)
        print("  sysinfo - Show system information")
        time.sleep(0.1)
        print("  uptime - Show RAD OS uptime")
        time.sleep(0.1)
        print("  debug help - Show debug help information (requires password)")
        time.sleep(0.1)
        print("  set browser <browser> - Set favorite browser (duckduckgo/google/bing/yahoo)")
        time.sleep(0.1)
        print("  direct browse <url> - Launch a URL directly instead of finding it in search.")
        time.sleep(0.1)
        print("  python execute <file> - Run a Python File")
        time.sleep(0.1)

    elif command.startswith("set browser"):  # sets the default browser
        bparts = command.split()
        if len(bparts) == 3:
            browser = bparts[2].strip()
        else:
            browser = input("Enter your favorite browser (duckduckgo/google/bing/yahoo): ").strip()
        if browser in ["duckduckgo", "google", "bing", "yahoo"]:
            with open('data.json', 'r') as file:
                data = json.load(file)
            data['FavBrowser'] = browser
            with open('data.json', 'w') as file:
                json.dump(data, file)
            print(f"Favorite browser set to {browser}.")
        else:
            print("Invalid browser choice.")

    elif command.startswith("direct browse"): # launches a URL directly without needing to search for it.
        parts = command.split(maxsplit=2)
        if len(parts) >= 3:
            url = parts[2].strip()
        else:
            url = input("Enter URL to browse: ").strip()

        if not url:
            print("No URL provided.")
        else:
            if not (url.startswith("http://") or url.startswith("https://")):
                url = "https://" + url
            try:
                webview.create_window("Site", url, width=800, height=600)
                webview.start()
            except Exception as e:
                print(f"Failed to open URL: {e}")

    elif command == "sysinfo":  # displays system info.
        print("RAD OS System Information:")
        time.sleep(0.1)
        print(f"  Current Working Directory: {os.getcwd()}")
        time.sleep(0.1)
        print(f"  Files in RAD OS filesystem: {len(os.listdir())}")
        time.sleep(0.1)
        print(f"  Python Version: {os.sys.version}")
        time.sleep(0.1)

    elif command == "uptime": # the most broken command. I dont know what it does.
        print("RAD OS Uptime:")
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            print(f"RAD OS Uptime: {uptime_seconds / 3600:.2f} hours")
    
    elif command == "exit": # exits the terminal
        confirm = input("Are you sure you want to exit RAD OS? (y/n): ")
        if confirm == "y":
            print("Exiting RAD OS...")
            break

    elif command == "cpu temp": # checks the CPU temp. (untested)
        result = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True, text=True)
        print(f"Pi CPU Temperature: {result.stdout.strip()}")

    elif command == "debug help": # shows debug commands. 
        password = input("Enter debug password: ")
        if password == "RADOSDEBUG":
            print("Debug help information:")
            time.sleep(0.1)
            print("  debug help - Show debug help information")
            time.sleep(0.1)
            print("  debug reset - reset the entire RAD OS system (WARNING: This will delete all files and reset the system!)")
            time.sleep(0.1)
            print("  debug install <package> - install a python package (WARNING: This will download and install a package from the internet!)")
            time.sleep(0.1)

    elif command == "debug reset": # resets the OS by deleting all files except this.
        time.sleep(0.1)
        password = input("Enter debug password: ")
        if password == "RADOSDEBUG":
            time.sleep(0.1)
            confirm = input("Are you sure you want to reset the entire RAD OS system? This will delete all files and reset the system! (y/n): ")
            if confirm == "y":
                for filename in os.listdir():
                    os.remove(filename)

                print("RAD OS system has been reset.")
            else:
                print("Reset cancelled.")
        else:
            print("Incorrect debug password.")

    elif command.startswith("debug install "): # runs pip install to install python packages.
        password = input("Enter debug password: ")
        if password == "RADOSDEBUG":
            package = command[14:].strip()
            if package:
                print(f"Installing package: {package}")
                os.system(f"pip install {package}")
                print(f"Package {package} installed successfully.")
            else:
                print("No package specified.")
        else:
            print("Incorrect debug password.")

    elif command.startswith("python execute"): # lets you execute python. if you run this, you clearly have python, so you can run more python with python!
        filename = command[15:].strip()
        if filename:
            if os.path.exists(filename):
                os.system(f"python {filename}")
            else:
                print(f"File '{filename}' not found.")
        else:
            print("No file specified.")

    else:
        print("Unknown command.")
