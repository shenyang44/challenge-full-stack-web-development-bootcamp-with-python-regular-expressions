import re

my_string = 'how are you'
my_regex = r'[aeiou]'

print(re.sub(my_regex,  '*', my_string))


# # Challenge 4
def hide_serial(string):
    print(re.sub(r'\d', 'X', string, 8))


hide_serial("123456-12-1234")   # XXXXXX-XX-1234


def hide_digits(string):
    print(re.sub(r'\d', '-', string))


hide_digits("You have 100 dollars")


def hide_last_four(string):
    print(re.sub(r'\d{4}', '****', string))


hide_last_four("12-34-5678, 90-80-7012, 45-65-1234")
# 12-34-****, 90-80-****, 45-65-****


# Challenge 5
def has_id(string):
    if re.search(r'\d{6}-\d{2}-\d{4}', string) == None:
        return 'false'
    else:
        return 'true'

        # Output
print(has_id("please don't share this: 890414-14-1422"))   # true
print(has_id("please confirm your identity: 234-122-1422"))  # false


def grab_id(string):
    my_id = re.search(r'\d{6}-\d{2}-\d{4}', string)

    if my_id == None:
        return 'Nil'
    else:
        return my_id.group()


print(grab_id("please don't share this: 890414-14-1422"))   # 890414-14-1422
print(grab_id("please confirm your identity: XXX-XX-1422"))  # nil


# Task 3
def grab_all_ids(string):
    my_id = re.search(r'\d{6}-\d{2}-\d{4}.+', string)
    id_array = []
    if my_id == None:
        return id_array
    else:
        id_array = my_id.group().split(', ')
        return id_array


# ["890414-14-1422", "900515-14-1092", "950616-12-5414"]
print(grab_all_ids("890414-14-1422, 900515-14-1092, 950616-12-5414"))
print(grab_all_ids("please confirm your identity: XXX-XX-1422"))  # []


# Task 4
def hide_all_ids(string):
    my_id = re.search(r'\d{6}-\d{2}-\d{4}.+', string)
    if my_id == None:
        return string
    else:
        return(re.sub(r'\d{6}-\d{2}-', 'XXXX-XX-', string))

# # !START! Next 6 lines is old code that I realised is long winded
# #        new_list = []
# #       id_array = my_id.group().split(', ')
# #       print(id_array)
# #        for id in id_array:
# #           new_list.append(re.sub(r'\d', 'X', id, 8))
# #        return ', '.join(new_list)
# # !END!


print(hide_all_ids("890414-14-1422, 900515-14-1092, 950616-12-5414"))
# XXXXXX-XX-1422, XXXXXX-XX-1092, XXXXXX-XX-5414
# please confirm your identity: XXX-XX-1422
print(hide_all_ids("please confirm your identity: XXX-XX-1422"))


# # Task 5

def format_ids(string):
    regex_5 = r'(\d{6})\W*(\d{2})\W*(\d{4})'
    return re.sub(regex_5, r"\1-\2-\3", string)


print(format_ids("890414.14.1422, 900515141092, 950616-12-5414"))
# 890414-14-1422, 900515-14-1092, 950616-12-5414
# please confirm your identity: 763158-58-1422
print(format_ids("please confirm your identity: 763158581422"))
