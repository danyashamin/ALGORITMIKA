with open('my_file_2.txt', 'rw') as f_cur:
    text = f_cur.read()
    text+='new_text'
    f_cur.write(text)