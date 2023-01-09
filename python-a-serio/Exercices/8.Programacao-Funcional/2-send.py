# def shorten(string_list):
#     length = len(string_list[0])
    
#     for s in string_list:
#         length = yield s[:length]


# my_string_list = ['loremipsum', 'dolorsit', 'ametfoobar']
# short_string_list = shorten(my_string_list)
# result = []

# try:
#     s = next(short_string_list)
#     result.append(s)
#     while True:
#         number_of_vowels = len(filter(lambda letter: letter in 'aeiou', s))
#         s = short_string_list.send(number_of_vowels)
#         result.append(s)
# except StopIteration:
#     pass


def shorten(string_list):
    length = len(string_list)
    for s in string_list:
        length = yield s[:length]

mystringlist = ['loremipsum', 'dolorsit', 'ametfoobar']
shortstringlist = shorten(mystringlist)
result = []

try:
    s = next(shortstringlist)
    result.append(s)
    while True:
        number_of_vowels = len(filter(lambda letter: letter in 'aeiou', s))
        # Trunca a próxima string dependendo
        # do número de vogais da string anterior
        s = shortstringlist.send(number_of_vowels)
        result.append(s)
except StopIteration:
    pass

