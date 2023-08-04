from django import template


register = template.Library()


word_list = ['редиска', 'режим', 'союз', 'библиотека', 'засуха']


@register.filter()
def censor(value):

    def check_word(word):
        for j in range(0, len(word_list)):
            if word.lower() == word_list[j]:
                # есть совпадение - цензурируем!
                new_word = word[0]
                for k in range(1, len(word)):
                    new_word += '*'
                word = new_word
        return word

    if type(value) != str:
        return 'Ошибка: "value" не строка!'

    s = ''
    i = 0
    new_word = ''

    while i < len(value):
        c = value[i]
        if (c != ' ') and (c != '.') and (c != ',') and (c != '!') and (c != '?') and (c != ' '):
            new_word += c
        else:
            # print('new_word='+new_word)
            if new_word != '':
                s = s + check_word(new_word) + c
                new_word = ''
            else:
                s += c
        i += 1
    if new_word != '':
        s = s + check_word(new_word)
    return s
