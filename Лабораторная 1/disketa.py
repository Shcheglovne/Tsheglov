# TODO Найдите количество книг, которое можно разместить на дискете

V_disk = 1.44 * 1024 * 1024
num_pages = 100
num_str = 50
num_symb = 25
V_symb = 4
V_knigi = num_pages * num_str * num_symb * V_symb
num_knig = V_disk // V_knigi

print("Количество книг, помещающихся на дискету:", int(num_knig) )
