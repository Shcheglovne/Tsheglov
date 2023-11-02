users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

statistika = {
    "Общее количество" : 0,
    "Уникальные посещения" : 0
}
statistika["Общее количество"] = len(users)
statistika ["Уникальные посещения"] = len(set(users))

print(statistika)
