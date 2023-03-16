import sqlite3

new_connect = sqlite3.connect("marcus.db")
new_cursor = new_connect.cursor()

def show_result(bk="Livre I", cptr="Chapitre 2", lang="FR"):
# Get the data
    res = new_cursor.execute('''SELECT content FROM meditation 
                                WHERE book=? AND chapter=? AND language=?''', (bk, cptr, lang))
    # Print the data
    row = res.fetchone()
    
    if row is not None:
        return row[0]
    else:
        return bk, cptr, lang

    # close the connection
    new_cursor.close()
    new_connect.close()


