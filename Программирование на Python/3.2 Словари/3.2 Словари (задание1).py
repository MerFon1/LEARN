vdv = {}


def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif 2 * key in d:
        d[2 * key] += [value]
    else:
        d[2 * key] = [value]

update_dictionary(vdv,1,-1)
update_dictionary(vdv,1,-2)
print(vdv)