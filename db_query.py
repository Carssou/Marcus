import sqlite3

new_connect = sqlite3.connect("marcus.db")
new_cursor = new_connect.cursor()

def show_result(bk="Livre I", cptr="Chapitre 2", lang="FR"):
# Get the data
    res = new_cursor.execute('''SELECT book, chapter, content FROM meditation 
                                WHERE book=? AND chapter=? AND language=?''', (bk, cptr, lang))
    # Print the data
    book, chapter, content = res.fetchone()
    
    if book is not None:
        return book, chapter, content
    else:
        return bk, cptr, lang

   

    
