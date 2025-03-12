def to_jaden_case(string):
    string_1 = string
    list_1 = string_1.split(' ')
    list_2 = []
    for x in list_1:
        list_2.append(x.capitalize())
    return ' '.join(list_2)
