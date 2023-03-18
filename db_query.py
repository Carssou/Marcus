import sqlite3
from random import randint

new_connect = sqlite3.connect("marcus.db")
new_cursor = new_connect.cursor()

def show_result(bk="Livre I", cptr="Chapitre "+str(randint(1,10)), lang="FR"):
# Get the data
    res = new_cursor.execute('''SELECT book, chapter, content FROM meditation 
                                WHERE book=? AND chapter=? AND language=?''', (bk, cptr, lang))
    # Print the data
    book, chapter, content = res.fetchone()
    
    if book is not None:
        return book, chapter, content
    else:
        return bk, cptr, lang
    
def dropdowns_options(bk="Livre I"):
    # Get the data
    res = new_cursor.execute('''SELECT chapter FROM meditation WHERE book=?''', (bk,))

    # Get a list of chapters
    chapters = [row[0] for row in res.fetchall()]
    
    return chapters
    

    
