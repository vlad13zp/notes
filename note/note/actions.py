import hashlib
import requests
import datetime
from note import tasks

BASE_DIR = 'http://localhost:8000'
AUTH = ('admin', 'pro100vlad')

"""
Make information for templates
"""


def make_info(id_user):
    context = {}
    context['tags'] = get_info_user('/tags/access/', id_user)
    context['colors'] = get_info_user(
        '/color/access/', id_user)
    context['categorys'] = get_info_user(
        '/cat/access/', id_user)
    context['users'] = get_all_user(
        '/user/', id_user)

    return context


"""
Actions with user (get/save)
"""


def get_user(hash_str):
    local_dir = BASE_DIR + '/user/' + str(hash_str)
    r = requests.get(local_dir, auth=AUTH)
    local_dict = r.json()

    if local_dict:
        return str(local_dict[0]['id'])
    else:
        return '-1'


def get_all_user(path, id_user):
    local_dir = BASE_DIR + path + str(id_user)
    r = requests.get(local_dir, auth=AUTH)
    local_dict = r.json()

    return local_dict


def get_info_user(path, id_user):
    local_dir = BASE_DIR + path + str(id_user)
    r = requests.get(local_dir, auth=AUTH)
    local_dict = r.json()

    return local_dict


def save_new_user(email, password):
    hash_str = str(email) + \
        str(password)
    hsh = hashlib.md5()
    # Double md5 coding
    hsh.update(hash_str)
    hash_str = hsh.hexdigest()
    hsh.update(hash_str)
    hash_str = hsh.hexdigest()

    local_dict = {'email': email, 'password': hash_str}

    local_dir = BASE_DIR + '/user/add/'
    r = requests.post(
        local_dir, auth=AUTH, data=local_dict)

    tasks.send_mail(email)

    return r.status_code

"""
Actions with tags/color/category (save)
"""


def save_new_tag(tag_name, id_user):
    local_dir = BASE_DIR + '/tags/'
    local_dict = {'tag_name': tag_name, 'access': id_user}
    r = requests.post(local_dir, auth=AUTH, data=local_dict)

    return r.status_code


def save_new_color(color_name, hex, id_user):
    local_dir = BASE_DIR + '/color/'
    local_dict = {'color_name': color_name, 'hex_stat': hex, 'access': id_user}
    r = requests.post(local_dir, auth=AUTH, data=local_dict)

    return r.status_code


def save_new_cat(cat_name, id_user):
    local_dir = BASE_DIR + '/cat/'
    local_dict = {'category_name': cat_name, 'access': id_user}
    r = requests.post(local_dir, auth=AUTH, data=local_dict)

    return r.status_code

"""
Actions with note (get,save,update,delete)
"""


def get_notes_user(id_user):
    local_dir = BASE_DIR + '/note/' + str(id_user)
    r = requests.get(local_dir, auth=AUTH)
    local_dict = r.json()

    local_dict.reverse()

    return local_dict


def get_notes_cat(id_cat, id_user):
    local_dir = BASE_DIR + '/note/cat/' + str(id_user) + '/' + str(id_cat)
    r = requests.get(local_dir, auth=AUTH)
    local_dict = r.json()

    return local_dict


def get_notes_edit(id_note):
    local_dir = BASE_DIR + '/note/del/' + str(id_note)
    print local_dir
    r = requests.get(local_dir, auth=AUTH)
    local_dict = r.json()

    return local_dict

# Save


def save_sub_note(id_user, subject, message):
    local_dict = {
        'id_user': id_user,
        'subject': subject, 'message': message}

    return local_dict


def save_color_note(id_color, id_cat):
    time = datetime.datetime.now()
    local_dict = {'date_create': str(time),
                  'id_color': id_color,
                  'id_category': id_cat}

    return local_dict


def save_new_note(tags, file_name, colors, sub):
    local_dict = {
        'id_tag': tags}
    local_dict.update(colors)
    local_dict.update(sub)

    local_dir = BASE_DIR + '/note/add/'
    r = requests.post(
        local_dir, auth=AUTH, data=local_dict, files={'files': file_name})

    return r.status_code

# Update, Delete


def delete_note(id_note):
    local_dir = BASE_DIR + '/note/del/' + str(id_note)
    r = requests.delete(local_dir, auth=AUTH)

    return r.status_code


def update_note(id_note, tags, file_name, colors, sub):
    local_dict = {
        'id_tag': tags}
    local_dict.update(colors)
    local_dict.update(sub)

    local_dir = BASE_DIR + '/note/del/' + str(id_note)
    r = requests.put(
        local_dir, auth=AUTH, data=local_dict, files={'files': file_name})

    return r.status_code

"""
Help make password with double md5
"""


def make_hash(hash_str):
    hsh = hashlib.md5()
    # Double md5 coding
    hsh.update(hash_str)
    hash_str = hsh.hexdigest()
    hsh.update(hash_str)
    hash_str = hsh.hexdigest()

    return hash_str


def get_hash(username, password):
    hash_str = make_hash(str(username) +
                         str(password))

    return hash_str
