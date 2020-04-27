import tkinter as tk 
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

print("hello nangu")
 

win= tk.Tk()
win.title("Text Editor")
win.geometry('1200x800')

############################# MENU BAR ###################################################
#main menu
main_menu= tk.Menu(win)

#placing menus
file_menu=tk.Menu(main_menu, tearoff=0)
edit_menu=tk.Menu(main_menu, tearoff=0)
view_menu=tk.Menu(main_menu, tearoff=0)
color_theme_menu=tk.Menu(main_menu, tearoff=0)

#adding the menus to the menu bar
main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='Edit', menu=edit_menu)
main_menu.add_cascade(label='View', menu=view_menu)
main_menu.add_cascade(label='Color Theme', menu=color_theme_menu)

########## WORKING ON FILE MENU ############
#adding icons 
new_icon=tk.PhotoImage(file='ICONS/icons2/new.png')
open_icon=tk.PhotoImage(file='ICONS/icons2/open.png')
save_icon=tk.PhotoImage(file='ICONS/icons2/save.png')
saveas_icon=tk.PhotoImage(file='ICONS/icons2/save_as.png')
exit_icon=tk.PhotoImage(file='ICONS/icons2/exit.png')


########### WORKING ON EDIT MENU ###########
#adding icons
copy_icon=tk.PhotoImage(file='ICONS/icons2/copy.png')
paste_icon=tk.PhotoImage(file='ICONS/icons2/paste.png')
cut_icon=tk.PhotoImage(file='ICONS/icons2/cut.png')
clr_scr_icon=tk.PhotoImage(file='ICONS/icons2/clear_all.png')
find_icon=tk.PhotoImage(file='ICONS/icons2/find.png')


########### WORKING ON VIEW MENU ###########
#adding view menu icons
toolbar_icon=tk.PhotoImage(file='ICONS/icons2/tool_bar.png')
status_icon=tk.PhotoImage(file='ICONS/icons2/status_bar.png')


########### WORKING ON COLOR THEME MENU ###############
dark_icon=tk.PhotoImage(file='ICONS/icons2/dark.png')
red_icon=tk.PhotoImage(file='ICONS/icons2/red.png')
light_icon=tk.PhotoImage(file='ICONS/icons2/light_default.png')
monokai_icon=tk.PhotoImage(file='ICONS/icons2/monokai.png')
blue_icon=tk.PhotoImage(file='ICONS/icons2/night_blue.png')
lightplus_icon=tk.PhotoImage(file='ICONS/icons2/light_plus.png')

theme_choice=tk.StringVar()
color_icons=(dark_icon, red_icon, light_icon, monokai_icon, blue_icon, lightplus_icon)

color_dict={
    'Dark':('#f2e466','#24231f'),
    'Red':('#42c5d4','#bf1518'),
    'Light':('#000000','#ffffff'),
    'Monokai':('#485fcf','#ed7839'),
    'Blue':('#ebf9fa','#1f3f99'),
    'Light Plus':('#474747','#e0e0e0')
}

# adding color theme commands
def change_theme():
    choose_color=theme_choice.get()
    color_tuple=color_dict.get(choose_color)
    fg_color, bg_color=color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)

count=0
for i in color_dict:
    color_theme_menu.add_radiobutton(label=i, image=color_icons[count],variable=theme_choice, compound='left', command=change_theme)
    count+=1



##################################### TOOL BAR ################################################

tool_bar= ttk.Label(win)
tool_bar.pack(side=tk.TOP, fill=tk.X)

# fontstyle box
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box= ttk.Combobox(tool_bar, width=30, textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=1,column=0, padx=5)

# fontsize box
fontsize_var=tk.IntVar()
font_size= ttk.Combobox(tool_bar, width=15, textvariable=fontsize_var, state='readonly')
font_size['values']=tuple(range(8,80,2))
font_size.current(3)
font_size.grid(row=1, column=1, padx=5)

# Bold your text
bold_icon=tk.PhotoImage(file='ICONS/icons2/bold.png')
bold_button=ttk.Button(tool_bar, image=bold_icon)
bold_button.grid(row=1, column=2, padx=5)

# italic your text
italic_icon=tk.PhotoImage(file='ICONS/icons2/italic.png')
italic_button=ttk.Button(tool_bar, image=italic_icon)
italic_button.grid(row=1, column=3 , padx=5)

# underline your text
underline_icon=tk.PhotoImage(file='ICONS/icons2/underline.png')
underline_button=ttk.Button(tool_bar, image=underline_icon)
underline_button.grid(row=1, column=4, padx=5)

# font colour button
font_colour_icon=tk.PhotoImage(file='ICONS/icons2/font_color.png')
font_colour_button=ttk.Button(tool_bar, image=font_colour_icon)
font_colour_button.grid(row=1, column=5,padx=5)

# left align
lalign_icon=tk.PhotoImage(file='ICONS/icons2/align_left.png')
lalign_button=ttk.Button(tool_bar, image=lalign_icon)
lalign_button.grid(row=1, column=6, padx=5)

# centre align
calign_icon=tk.PhotoImage(file='ICONS/icons2/align_center.png')
calign_button=ttk.Button(tool_bar, image=calign_icon)
calign_button.grid(row=1, column=7, padx=5)

# right align
ralign_icon=tk.PhotoImage(file='ICONS/icons2/align_right.png')
ralign_button=ttk.Button(tool_bar, image=ralign_icon)
ralign_button.grid(row=1, column=8, padx=5)



##################################### TEXT EDITOR ####################################################

text_editor=tk.Text(win)
text_editor.config(wrap='word', relief=tk.FLAT)
text_editor.focus_set()

scroll_bar=tk.Scrollbar(win)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
scroll_bar.config(command=text_editor.yview)

text_editor.config(yscrollcommand=scroll_bar.set)
text_editor.pack(fill=tk.BOTH, expand=True)

# font size and font style functionality
current_font_family='Arial'
current_fontsize=14

def changefont(event=None):
    global current_font_family, current_fontsize
    current_font_family=font_family.get()
    current_fontsize=fontsize_var.get()
    text_editor.configure(font=(current_font_family,current_fontsize))

font_box.bind('<<ComboboxSelected>>',changefont)
font_size.bind('<<ComboboxSelected>>',changefont)
text_editor.configure(font=(current_font_family,current_fontsize))
## buttons functionality

# bold button functionality
def changebold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family,current_fontsize, 'bold')) 
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family,current_fontsize, 'normal'))

bold_button.configure(command=changebold)

# italics button functionality
def changeitalics():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family,current_fontsize, 'italic')) 
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family,current_fontsize, 'roman'))

italic_button.configure(command=changeitalics)

# underline button functionality
def underline_text():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family,current_fontsize, 'underline')) 
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family,current_fontsize, 'normal'))

underline_button.configure(command=underline_text)

# font color button functionality
def change_fontcolor():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_colour_button.configure(command=change_fontcolor)

### alignment functionality
# left align
def left_align():
    text_content=text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')
lalign_button.config(command=left_align)

# center align
def center_align():
    text_content=text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')
calign_button.config(command=center_align)

# right align
def right_align():
    text_content=text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')
ralign_button.config(command=right_align)
 

############################################### STATUS BAR ###########################################

status_bar=tk.Label(win, text='Status Bar')
status_bar.pack(side=tk.BOTTOM, fill=tk.Y)

text_changed=False
def change_text(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0, 'end-1c').split())
        charachters=len(text_editor.get(1.0,'end-1c'))
        lines=len(text_editor.get(1.0,'end').split('\n'))
        status_bar.config(text=f'Charachters : {charachters}   Words : {words}   Lines : {lines}')
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>", change_text)



######################################## MAIN MENU FUNCTIONALITY #############################################

############ FILE MENU ###################

# variable
url = ''

# new file functionality
def new_file(event=None):
    text_editor.delete(1.0, 'end')

# open file functionality
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(), title='Select a file', filetypes=(('Text File','*.txt'),('All Files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, 'end')
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    win.title(os.path.basename(url))

# save file functionality
def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0,tk.END))
            with open(url, 'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='*.txt', filetypes=(('Text File', '*.txt'),('All Files','*.*')))
            content=text_editor.get(1.0, 'end')
            url.write(content)
            url.close()
    except:
        return

# saveas file functionality
def saveas_file(event=None):
    global url
    try:
        content=text_editor.get(1.0,'end')
        url=filedialog.asksaveasfile(mode='w',defaultextension='*.txt', filetypes=(('Text File', '*.txt'),('All Files','*.*')))      
        url.write(content)
        url.close()
    except:
        return

# exit file functionality
def exit_file(event=None):
    global url, text_changed
    try:
        if url=='':
            mbox=tk.messagebox.askyesnocancel('Warning', 'Do you want to save your file?')
            if mbox ==True:
                saveas_file()
                win.destroy()
            elif mbox==False:
                win.destroy()
        elif url:
            if text_changed==True:
                mbox=tk.messagebox.askyesnocancel('Warning', 'Do you want to save changes to your file?')
                if mbox == True:
                    content=str(text_editor.get(1.0,tk.END))
                    with open(url, 'w',encoding='utf-8') as fw:
                        fw.write(content)
                        fw.close()
                    win.destroy()
                elif mbox==False:
                    win.destroy()
            else:
                win.destroy()
    except:
        return     

#adding file menu commands
file_menu.add_command(label='New', accelerator='Ctrl+N',image=new_icon, compound='left', command= new_file)
file_menu.add_command(label='Open', accelerator="Ctrl+O",image=open_icon,compound='left', command= open_file)
file_menu.add_command(label='Save', accelerator='Ctrl+S',image=save_icon,compound='left', command=save_file)
file_menu.add_command(label='Save As', accelerator='Ctrl+H',image=saveas_icon,compound='left', command=saveas_file)
file_menu.add_command(label='Exit', accelerator='Ctrl+Q',image=exit_icon,compound='left', command=exit_file)


########### EDIT MENU ###########

##### find functionality####

def find_and_replace(event=None):
    find_window = tk.Toplevel(win)
    find_window.title('Find and Replace')
    find_window.geometry('275x125+20+40')
    find_window.resizable(0,0)
    #labelframe
    find_label= ttk.LabelFrame(find_window, text='Find Replace')
    find_label.grid(row=5,column=10, padx=5, pady=5)
    #label
    findbox=ttk.Label(find_label, text='Find')
    findbox.grid(row=0,column=1, padx=5,pady=5)
    
    replacebox=ttk.Label(find_label, text='Replace')
    replacebox.grid(row=1,column=1, padx=5,pady=5)
    #entry box and variables
    find_var=tk.StringVar()
    find_entry=ttk.Entry(find_label,textvariable=find_var, width=20)
    find_entry.grid(row=0,column=2, padx=5,pady=5)
    
    replace_var=tk.StringVar()
    replace_entry=ttk.Entry(find_label,textvariable=replace_var, width=20)
    replace_entry.grid(row=1,column=2, padx=5, pady=5)
    #buttonn
    find_button=ttk.Button(find_label, text='Find')
    find_button.grid(row=4,column=1)
    
    replace_button=ttk.Button(find_label, text= 'Replace')
    replace_button.grid(row=4, column=2)

    def find_function():
        word=find_var.get()
        text_editor.tag_remove(word, 1.0, tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos} + {len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')

    def replace_function():
        word1=replace_var.get()
        word2=find_var.get()
        if word1 and word2:
            start_pos='1.0'
            try:
                while True:
                    start_pos=text_editor.search(word2, start_pos, stopindex=tk.END)
                    end_pos=f'{start_pos} + {len(word2)}c'
                    end_pos_replace=f'{start_pos} + {len(word1)}c'
                    text_editor.replace(start_pos,end_pos, word1)
                    start_pos=end_pos
            except:
                return        


    find_button.config(command=find_function)
    replace_button.config(command=replace_function)        

#adding edit menu commands
edit_menu.add_command(label='Copy', accelerator='Ctrl+C', image=copy_icon, compound='left', command= lambda: text_editor.event_generate('<Control c>') )
edit_menu.add_command(label='Paste', accelerator='Ctrl+V', image=paste_icon, compound='left', command= lambda: text_editor.event_generate('<Control v>'))
edit_menu.add_command(label='Cut', accelerator='Ctrl+X', image=cut_icon, compound='left', command= lambda: text_editor.event_generate('<Control x>'))
edit_menu.add_command(label='Clear Screen', accelerator='Ctrl+M', image=clr_scr_icon, compound='left', command= lambda: text_editor.delete(1.0, tk.END))
edit_menu.add_command(label='Find', accelerator='Ctrl+F', image=find_icon, compound='left', command=find_and_replace)



############### VIEW MENU ###########

# adding functionality
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbar(event=None):
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM,fill=tk.X)
        show_toolbar=True

def hide_statusbar(event=None):
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM,fill=tk.X)
        show_statusbar=True


#adding view menu commands
view_menu.add_checkbutton(label='Tool Bar',onvalue=True ,offvalue=False ,variable=show_toolbar, image=toolbar_icon, compound='left', command=hide_toolbar)
view_menu.add_checkbutton(label='Status Bar',onvalue=True ,offvalue=False ,variable=show_statusbar, image=status_icon, compound='left', command= hide_statusbar)


######### ADDING SHORTCUT KEYS ######
win.bind('<Control-n>', new_file )
win.bind('<Control-o>', open_file )
win.bind('<Control-s>', save_file )
win.bind('<Control-h>', saveas_file )
win.bind('<Control-q>', exit_file )
win.bind('<Control-f>', find_and_replace )

win.config(menu=main_menu)
win.mainloop()