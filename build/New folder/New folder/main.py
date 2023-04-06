import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry('1200x600')
main_application.title('A_pad Text Editor')

#  ----------------------------------------- Main_Menu -------------------------------------------------
#  ----------------------------------------End Main Menu -----------------------------------------------


# File Icons

new_icon = tk.PhotoImage(file="icons2/new.png")
open_icon = tk.PhotoImage(file="icons2/open.png")
save_icon = tk.PhotoImage(file="icons2/save.png")
save_as_icon = tk.PhotoImage(file="icons2/save_as.png")
exit_icon = tk.PhotoImage(file="icons2/exit.png")

# Edit Icons

copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')

# View icon
tool_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_icon = tk.PhotoImage(file='icons2/status_bar.png')

# Color Theme Icon

light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')


def func():
    pass


menubar = tk.Menu(main_application)

# Create Menus Option
file_menu = tk.Menu(menubar, tearoff=False)
Edit_Menu = tk.Menu(menubar, tearoff=False)
view_menu = tk.Menu(menubar, tearoff=False)
colorTheme_Menu = tk.Menu(menubar, tearoff=False)

theme_choice = tk.StringVar()
color_icon = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Default': ('#000000', '#ffffff'),
    'Light Plus': ('#474747', '#e0e0e0'),
    'Dark': ('#c4c4c4', '#2d2d2d'),
    'Monokai': ('#d3b774', '#474747'),
    'Night_Blue': ('#ededed', '#6b9dc2')
}
# Cascading:

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label='Edit', menu=Edit_Menu)
menubar.add_cascade(label='View', menu=view_menu)
menubar.add_cascade(label='ColorTheme', menu=colorTheme_Menu)

# -----------------------------------------End Main Menu ----------------------------------------------
#  -----------------------------------------------Tool_Bar  -------------------------------------------
tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

font_tuples = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box.grid(row=0, column=0, padx=5)
font_box['values'] = font_tuples
font_box.current(font_tuples.index('Arial'))

# Size Box:

size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable=size_var, state='readonly')
font_size['values'] = tuple(range(8, 80))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)

# Bold Button

bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

# Italic Button

italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

# Underline Button

underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

# font Color Button

color = tk.PhotoImage(file='icons2/font_color.png')
color_btn = ttk.Button(tool_bar, image=color)
color_btn.grid(row=0, column=5, padx=5)

# Align

align_left = tk.PhotoImage(file='icons2/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left)
align_left_btn.grid(row=0, column=6, padx=5)

align_center = tk.PhotoImage(file='icons2/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center)
align_center_btn.grid(row=0, column=7, padx=5)

align_right = tk.PhotoImage(file='icons2/align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right)
align_right_btn.grid(row=0, column=8, padx=5)

# -----------------------------------------End Tool Bar ----------------------------------------------

# -----------------------------------------------Text Editor ------------------------------------------
text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)

# Scroll Bar
scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# Font Family and FOnt Size Functionality:

current_font_family = 'Arial'
current_font_size = 12


def Change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))


def Change_font_size(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", Change_font)
font_size.bind("<<ComboboxSelected>>", Change_font_size)


# Buttons Functionality

# Bold Button Functionality

def change_bold(event=None):
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))


bold_btn.configure(command=change_bold)


# Italic Button Functionality

def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'roman'))


italic_btn.configure(command=change_italic)


# Underline Functionality

def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))


underline_btn.configure(command=change_underline)


# Font Color Functionality:

def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


color_btn.configure(command=change_font_color)


# Align Functionality:

def Align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')


align_left_btn.configure(command=Align_left)


def Align_Center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')


align_center_btn.configure(command=Align_Center)


def Align_Right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')


align_right_btn.configure(command=Align_Right)

text_editor.configure(font=('Arial', 12))

# -----------------------------------------End Text Editor -------------------------------------------

#  ---------------------------------------- Main Status Bar  ----------------------------------------------
status_bar = ttk.Label(main_application, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

# Status Bar Functionality

text_changed = False


def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f"Character:{characters} Words: {words}")
    text_editor.edit_modified(False)


text_editor.bind("<<Modified>>", changed)

# ------------------------------------------End Status Bar -----------------------------------------------

# -------------------------------------- Main Menu Functionality ---------------------------------------
url = ""


def new_file(event=None):
    global url
    url = ""
    text_editor.delete(1.0, tk.END)


# File Commands
file_menu.add_command(label='New', command=new_file, image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N')


# Open Functionality:


def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File',
                                     filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))


file_menu.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O', command=open_file)


# Save File Functionality:

def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1, 0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'),
                                                                                         ('All Files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return


file_menu.add_command(label='Save', command=save_file, image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S')


def save_as_file(event=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'),
                                                                                     ('All Files', '*.*')))
        url.write(content)
        url.close()
    except:
        return


file_menu.add_command(label='Save as', command=save_as_file, image=save_as_icon, compound=tk.LEFT,
                      accelerator='Ctrl+alt+S')


# Exit Functionality:


def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            m_box = messagebox.askyesnocancel('Warning', 'Do you Want to save the File ?')
            if m_box is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'),
                                                                                                 ('All Files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif m_box is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return


file_menu.add_command(label='Exit', command=exit_func, image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q')

# Edit Commands

Edit_Menu.add_command(label='Copy', command=lambda: text_editor.event_generate("<Control c>"), image=copy_icon,
                      compound=tk.LEFT, accelerator='Ctrl+C')
Edit_Menu.add_command(label='Paste', command=lambda: text_editor.event_generate("<Control v>"), image=paste_icon,
                      compound=tk.LEFT, accelerator='Ctrl+V')
Edit_Menu.add_command(label='Cut', command=lambda: text_editor.event_generate("<Control x>"), image=new_icon,
                      compound=tk.LEFT, accelerator='Ctrl+X')
Edit_Menu.add_command(label='Clear_all', command=lambda: text_editor.delete(1.0, tk.END), image=clear_all_icon,
                      compound=tk.LEFT, accelerator='Ctrl+Alt+X')


# Find Functionality:

def find_fun(event=None):
    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos} + {len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('250x250+200+100')
    find_dialogue.title('Find')
    find_dialogue.resizable(0, 0)

    # # Frame
    find_frame = ttk.LabelFrame(find_dialogue)
    find_frame.pack(pady=20)

    # Creating Label:
    text_find_label = ttk.Label(find_frame, text='Find')
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    # Creating Entry:

    find_input = ttk.Entry(find_frame, width=13)
    find_input.grid(row=0, column=1, padx=4, pady=4)
    # Button

    find_button = ttk.Button(find_frame, text='Find', command=find)
    find_button.grid(row=2, columnspan=2, padx=8, pady=4)

    find_dialogue.mainloop()


Edit_Menu.add_command(label='Find', command=find_fun, image=find_icon,
                      compound=tk.LEFT, accelerator='Ctrl+F')

# View Checks Buttons

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)


def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        text_editor.pack(side=tk.TOP)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True


view_menu.add_checkbutton(label="Tool Bar", onvalue=True, offvalue=False, variable=show_toolbar, image=tool_icon,
                          compound=tk.LEFT,
                          accelerator='Ctrl+N', command=hide_toolbar)
view_menu.add_checkbutton(label="Status Bar", onvalue=True, offvalue=False, variabl=show_statusbar, image=status_icon,
                          compound=tk.LEFT,
                          accelerator='Ctrl+N', command=hide_statusbar)


# Color Theme Radio buttons

def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(foreground=fg_color, background=bg_color)


theme_choice = tk.StringVar()
count = 0
for i in color_dict:
    colorTheme_Menu.add_radiobutton(label=i, image=color_icon[count], compound=tk.LEFT, variable=theme_choice,
                                    command=change_theme)
    count = count + 1

# -----------------------------------------End Main Menu ----------------------------------------------
main_application.config(menu=menubar)

# Bind ShortCut Key:
main_application.bind('<Control-n>', new_file)
main_application.bind('<Control-o>', open_file)
main_application.bind('<Control-s>', save_file)
main_application.bind('<Control-Alt-s>', save_as_file)
main_application.bind('<Control-q>', exit_func)
main_application.bind('<Control-f>', find_fun)

main_application.mainloop()