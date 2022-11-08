import re # импорт модуля регулярных выражений


def hashtags(text): # функция для печати всех хэштегов
    regex = "#(\w+)" # регулярное выражение

    hashtag_list = re.findall(regex, text) # убираем хэштеги

    print("The hashtags in \"" + text + "\" are :")  # печать списка хэштегов
    for hashtag in hashtag_list:
        print(hashtag)


if __name__ == "__main__":
    text = "#Проверка #работы программы"
    hashtags(text)



