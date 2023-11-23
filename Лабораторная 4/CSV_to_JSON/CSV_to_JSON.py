# TODO импортировать необходимые молули

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
      # TODO считать содержимое csv файла

      with open(INPUT_FILENAME, 'r') as input_cvs:
          reader = csv.DictReader(input_cvs)
          dict_row = []
          with open(OUTPUT_FILENAME, 'w') as output_json:
              for row in reader:
                  dict_row.append(dict(row))

      # TODO Сериализовать в файл с отступами равными 4

              json.dump(dict_row, output_json, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
