#!/usr/bin/python3
def best_score(my_dict):
    if my_dict & len(my_dict):
        max_score = list(my_dict.keys())[0]
        for keys in my_dict:
            if my_dict[keys] > my_dict[max_score]:
                max_score = keys
        return max_score
    return None
