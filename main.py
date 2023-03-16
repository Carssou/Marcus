import tkinter as tk
from tkinter import ttk, messagebox
from random import randint
import db_query


def update_text(label, result):
    """
    Update the label with a random quotes.

    If the list of quotes is empty, update the label telling so
    """
    result = db_query.show_result(cptr="Chapitre "+str(randint(1,10)))
    if result:
        # If the quote file is read by the previous function, set the label to the text of random quote
        label.config(text=result)
    else:
        label.config(text='No quotes found.')

def create_ui(root, result):
    """
    Creates the user interface
    """
    root.geometry('650x800')
    root.config(background='#c6c5ef')
    root.title('Marcus')
    root.resizable(False, False)
    root.iconbitmap('iconTest-150x150.ico')
    
    

    """"""
    # Create tabs for quotes and journaling
    tabs = ttk.Notebook(root)
    text_tab = ttk.Frame(tabs)
    favorite_tab = ttk.Frame(tabs)
    tabs.add(text_tab, text='Pensées pour moi-même')
    tabs.add(favorite_tab, text='Favoris')
    tabs.pack(expand=True, fill='both')

    # Add title to the app
    title = tk.Label(root,text='Marcus Alpha ver 0.01',
                     font=('Verdana',10),
                     bg='#c6c5ef')
    title.pack(expand=False, fill='both')

    # Add text label
    text_label = tk.Label(text_tab, font=('Verdana',15),
                           bg='#c6c5ef', wraplength=550)
    text_label.pack(expand=True, fill='both')

    # Update the label with a random quote
    update_text(text_label, result)

    #  Add a button to request another quote
    text_button = tk.Button(text_tab, text='Autre paragraphe',
                             command=(lambda: update_text(text_label, result)),
                             font=('Arial', 15), bg='#c6c5ef')
    text_button.pack()

    favorite_label = tk.Label(favorite_tab, text='Journal placeholder',
                             font=('Verdana',20,'bold', 'italic'),
                             bg='#c6c5ef', pady=50, padx=20)
    
    favorite_label.pack(expand=True, fill='both')

    """
    Create the top menu for the user interface
    """
    top_menu = tk.Menu(root)
    root.config(menu=top_menu)

    file_menu = tk.Menu(top_menu)

    file_menu.add_separator()
    file_menu.add_command(label='New quote', command=lambda: update_quote(quote_label, quotes))
    file_menu.add_command(label='Exit', command=root.destroy)

    sub_menu = tk.Menu(file_menu)
    sub_menu.add_command(label='Display')
    file_menu.add_cascade(label='Preferences', menu=sub_menu)

    top_menu.add_cascade(label='File', menu=file_menu)

    help_menu = tk.Menu(top_menu)
    help_menu.add_command(label='About', command=lambda: messagebox.showinfo('About', 'Motivation Alpha ver 0.01'))
    top_menu.add_cascade(label='Help', menu=help_menu)


def main():
    """
    Mendatory function to create the window, also define the quotes file path
    """
    result = db_query.show_result(cptr="Chapitre "+str(randint(1,10)))
#    quotes = read_quotes('/Users/ludo/PythonScripts/citations.txt')
    root = tk.Tk()
    create_ui(root, result)
    root.mainloop()

# Check if the main function is called by the script and not by a module
if __name__ == "__main__":
    main()