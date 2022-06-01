import sys

# Название магазина (фильтр 2х)
# Название товара
# Стоимость

list_shop = []
spisok_new = []

while True:
    command = input('>>> ').lower()

    if command == 'exit':
        break 

    elif command == 'add':
        name_shop = input('Название магазина: ')
        name_prodyckt = input('Название товара: ')
        prise = input('Стоимость товара: ')        

        list_shop_new = {
        'name_shop': name_shop,
        'name_prodyckt': name_prodyckt,
        'prise': prise
        }

        list_shop.append(list_shop_new)

        if len(list_shop) > 1:
            list_shop.sort(key=lambda item: item.get('name_shop', ''))

    elif command == 'list':
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 6,
            '-' * 20,
            '-' * 30,
            '-' * 20
        )

        print(line)
        print(
            '| {:^6} | {:^20} | {:^30} | {:^20} | '.format(
                "№",
                "Название магазина",
                "Название товара",
                "Стоимость"
            )
        )
        print(line)

        for idx, spisok_new in enumerate(list_shop, 1):
            # print(spisok_new)
            print(
                '| {:>6} | {:<20} | {:<30} | {:<20} | '.format(
                    idx,
                    spisok_new.get('name_shop', ''),
                    spisok_new.get('name_prodyckt', ''),
                    spisok_new.get('prise', 0)
                )
            )

        print(line)


    elif command == 'prodyckt':
        shop_sear = input('Введите название товара: ')
        search_shop = []
        for shop_sear_itme in list_shop:
            if shop_sear == shop_sear_itme['name_prodyckt']:
                search_shop.append(shop_sear_itme)

        if len(search_shop) > 0:
            line_new = '+-{}-+-{}-+-{}-+-{}-+'.format(
                    '-' * 6,
                    '-' * 20,
                    '-' * 30,
                    '-' * 20
                )
            print(line_new)

            print(
                    '| {:^6} | {:^20} | {:^30} | {:^20} | '.format(
                        "№",
                        "Название магазина",
                        "Название товара",
                        "Стоимость"
                    )
                )
            print(line_new)

            for idx_new, spisok_new_new in enumerate(search_shop, 1):
                print(
                    '| {:>6} | {:<20} | {:<30} | {:<20} | '.format(
                        idx_new,
                        spisok_new_new.get('name_shop', ''),
                        spisok_new_new.get('name_prodyckt', ''),
                        spisok_new_new.get('prise', '')
                    )
                )

            print(line_new)
        else:
            print('Такого товара не найдено', file=sys.stderr)


    elif command == 'help':
        print('Список команд:\n')
        print('add - добавить магазин.')
        print('list - вывести список магазинов.')
        print('prodyckt <Название> - запросить информацию о товаре.')
        print('help - Справочник.')
        print('exit - Завершить пработу программы.')
    else:
        print(f'Команда <{command}> не существует.', file=sys.stderr)
        print('Введите <help> для просмотра доступных команд')