import tkinter as tk
import pyautogui
import threading

class AutoClickerApp:
    def __init__(self, master):
        self.master = master
        master.title("Auto Clicker")

        self.label = tk.Label(master, text="Choose Action (Mouse / Keyboard)")
        self.label.pack()

        self.label = tk.Label(master, text="If you use keyboard please enter key you want to auto.")
        self.label.pack()

        self.action_entry = tk.Entry(master)
        self.action_entry.pack()

        self.click_button = tk.Button(master, text="Start Action", command=self.start_action)
        self.click_button.pack()

        self.stop_button = tk.Button(master, text="Stop Action", command=self.stop_action, state=tk.DISABLED)
        self.stop_button.pack()

        self.is_acting = False
        self.action_thread = None

    def start_action(self):
        action = self.action_entry.get().lower()
        if action not in ['mouse', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            self.label.config(text="Invalid input.")
            return

        self.label.config(text="Choose Action (mouse/keyboard):")

        self.is_acting = True
        self.click_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.action_thread = threading.Thread(target=self.perform_action, args=(action,))
        self.action_thread.start()

    def stop_action(self):
        self.is_acting = False
        self.click_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def perform_action(self, action):
        while self.is_acting:
            if action == 'mouse':
                pyautogui.click()
            elif action == 'a':
                pyautogui.press('a')
            elif action == 'b':
                pyautogui.press('b')
            elif action == 'c':
                pyautogui.press('c')
            elif action == 'd':
                pyautogui.press('d')
            elif action == 'e':
                pyautogui.press('e')
            elif action == 'f':
                pyautogui.press('f')
            elif action == 'g':
                pyautogui.press('g')
            elif action == 'h':
                pyautogui.press('h')
            elif action == 'i':
                pyautogui.press('i')
            elif action == 'j':
                pyautogui.press('j')
            elif action == 'k':
                pyautogui.press('k')
            elif action == 'l':
                pyautogui.press('l')
            elif action == 'm':
                pyautogui.press('m')
            elif action == 'n':
                pyautogui.press('n')
            elif action == 'o':
                pyautogui.press('o')
            elif action == 'p':
                pyautogui.press('p')
            elif action == 'q':
                pyautogui.press('q')
            elif action == 'r':
                pyautogui.press('r')
            elif action == 's':
                pyautogui.press('s')
            elif action == 't':
                pyautogui.press('t')
            elif action == 'u':
                pyautogui.press('u')
            elif action == 'v':
                pyautogui.press('v')
            elif action == 'w':
                pyautogui.press('w')
            elif action == 'x':
                pyautogui.press('x')
            elif action == 'y':
                pyautogui.press('y')
            elif action == 'z':
                pyautogui.press('z')


def main():
    root = tk.Tk()
    app = AutoClickerApp(root)
    
    # Set the size of the window
    window_width = 300
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)
    root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))
    
    root.mainloop()

if __name__ == "__main__":
    main()