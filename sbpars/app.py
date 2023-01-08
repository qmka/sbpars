from bs4 import BeautifulSoup
import csv


def parser():
    # Формат: список транзакций, каждая транзакция - словарь
    # { 'shop': ... , 'date': ... , 'cost': ... , 'category': ... }
    result = []

    # Указываем, какой файл будем парсить
    with open('index.html', 'r') as f:
        file_to_parse = f.read()

    # Делаем суп
    soup = BeautifulSoup(file_to_parse, 'html.parser')
    soup.prettify()

    # title_tag = (soup.find('title'))
    # print(title_tag.text) ('td', {'class':'td-text td-text_bold'})

    trs = soup.find_all('div', {'class': 'trs_it'})

    for tr in trs:
        tr_data = tr.contents[0]

        # 1. Магазин
        tr_shop = tr_data.contents[0].text.strip()

        # 2. Дата транзакции (строка)
        tr_date = str(tr_data.contents[1].contents[1]['data-date'])

        # 3. Стоимость
        tr_cost_parent = tr_data.contents[2].contents[2].contents[0]
        tr_cost_head = str(tr_cost_parent.contents[0])
        tr_cost_tail = str(tr_cost_parent.contents[1].contents[0])
        tr_cost = tr_cost_head + tr_cost_tail

        # Нормализуем стоимость
        tr_cost = tr_cost.replace(',', '.')
        tr_cost = tr_cost.replace('\u202f', '')
        tr_cost_number = float(tr_cost)
        tr_cost = '{:.2f}'.format(tr_cost_number)

        # 4. Категория
        tr_cat = tr_data.contents[3].contents[1].contents[0].contents[0]

        result.append({
            'shop': tr_shop,
            'date': tr_date,
            'cost': tr_cost,
            'category': tr_cat
        })

    return result


def export_to_csv(parsed_data):

    f = open('transactions.csv', "w+")
    f.close()

    with open('transactions.csv', 'w', newline='') as csvfile:
        fieldnames = ['shop', 'date', 'cost', 'category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for tr in parsed_data:
            writer.writerow({
                'date': tr['date'],
                'category': tr['category'],
                'shop': tr['shop'],
                'cost': tr['cost']})
