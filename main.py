from pprint import pprint
import os


def read_file(doc):
    with open(doc, 'r', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish = line.strip()
            cook_book[dish] = []
            for _ in range(int(file.readline())):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                cook_book[dish].append({'ingredient_name': ingredient_name,
                                        'quantity': int(quantity),
                                        'measure': measure.strip()})
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, doc):
    result = {}
    for dish in dishes:
        if dish in read_file(doc):
            for i in read_file(doc)[dish]:
                if i['ingredient_name'] in result:
                    result[i['inrgedient_name']]['quantity'] += i['quantity'] * person_count
                else:
                    result[i['ingredient_name']] = {'measure': i['measure'], 'quantity': (i['quantity'] * person_count)}
        else:
            print('Dish is not correct!!!')
    return result


def number_lines_in_file(file):
    with open(file, 'r', encoding='utf-8') as fp:
        lines = len(fp.readlines())
        return f'{lines}'


def merging_files_in_one(files):
    all_files = [files for files in os.listdir(dirname) if files.endswith('.txt')]
    result = {}
    sorted_list = []
    for doc in all_files:
        result[doc] = int(number_lines_in_file(doc))
        sorted_files = sorted(result.items(), key=lambda item: item[1])
    for j in sorted_files:
        sorted_list.append(j[0])
    with open('result.txt', 'w', encoding='utf-8') as fs:
        for file in sorted_list:
            fs.write(f'{file}\n')
            fs.write(f'{number_lines_in_file(file)}\n')
            with open(file, 'r', encoding='utf-8') as f:
                counting = 1
                for i in f:
                    fs.write(f'строка номер {counting} в файле {file}: {i}')
                    counting += 1
                    fs.write('\n')
    return f'Файл создан'


dirname = r'C:\Users\ivanh\Desktop\Project11'
print(merging_files_in_one(dirname))
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Утка по-пекински'], 2, 'recipes.txt'))
pprint(read_file('recipes.txt'))