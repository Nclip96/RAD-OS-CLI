import os # module imports
os.system("pip install webview")
os.system("pip install subprocess")
os.system("pip install json")
os.system("pip install time")
os.system("pip install shutil")
import webview
import subprocess
import json
import time
import shutil

if not os.path.exists('tour.py'): # creates the tour script if it doesn't exist.
    with open('tour.py', 'w') as f:
        f.write('import time\n')
        f.write('print("Welcome to RAD OS! Would you like to take a tour? (y/n)")\n')
        f.write('time.sleep(0.01)\n')
        f.write('tour = input()\n')
        f.write('if tour == "y":\n')
        f.write('    time.sleep(0.1)\n')
        f.write('    print("RAD OS is a simple command-line operating system with basic file management and web browsing capabilities.")\n')
        f.write('    time.sleep(0.1)\n')
        f.write('    print("You can use commands like \'browse duckduckgo\', \'view files\', \'cat <filename>\', and more!")\n')
        f.write('    time.sleep(0.1)\n')
        f.write('    print("Type \'help\' to see a list of available commands.")\n')
        f.write('    time.sleep(0.1)\n')
        f.write('    print("Enjoy your experience with RAD OS!")\n')
        f.write('    time.sleep(0.1)\n')
        f.write('if tour == "n":\n')
        f.write('    time.sleep(0.1)\n')
        f.write('    print("Tour has been skipped. Enjoy your experience with RAD OS!")\n')

with open('snake.py', 'w', encoding='utf-8') as f:  # creates the snake game script if it doesn't exist.
    f.write('import pygame\n')
    f.write('import random\n')
    f.write('import sys\n')
    f.write('\n')
    f.write('print("LAUNCHING SNAKE. GAME CREATED WITH PYGAME.")')
    f.write('SCREEN_WIDTH = 600\n')
    f.write('SCREEN_HEIGHT = 400\n')
    f.write('BLOCK_SIZE = 20\n')
    f.write('FPS = 10\n')
    f.write('\n')
    f.write('WHITE = (255, 255, 255)\n')
    f.write('BLACK = (0, 0, 0)\n')
    f.write('GREEN = (0, 255, 0)\n')
    f.write('RED = (255, 0, 0)\n')
    f.write('\n')
    f.write('class Snake:\n')
    f.write('    def __init__(self):\n')
    f.write('        self.body = [(100, 100), (80, 100), (60, 100)]\n')
    f.write('        self.direction = (BLOCK_SIZE, 0)\n')
    f.write('        self.growing = False\n')
    f.write('\n')
    f.write('    def move(self):\n')
    f.write('        head_x, head_y = self.body[0]\n')
    f.write('        delta_x, delta_y = self.direction\n')
    f.write('        new_head = (head_x + delta_x, head_y + delta_y)\n')
    f.write('        self.body = [new_head] + self.body\n')
    f.write('        if not self.growing:\n')
    f.write('            self.body.pop()\n')
    f.write('        else:\n')
    f.write('            self.growing = False\n')
    f.write('\n')
    f.write('    def grow(self):\n')
    f.write('        self.growing = True\n')
    f.write('\n')
    f.write('    def set_direction(self, direction):\n')
    f.write('        opposite_direction = (-self.direction[0], -self.direction[1])\n')
    f.write('        if direction != opposite_direction:\n')
    f.write('            self.direction = direction\n')
    f.write('\n')
    f.write('    def check_collision(self):\n')
    f.write('        head_x, head_y = self.body[0]\n')
    f.write('        if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:\n')
    f.write('            return True\n')
    f.write('        if self.body[0] in self.body[1:]:\n')
    f.write('            return True\n')
    f.write('        return False\n')
    f.write('\n')
    f.write('class Food:\n')
    f.write('    def __init__(self):\n')
    f.write('        self.position = (0, 0)\n')
    f.write('        self.spawn()\n')
    f.write('\n')
    f.write('    def spawn(self):\n')
    f.write('        x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE\n')
    f.write('        y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE\n')
    f.write('        self.position = (x, y)\n')
    f.write('\n')
    f.write('    def draw(self, screen):\n')
    f.write('        pygame.draw.rect(screen, RED, pygame.Rect(self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))\n')
    f.write('\n')
    f.write('class Game:\n')
    f.write('    def __init__(self):\n')
    f.write('        pygame.init()\n')
    f.write('        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))\n')
    f.write('        pygame.display.set_caption(\'Snake Game\')\n')
    f.write('        self.clock = pygame.time.Clock()\n')
    f.write('        self.snake = Snake()\n')
    f.write('        self.food = Food()\n')
    f.write('        self.score = 0\n')
    f.write('        self.running = True\n')
    f.write('\n')
    f.write('    def handle_events(self):\n')
    f.write('        for event in pygame.event.get():\n')
    f.write('            if event.type == pygame.QUIT:\n')
    f.write('                pygame.quit()\n')
    f.write('                sys.exit()\n')
    f.write('            elif event.type == pygame.KEYDOWN:\n')
    f.write('                if event.key == pygame.K_UP:\n')
    f.write('                    self.snake.set_direction((0, -BLOCK_SIZE))\n')
    f.write('                elif event.key == pygame.K_DOWN:\n')
    f.write('                    self.snake.set_direction((0, BLOCK_SIZE))\n')
    f.write('                elif event.key == pygame.K_LEFT:\n')
    f.write('                    self.snake.set_direction((-BLOCK_SIZE, 0))\n')
    f.write('                elif event.key == pygame.K_RIGHT:\n')
    f.write('                    self.snake.set_direction((BLOCK_SIZE, 0))\n')
    f.write('\n')
    f.write('    def update(self):\n')
    f.write('        self.snake.move()\n')
    f.write('        if self.snake.body[0] == self.food.position:\n')
    f.write('            self.snake.grow()\n')
    f.write('            self.food.spawn()\n')
    f.write('            self.score += 1\n')
    f.write('            if self.score % 5 == 0:\n')
    f.write('                global FPS\n')
    f.write('                FPS += 2\n')
    f.write('        if self.snake.check_collision():\n')
    f.write('            self.running = False\n')
    f.write('\n')
    f.write('    def draw_elements(self):\n')
    f.write('        self.screen.fill(BLACK)\n')
    f.write('        for segment in self.snake.body:\n')
    f.write('            pygame.draw.rect(self.screen, GREEN, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))\n')
    f.write('        self.food.draw(self.screen)\n')
    f.write('        self.draw_score()\n')
    f.write('\n')
    f.write('    def draw_score(self):\n')
    f.write('        font = pygame.font.Font(None, 36)\n')
    f.write('        text = font.render(f\'Score: {self.score}\', True, WHITE)\n')
    f.write('        self.screen.blit(text, (10, 10))\n')
    f.write('\n')
    f.write('    def run(self):\n')
    f.write('        while self.running:\n')
    f.write('            self.handle_events()\n')
    f.write('            self.update()\n')
    f.write('            self.draw_elements()\n')
    f.write('            pygame.display.flip()\n')
    f.write('            self.clock.tick(FPS)\n')
    f.write('        self.game_over()\n')
    f.write('\n')
    f.write('    def game_over(self):\n')
    f.write('        self.screen.fill(BLACK)\n')
    f.write('        font = pygame.font.Font(None, 48)\n')
    f.write('        text = font.render(\'Game Over\', True, WHITE)\n')
    f.write('        self.screen.blit(text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 24))\n')
    f.write('        score_text = font.render(f\'Score: {self.score}\', True, WHITE)\n')
    f.write('        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 + 24))\n')
    f.write('        pygame.display.flip()\n')
    f.write('        pygame.time.wait(2000)\n')
    f.write('        pygame.quit()\n')
    f.write('        sys.exit()\n')
    f.write('\n')
    f.write('if __name__ == "__main__":\n')
    f.write('    game = Game()\n')
    f.write('    game.run()\n')

if not os.path.exists('test.txt'):  # creates the test.txt file if it doesn't exist.
    with open('test.txt', 'w') as f:
        f.write('Hello World!')

def ensure_data_json():  # defines ensure json, which writes the actual data.json file.
    if not os.path.exists('data.json'):
        with open('data.json', 'w') as f:
            json.dump({'TourComplete': False, 'Password': None,}, f)

ensure_data_json()

with open('data.json', 'r') as file:  # reads data.json and sets variable data to the json file.
    data = json.load(file)

if not data.get('TourComplete'):  # runs the tour and tells the json that the tour has been completed so it doesnt run again at startup
    subprocess.run(['python', 'tour.py'])
    data['TourComplete'] = True
    with open('data.json', 'w') as f:
        json.dump(data, f)

if data.get('Password') is None: # asks the user to set system password. the password is then stored in data.json.
    password = input("Please enter a system password: ")
    data['Password'] = password
    with open('data.json', 'w') as f:
        json.dump(data, f)
    print("Thank you! Launching RAD OS...")
    time.sleep(1)
    print("\033c", end="")
else:
    enteredpassword = input("Please Enter Your Password: ") # asks the user to enter password.
    if data.get('Password') == enteredpassword:
        print("Thank you! Launching RAD OS...")
        time.sleep(1)
        print("\033c", end="")
    else:
        print("Incorrect. Session Terminated.") # kills the session if the password is wrong. Remember. Your. Password.
        while True:
            time.sleep(5)




while True: # start of the actual CLI.
    command = input("RAD OS-+> ") # input thing.
    if command == "browse duckduckgo": # this command launches duckduckgo.
        webview.create_window("Browser", "https://duckduckgo.com", width=800, height=600)
        webview.start()

    elif command == "browse google": # this command launches google
        webview.create_window("Browser", "https://google.com", width=800, height=600)
        webview.start()

    elif command == "browse": # this command takes your default browser, and launches that. (favorite browser must be set with the 'set browser' command.)
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

    elif command == "browse bing":
        webview.create_window("Browser", "https://bing.com", width=800, height=600)
        webview.start()

    elif command == "browse yahoo":
        webview.create_window("Browser", "https://yahoo.com", width=800, height=600)
        webview.start()

    elif command == "launch proxy":
        webview.create_window("Proxy", "https://www.croxyproxy.com", width=800, height=600)
        webview.start()

    elif command == "view files": # this command views the files on the OS directory. (The OS is meant to function only in one directory.)
        print("Files in RAD OS filesystem:")
        for filename in os.listdir():
            print(f"  {filename}")

    elif command.startswith("cat "): # this command reads a file.
        filename = command[4:].strip()
        if filename and os.path.isfile(filename):
            if not filename == "data.json" or "tour.py":
                with open(filename, 'r', encoding='utf-8') as f:
                    print(f.read())
            
            else:
                print("File can not be read for security reasons.")
        
        else:
            print("File not found.")

    elif command.startswith("write "): # this command creates a file and lets you write data to it.
        filename = command[6:].strip()
        if filename:
            print("Enter content (type 'END' on a new line to finish):")
            lines = []
            while True:
                line = input()
                if line == "END":
                    break
                lines.append(line)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))

    elif command.startswith("edit "): # this command edits a file that already exist.
        filename = command[5:].strip()
        if filename and os.path.isfile(filename):
            if not filename == "data.json" or "tour.py":
                with open(filename, 'r', encoding='utf-8') as f:
                    print(f"Current content of {filename}:")
                    print(f.read())
                print("Enter new content (type 'END' on a new line to finish):")
                lines = []
                while True:
                    line = input()
                    if line == "END":
                        break
                    lines.append(line)
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(lines))
            else:
                print("File can not be edited for security reasons")

    elif command == "clear": # this command clears the terminal
        print("\033c", end="")

    elif command == "help": # this command shows an explanation of all commands.
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
        print("  write <filename> <content> - Create a new file and write content to it")
        time.sleep(0.1)
        print("  edit <filename> - Edit the contents of a file")
        time.sleep(0.1)
        print("  clear - Clear the terminal screen")
        time.sleep(0.1)
        print("  help - Show this help message")
        time.sleep(0.1)
        print("  sysinfo - Show system information")
        time.sleep(0.1)
        print("  debug help - Show debug help information (requires password)")
        time.sleep(0.1)
        print("  set browser <browser> - Set favorite browser (duckduckgo/google/bing/yahoo)")
        time.sleep(0.1)
        print("  direct browse <url> - Launch a URL directly instead of finding it in search.")
        time.sleep(0.1)
        print("  python execute <file> - Run a Python File")
        time.sleep(0.1)

    elif command.startswith("set browser"): # this command sets the default browser.
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

    elif command.startswith("direct browse"): # this command launches a URL directly.
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

    elif command == "sysinfo": # this command shows the system info.
        print("RAD OS System Information:")
        time.sleep(0.1)
        print(f"  Current Working Directory: {os.getcwd()}")
        time.sleep(0.1)
        print(f"  Files in RAD OS filesystem: {len(os.listdir())}")
        time.sleep(0.1)
        print(f"  Python Version: {os.sys.version}")
        time.sleep(0.1)
    
    elif command == "exit": # this command exists RAD OS.
        confirm = input("Are you sure you want to exit RAD OS? (y/n): ")
        if confirm == "y":
            print("Exiting RAD OS...")
            break

    elif command == "cpu temp": # this command checks the CPU temp.
        result = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True, text=True)
        print(f"Pi CPU Temperature: {result.stdout.strip()}")

    elif command == "debug help": # this command shows debug commands.
        password = input("Enter debug password: ")
        if password == data["Password"]:
            print("Debug help information:")
            time.sleep(0.1)
            print("  debug help - Show debug help information")
            time.sleep(0.1)
            print("  debug reset - reset the entire RAD OS system (WARNING: This will delete all files and reset the system!)")
            time.sleep(0.1)
            print("  debug install <package> - install a python package (WARNING: This will download and install a package from the internet!)")
            time.sleep(0.1)

    elif command == "debug reset": # this command resets all files.
        time.sleep(0.1)
        password = input("Enter debug password: ")
        if password == data["Password"]:
            time.sleep(0.1)
            confirm = input("Please enter debug password again for confirmation: ")
            if confirm == data["Password"]:
                shutil.rmtree()

                print("RAD OS system has been reset.")
            else:
                print("Reset cancelled.")
        else:
            print("Incorrect debug password.")

    elif command.startswith("debug install "): # this command install python libraries.
        password = input("Enter debug password: ")
        if password == password:
            package = command[14:].strip()
            if package:
                subprocess.run(['pip', 'install', package], check=True)
                print(f"Package {package} installed successfully.")
            else:
                print("No package specified.")
        else:
            print("Incorrect debug password.")

    elif command.startswith("python execute"): # this command executes a python script.
        filename = command[15:].strip()
        if filename:
            if os.path.exists(filename):
                subprocess.run(['python', filename], check=False)
            else:
                print(f"File '{filename}' not found.")
        else:
            print("No file specified.")

    else:
        print("Unknown command.")
