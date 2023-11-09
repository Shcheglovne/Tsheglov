# TODO Напишите функцию для поиска индекса товара
def poisk_index(list_tovarov, tovar):
    for i in range(0, len(list_tovarov)):
        if tovar == list_tovarov[i]:
            return i

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = poisk_index(items_list, find_item)  # TODO Вызовите функцию, чтобы получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
