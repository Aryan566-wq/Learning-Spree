# Importing necessary stuff for the Notepad
import tkinter as tk
from  tkinter import PhotoImage, ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os
from tkinter.constants import END

#---------------------------------------------------------------------------------------------------------------------

# The size, title etc  
main_application = tk.Tk()
main_application.geometry("1200x1000")
main_application.title('Google Classroom Clone Notepad')

main_menu = tk.Menu()

#---------------------------------------------------------------------------------------------------------------------

# File Icons and Menu Setup
new_icon = tk.PhotoImage(file = "icons/new_file.png")
open_icon = tk.PhotoImage(file = "icons/open-file.png")
save_icon = tk.PhotoImage(file = "icons/save_icon.png")
save_as_icon = tk.PhotoImage(file = "icons/save_as.png")
exit_icon = tk.PhotoImage(file = "icons/exit.png")

file = tk.Menu(main_menu,tearoff = False)

#---------------------------------------------------------------------------------------------------------------------

#Edit Menu Icons and Menu Setup
copy_icon = tk.PhotoImage(file = "icons/copy_icon.png")
paste_icon = tk.PhotoImage(file = "icons/paste_icon.png")
cut_icon = tk.PhotoImage(file = "icons/cut_icon.png")
clear_all_icon = tk.PhotoImage(file = "icons/clear_icon.png")
find_icon = tk.PhotoImage(file = "icons/find_icon.png")

edit = tk.Menu(main_menu, tearoff = False)

#------------------------------------------------------------------------------------------------------------

# View Menu Icons and Menu Setup
tool_bar = tk.PhotoImage(file = "icons/tool_bar.png")
status_bar = tk.PhotoImage(file = "icons/status_bar.png")

view = tk.Menu(main_menu,tearoff = False)

#------------------------------------------------------------------------------------------------------------

# Tool Bar configurations 
tool_bar_label = ttk.Label(main_application)
tool_bar_label.pack(side = tk.TOP,fill = tk.X)

#----------------------------------------------------------------------------------------------------------

# Font Style box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar_label,width = 30,textvariable = font_family,state = "readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row = 0, column = 0,padx = 5,pady = 5)

#----------------------------------------------------------------------------------------------------------

# Font Size box
size_variable = tk.IntVar()
font_size = ttk.Combobox(tool_bar_label,width = 20,textvariable = size_variable,state = "readonly")
font_size["values"] = tuple(range(8,100,2))
font_size.current(4)
font_size.grid(row = 0,column = 1,padx = 5)

#----------------------------------------------------------------------------------------------------------

# Bold Button
bold_icon = tk.PhotoImage(file = "icons/bold.png")
bold_btn = ttk.Button(tool_bar_label,image = bold_icon)
bold_btn.grid(row = 0,column = 2,padx = 5)

#----------------------------------------------------------------------------------------------------------

# Underline Button
underline_icon = tk.PhotoImage(file = "icons/underline.png")
underline_btn = ttk.Button(tool_bar_label,image = underline_icon)
underline_btn.grid(row = 0,column = 3,padx = 5)

#----------------------------------------------------------------------------------------------------------

# Italic Button
italic_icon = tk.PhotoImage(file = "icons/italic.png")
italic_btn = ttk.Button(tool_bar_label,image = italic_icon)
italic_btn.grid(row = 0,column = 4,padx = 5)

#----------------------------------------------------------------------------------------------------------

# Font Colour Button
font_colour_icon = tk.PhotoImage(file = "icons/Font-color-icon.png")
font_colour_btn = ttk.Button(tool_bar_label,image = font_colour_icon)
font_colour_btn.grid(row = 0,column = 5,padx = 5)

#----------------------------------------------------------------------------------------------------------

# Left Allignment Button
left_allignment_icon = tk.PhotoImage(file = "icons/left_align.png")
left_allignment_btn = ttk.Button(tool_bar_label,image = left_allignment_icon)
left_allignment_btn.grid(row = 0,column = 6,padx = 5)

#---------------------------------------------------------------------------------------------------------

# Center Allignment Button
center_allignment_icon = tk.PhotoImage(file = "icons/center_align.png")
center_allignment_btn = ttk.Button(tool_bar_label,image = center_allignment_icon)
center_allignment_btn.grid(row = 0,column = 7,padx = 5)

#---------------------------------------------------------------------------------------------------------

# Right Allignment Button
right_allignment_icon = tk.PhotoImage(file = "icons/right_align.png")
right_allignment_btn = ttk.Button(tool_bar_label,image = right_allignment_icon)
right_allignment_btn.grid(row = 0,column = 8,padx = 5)

#---------------------------------------------------------------------------------------------------------

# Text editor/Workspace
text_editor = tk.Text(main_application)
text_editor.config(wrap = "word",relief = tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side = tk.RIGHT,fill = tk.Y)
text_editor.pack(fill = tk.BOTH,expand = True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set)

#--------------------------------------------------------------------------------------------------------

# Font Family and size and it's functions
font_now = "Arial"
font_size_now = 16

def change_font(main_application):
    global font_now
    font_now = font_family.get()
    text_editor.configure(font = (font_now, font_size_now))

def change_size(main_application):
    global font_size_now
    font_size_now = size_variable.get()
    text_editor.configure(font = (font_now, font_size_now))
font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_size)

#-----------------------------------------------------------------------------------------------------

# Bold Function
print(tk.font.Font(font = text_editor["font"]).actual())

def bold_func():
    text_get = tk.font.Font(font=text_editor["font"])
    if text_get.actual()["weight"] == 'normal':
        text_editor.configure(font = (font_now,font_size_now,"bold"))
    if text_get.actual()["weight"] == 'bold':
        text_editor.configure(font = (font_now,font_size_now,"normal"))
bold_btn.configure(command = bold_func)

#----------------------------------------------------------------------------------------------------

# Italic Function
def Italic_func():
    text_get = tk.font.Font(font=text_editor["font"])
    if text_get.actual()["slant"] == 'roman':
        text_editor.configure(font = (font_now,font_size_now,"italic"))
    if text_get.actual()["slant"] == 'italic':
        text_editor.configure(font = (font_now,font_size_now,"roman"))
italic_btn.configure(command = Italic_func)

#----------------------------------------------------------------------------------------------------

# Underline Function
def under_line_func():
    text_get = tk.font.Font(font=text_editor["font"])
    if text_get.actual()["underline"] == 0:
        text_editor.configure(font = (font_now,font_size_now,"underline"))
    if text_get.actual()["underline"] == 1:
        text_editor.configure(font = (font_now,font_size_now,"normal"))
underline_btn.configure(command = under_line_func)

#---------------------------------------------------------------------------------------------------

# Colour Button Functions
def Colour_func():
    colour_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=colour_var[1])
font_colour_btn.configure(command = Colour_func)

#---------------------------------------------------------------------------------------------------

# Left Alignment Function
def left_alignment_func():
    text_get_all = text_editor.get(1.0,"end")
    text_editor.tag_config("left",justify= tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"left")
left_allignment_btn.config(command = left_alignment_func)

#---------------------------------------------------------------------------------------------------

# Center Alignment Function
def center_alignment_func():
    text_get_all = text_editor.get(1.0,"end")
    text_editor.tag_config("center",justify= tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"center")
center_allignment_btn.config(command = center_alignment_func)

#-------------------------------------------------------------------------------------------------------------------------------------------------

# Right Alignment Function
def right_alignment_func():
    text_get_all = text_editor.get(1.0,"end")
    text_editor.tag_config("right",justify= tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"right")
right_allignment_btn.config(command = right_alignment_func)

#------------------------------------------------------------------------------------------------------------------------------------------------


# Status Bar, word and character counter
status_bars = ttk.Label(main_application,text = "Status Bar")
status_bars.pack(side = tk.BOTTOM)

text_change = False

#------------------------------------------------------------------------------------------------------------------------------------------------

# Status Bar's Character and Word counter function
def change_word(event = None):
    global text_change
    if text_editor.edit_modified():
        text_change = True
        word = len(text_editor.get(1.0,"end-1c").split())
        character = len(text_editor.get(1.0,"end-1c").replace(" ",""))
        status_bars.config(text = f"character :{character} word :{word}")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>",change_word)

#------------------------------------------------------------------------------------------------------------------------------------------------

# Copy Function
edit.add_command(label = "Copy",image = copy_icon,compound = tk.LEFT, accelerator = "Ctrl+C",command = lambda:text_editor.event_generate("<Control c>"))
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Paste Function
edit.add_command(label = "Paste",image = paste_icon,compound = tk.LEFT, accelerator = "Ctrl+V",command = lambda:text_editor.event_generate("<Control v>"))
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Cut Function
edit.add_command(label = "Cut", image =  cut_icon,compound = tk.LEFT, accelerator = "Ctrll+X",command = lambda:text_editor.event_generate("<Control x>"))
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Clear All Function
edit.add_command(label = "Clear All", image = clear_all_icon, compound = tk.LEFT, accelerator = "Ctrl+",command = lambda:text_editor.delete(1.0,tk.END))
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Find & Replace Functions

def find_function(event = None):
    
    def find_func():
        word = find_input.get()
        text_editor.tag_remove("match","1.0",tk.END)
        matches = 0
        if word:
            start_position = "1.0"
            while True:
                start_position = text_editor.search(word,start_position,stopindex = tk.END)
                if not start_position:
                    break
                end_position = f"{start_position}+{len(word)}c"
                text_editor.tag_add("match",start_position,end_position)
                matches += 1
                start_position = end_position
                text_editor.tag_config('match',foreground= "black",background= "yellow")
    
    def replace_func():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    find_popup = tk.Toplevel()
    find_popup.geometry("450x200")
    find_popup.title("Find & Replace")
    find_popup.resizable(0,0)

    find_fram = ttk.Labelframe(find_popup,text = "Find & Replace")
    find_fram.pack(pady = 20)

    # Label
    text_find = ttk.Label(find_fram,text = "Find")
    text_replace = ttk.Label(find_fram,text = "Replace")

    # Entry Box
    find_input = ttk.Entry(find_fram,width = 30)
    replace_input = ttk.Entry(find_fram,width = 30)

    # Button
    find_button = ttk.Button(find_fram,text = "Find",command = find_func)
    replace_button = ttk.Button(find_fram,text = "Replace",command = replace_func)
    
    # Text Label Grid
    text_find.grid(row = 0, column = 0, padx = 4, pady = 4)
    text_replace.grid(row = 1, column = 0, padx = 4, pady = 4)

    # Entry Grid
    find_input.grid(row = 0, column = 1, padx = 4, pady = 4)
    replace_input.grid(row = 1, column = 1, padx = 4, pady = 4)

    # Button Grid
    find_button.grid(row = 2, column = 0, padx = 8, pady = 4)
    replace_button.grid(row = 2, column = 1, padx = 8, pady = 4)

edit.add_command(label = "Find",image = find_icon,compound = tk.LEFT, accelerator = "Ctrl+F",command = find_function)

#-----------------------------------------------------------------------------------------------------------------------------------------------

# File Menu buttons,Icons and Functions

text_URL = ""

#-----------------------------------------------------------------------------------------------------------------------------------------------

# New File Function

def new_file(event = None):
    global text_URL
    text_URL = ""
    text_editor.delete(1.0,tk.END)

file.add_command(label= "New", image = new_icon, compound = tk.LEFT, accelerator = "Ctrl+N",command = new_file)

#-----------------------------------------------------------------------------------------------------------------------------------------------

# Open File Function

def open_file(event = None):
    global text_URL
    text_URL = filedialog.askopenfilename(initialdir = os.getcwd(),title = "selectfile",filetypes = (("Text file","*txt"),("All files","*.*")))
    try:
        with open(text_URL, "r") as for_read:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,for_read.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(text_URL))

file.add_command(label= "Open", image = open_icon, compound = tk.LEFT, accelerator = "Ctrl+O",command = open_file)

#-----------------------------------------------------------------------------------------------------------------------------------------------

#Save File Function

def save_file(event = None):
    global text_URL
    try:
        if text_URL:
            content = str(text_editor.get(1.0,tk.END))
            with open(text_URL,"w",encoding="utf-8") as for_read:
                for_read.write(content)
        else:
            text_URL = filedialog.asksaveasfile(mode = "w",defaultextension = "txt",filetypes = (("Text File","*txt"),("All Files","*.*")))
            content2 = text_editor.get(1.0,tk.END)
            text_URL.write(content2)
            text_URL.close()
    except Exception as e:
        return



file.add_command(label= "Save", image = save_icon, compound = tk.LEFT, accelerator = "Ctrl+S",command = save_file)

#-----------------------------------------------------------------------------------------------------------------------------------------------

#Save as File fuction

def save_as_file(event = None):
    global text_URL
    try:
        content = text_editor.get(1.0,tk.END)
        text_URL = filedialog.asksaveasfile(mode = "w",defaultextension = "txt",filetypes = (("Text File","*txt"),("All Files","*.*")))
        text_URL.write(content)
        text_URL.close()
    except Exception as e:
        return

file.add_command(label= "Save as..", image = save_as_icon, compound = tk.LEFT, accelerator = "Ctrl+Alt+S",command = save_as_file)

#-----------------------------------------------------------------------------------------------------------------------------------------------

#Exit Function

def exit_function(event = None):
    global text_URL,text_change
    try:
        if text_change:
            mbox = messagebox.askyesnocancel("Warning!","Do you want to save this file?")
            if mbox is True:
                if text_URL:
                    content = text_editor.get(1.0,tk.END)
                    with open(text_URL,"w",encoding = "utf-8") as for_read:
                        for_read.write(content)
                        main_application.destroy()
                else:
                    content2 = text_editor.get(1.0,tk.END)
                    text_URL = filedialog.asksaveasfile(mode = "w",defaultextensions = "txt",filetypes = (("Text File","*txt"),("All Files","*.*")))
                    text_URL.write(content2)
                    text_URL.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

file.add_command(label= "Exit", image = exit_icon, compound = tk.LEFT, accelerator = "Ctrl+A+Delete",command = exit_function)

#--------------------------------------------------------------------------------------------------------------------------------------------------------\

# Status bar and Tool bar hide function
show_status_bar = tk.BooleanVar()
show_status_bar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar_func():
    global show_toolbar
    if show_toolbar:
        tool_bar_label.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bars.pack_forget()
        tool_bar_label.pack(side = tk.TOP,fill = tk.X)
        text_editor.pack(fill = tk.BOTH, expand = True)
        status_bars.pack(side = tk.BOTTOM)
        show_toolbar = True

def hide_status_bar_func():
    global show_status_bar
    if show_status_bar:
        status_bars.pack_forget()
        show_status_bar = False
    else:
        status_bars.pack(side = tk.BOTTOM)
        show_status_bar = True
        

view.add_checkbutton(label = "Tool Bar",onvalue = True,offvalue = 0,variable = show_toolbar,image = tool_bar,compound = tk.LEFT,command = hide_toolbar_func)
view.add_checkbutton(label = "Status Bar",onvalue = True,offvalue = 0,variable = show_status_bar,image = status_bar,compound = tk.LEFT,command = hide_status_bar_func)

#--------------------------------------------------------------------------------------------------------------------------------------------------------

# Main Menu Labels etc
main_menu.add_cascade(label = 'File',menu = file)
main_menu.add_cascade(label = 'Edit',menu = edit)
main_menu.add_cascade(label = 'View',menu = view)

#--------------------------------------------------------------------------------------------------------------------------------------------------------

main_application.config(menu=main_menu)

main_application.mainloop()

#------------------------------------------------------------------------------------------------
