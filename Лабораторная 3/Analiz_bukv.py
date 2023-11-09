# TODO  Напишите функцию count_letters

def count_letters(stroka):
    dictionary_letters = {}
    list_slov = stroka.split()
    list_slov_sploshnoy = ''.join(list_slov) #преобразование списка слов в сплошной текст без пробелов
    stroka_nizniy_registr = list_slov_sploshnoy.lower() # преобразование всех символов в нижний регистр
    unique_letters = list(set(stroka_nizniy_registr)) # уникальные символы
    n = 0 #счетчик
    for i in range(0, len(unique_letters)):
        if unique_letters[i].isalpha(): #Проверка, является ли символ буквой
            for j in range(0, len(stroka_nizniy_registr)):
                if stroka_nizniy_registr[j] == unique_letters[i]:
                    n += 1
            dictionary_letters[unique_letters[i]] = n #заполнение словаря
            n = 0 #обнуление счетчика после записи количества одной буквы

    return dictionary_letters

# TODO Напишите функцию calculate_frequency

def calculate_frequency(dictionary_letters):
    count_uniq_letter = list(dictionary_letters.items())
    summa = 0
    for i in range(0,len(count_uniq_letter)):
        summa += count_uniq_letter[i][1]
    new_dictionary = {}
    for i in range(0, len(count_uniq_letter)):
        f = round(count_uniq_letter[i][1] / summa, 2)
        new_dictionary[count_uniq_letter[i][0]] = f

    return new_dictionary

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

count = count_letters(main_str)
calculate = list(calculate_frequency(count).items())
for i in range(0, len(calculate)):
    print(f'{calculate[i][0]}: {calculate[i][1]}')
