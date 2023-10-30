numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

index_propusk = 4 #индекс пропущенного элелмента
avarage = ( sum( numbers[:index_propusk] ) + sum( numbers[index_propusk+1:] ) )/ (len(numbers))
numbers[index_propusk] = avarage

print("Измененный список:", numbers)
