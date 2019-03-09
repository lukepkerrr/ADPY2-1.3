import datetime


def logger(path):
    def decorator(old_func):
        def new_func(*args, **kwargs):
            returned = old_func(*args, **kwargs)
            log = '=====\nДата и время:\n{}\nИмя функции:\n{}\nАргументы:\n{}\nВозвращаемое значение:\n{}\n'.format(datetime.datetime.now(), old_func.__name__, args, returned)
            with open(path, 'a', encoding='utf8') as file:
                file.write(log)
            return returned
        return new_func
    return decorator

#Старое дз
#-------------------------------------------------
@logger('logs.txt')
def make_new_cook_book(file):
    with open(file) as recipes:
        splitted = recipes.read().split('\n\n')

    new_cook_book = {}

    fully_splitted = []
    for dish in splitted:
        fully_splitted.append(dish.split('\n'))

    for dish in fully_splitted:
        ingridients = []
        i = 2
        while i < len(dish):
            splitted_dish = dish[i].split(' | ')
            ingridient = {'ingridient_name': splitted_dish[0], 'quantity': splitted_dish[1], 'measure': splitted_dish[2]}
            ingridients.append(ingridient)
            i += 1
        new_cook_book.update({dish[0]: ingridients})

    return new_cook_book

@logger('logs.txt')
def get_shop_list_by_dishes(dishes, person_count, book):
    cook_book = book

    shop_list = {}

    for dish in dishes:
        for ingridient in cook_book[dish]:
            if ingridient['ingridient_name'] in shop_list:
                new_quantity = shop_list[ingridient['ingridient_name']]['quantity'] + (int(ingridient['quantity']) * person_count)
                shop_list[ingridient['ingridient_name']]['quantity'] = new_quantity
            else:
                shop_list.update({ingridient['ingridient_name']: {'measure': ingridient['measure'], 'quantity': int(ingridient['quantity']) * person_count}})

    return shop_list

@logger('logs.txt')
def test():
    print('Вызов тестовой функции')
    cook_book = make_new_cook_book('recipes.txt')
    test_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2, cook_book)
    # for ingr in test_list:
    #     print('{} - {} {}'.format(ingr, test_list[ingr]['quantity'], test_list[ingr]['measure']))
#-------------------------------------------------
#Для наглядности
@logger('logs.txt')
def multiplier(first_arg, second_arg):
    return first_arg * second_arg

test()
multiplier(3, 5)