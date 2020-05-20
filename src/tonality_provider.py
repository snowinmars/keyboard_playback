tonalities = {
    'c_major': [0,2,4,5,7,9,11]
}


def get(id):
    if id in tonalities:
        return tonalities[id]
    else:
        return None
