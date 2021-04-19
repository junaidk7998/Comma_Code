spam = ['apples', 'bananas', 'tofu', 'cats']
crypto = ['bitcoin', 'etherium', 'dogecoin', 'safemoon']

# function
def commaCode(lst):

    # empty string
    s = '' 
    last = lst[len(lst) - 1]
    length = int(len(lst)) - 1
    new_lst = lst[0:length]

    for words in new_lst:
        s += words + ', '
    print(s + 'and ' + last)

commaCode(spam)
commaCode(crypto)