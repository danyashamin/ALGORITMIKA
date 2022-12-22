import json

with open('file_j.json', 'w') as f_cur:
    need_dict = {1:"1", 2:"2"}
    json.dump(need_dict, f_cur)
    f_cur.close()