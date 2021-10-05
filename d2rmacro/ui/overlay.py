# Import the required Libraries
from tkinter import *
from PIL import Image, ImageTk

from d2rmacro.config import MacroConfig
from d2rmacro.hotkeys.core import CoreHotkeyListener


class FlashableLabel(Label):
    def flash(self, count):
        bg = self.cget('background')
        fg = self.cget('foreground')
        self.configure(background=fg, foreground=bg)
        count += 1
        if (count < 2):
            self.after(1000, self.flash, count)


class D2ROverlay:
    def __init__(self, hotkeys: [MacroConfig]):
        self.skill_labels = []
        # Create an instance of Tkinter frame
        self.win = Tk()
        # Set the Geometry
        self.win.geometry("500x200")
        self.populate_ui(hotkeys)
        self.listener = CoreHotkeyListener(hotkeys)
        self.win.mainloop()

    def quit_win(self):
        self.win.destroy()

    def populate_ui(self, hotkeys: [MacroConfig]):
        self.win.attributes('-topmost', 1)
        self.win.update()
        self.win.wm_attributes("-transparentcolor", "black")
        self.win.configure(bg='')
        self.win.overrideredirect(1)
        # Create a Quit Button
        button = Button(self.win, text="x", command=self.quit_win, fg='yellow', bg='black')
        button.place(x=48 * len(hotkeys) + 30)
        # icons
        for idx, val in enumerate(hotkeys):
            self.show_img(idx, val.icon_path, val.hotkey)
            val.flash_fn=self.skill_labels[idx].flash

    def show_img(self, position: int, file_path: str, hotkey: str):
        size = 48
        load = Image.open(file_path)
        render = ImageTk.PhotoImage(load)
        img = FlashableLabel(self.win, image=render, text=hotkey, fg='yellow', compound='top', bg='black', justify='center',
                    font="Helvetica 12 bold")

        self.win.bind('<Button-1>', self.clickwin)
        self.win.bind('<B1-Motion>', self.dragwin)

        img.image = render
        img.place(x=size * position + 5, y=0)
        self.skill_labels.append(img)

    def dragwin(self, event):
        x = self.win.winfo_pointerx() - self.win._offsetx
        y = self.win.winfo_pointery() - self.win._offsety
        self.win.geometry('+{x}+{y}'.format(x=x, y=y))

    def clickwin(self, event):
        self.win._offsetx = event.x
        self.win._offsety = event.y

    def highlight_skill(self, idx):
        label = self.skill_labels[idx]
        label.flash(0)