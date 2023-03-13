import tkinter as tk
from tkinter import ttk, messagebox
from random import randint
import db_connect

def read_quotes(file_path):
    """
    Read the file provided in the root function

    returns:
        A list of quotes from the file or an empty list if there is an error
    """
    try: # will try to open the file
        with open(file_path, 'r') as f:
            quotes = f.readlines()
        return quotes
    except Exception as e:
        # If error, print the error message
        print(f'An error occured while reading the quotes file: {e}')
        return []

def update_quote(label, quotes):
    """
    Update the label with a random quotes.

    If the list of quotes is empty, update the label telling so
    """
    if quotes:
        # If the quote file is read by the previous function, set the label to the text of random quote
        label.config(text=quotes[randint(0, len(quotes) - 1)])
    else:
        label.config(text='No quotes found.')

def create_ui(root, quotes):
    """
    Creates the user interface
    """
    root.geometry('800x300')
    root.config(background='#c6c5ef')
    root.title('Motivation')
    root.resizable(False, False)
    root.iconbitmap('iconTest-150x150.ico')
    
    

    """"""
    # Create tabs for quotes and journaling
    tabs = ttk.Notebook(root)
    quotes_tab = ttk.Frame(tabs)
    journal_tab = ttk.Frame(tabs)
    tabs.add(quotes_tab, text='Quotes')
    tabs.add(journal_tab, text='Journal')
    tabs.pack(expand=True, fill='both')

    # Add title to the app
    title = tk.Label(root,text='Motivation Alpha ver 0.01',
                     font=('Verdana',30,'bold'),
                     bg='#c6c5ef')
    title.pack(expand=True, fill='both')

    # Add quote label
    quote_label = tk.Label(quotes_tab, font=('Verdana',15,'bold'),
                           bg='#c6c5ef', wraplength=600)
    quote_label.pack(expand=True, fill='both')

    # Update the label with a random quote
    update_quote(quote_label, quotes)

    #  Add a button to request another quote
    quote_button = tk.Button(quotes_tab, text='Another quote',
                             command=(lambda: update_quote(quote_label, quotes)),
                             font=('Arial', 15), bg='#c6c5ef')
    quote_button.pack()

    # Add the journal label
    journal_label = tk.Label(journal_tab, text='Journal placeholder',
                             font=('Verdana',20,'bold', 'italic'),
                             bg='#c6c5ef', pady=50, padx=20)
    journal_label.pack(expand=True, fill='both')

    # ADD TEXT WIDGET FOR JOURNALING/THOUGHT INPUT
    journal_entry = tk.Text(journal_tab)
    journal_entry.pack(fill='both', expand=True)

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
    quotes = read_quotes('/Users/ludo/PythonScripts/citations.txt')
    root = tk.Tk()
    create_ui(root, quotes)
    root.mainloop()

# Check if the main function is called by the script and not by a module
if __name__ == "__main__":
    main()