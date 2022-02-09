import re

def solution(new_id):
    id = re.sub('[^a-z\d\-\_\.]', '', new_id.lower())
    id = re.sub('\.\.+', '.', id)
    id = re.sub('^\.|\.$', '', id)
    id = 'a' if id == '' else id
    id = re.sub('\.$', '', id[:15])
    if len(id) < 3:
        while True:
            id += id[-1]
            if len(id) == 3: break

    return id