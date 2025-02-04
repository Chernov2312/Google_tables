from typing import List, Dict

from gspread import Client, Spreadsheet, Worksheet, service_account
import pandas as pd

table_link="https://docs.google.com/spreadsheets/d/1CLQU155YNMP9vm4XcMVW-TOy2udXRDJloegqEDcIfxI/edit?gid=0#gid=0"
table_link2="https://docs.google.com/spreadsheets/d/16Lnoux06Vue88Y2Arclbher3hg39fZ11FX3AJQTOhS4"
def client_init_json() -> Client:
    """Создание клиента для работы с Google Sheets."""
    return service_account(filename='wildberries-448712-3d49673f0fbe.json')


def get_table_by_url(client: Client, table_url):
    """Получение таблицы из Google Sheets по ссылке."""
    return client.open_by_url(table_url)



def get_worksheet_info(table: Spreadsheet) -> dict:
    """Возвращает количество листов в таблице и их названия."""
    worksheets = table.worksheets()
    worksheet_info = {
        "count": len(worksheets),
        "names": [worksheet.title for worksheet in worksheets]
    }
    return worksheet_info

def insert_one(table: Spreadsheet, title: str, data: list, index: int = 1):
    """Вставка данных в лист."""
    worksheet = table.worksheet(title)
    worksheet.insert_row(data, index=index)

def extract_data_from_sheet(table: Spreadsheet, sheet_name: str) -> List[Dict]:
    """
    Извлекает данные из указанного листа таблицы Google Sheets и возвращает список словарей.

    :param table: Объект таблицы Google Sheets (Spreadsheet).
    :param sheet_name: Название листа в таблице.
    :return: Список словарей, представляющих данные из таблицы.
    """
    worksheet = table.worksheet(sheet_name)
    rows = worksheet.get_all_records()
    return rows

if __name__ == '__main__':
    client = client_init_json()
    table = get_table_by_url(client, table_link)
    info = get_worksheet_info(table)
    insert_one(table=table,
               title=info['names'][0],
               data=['дилдов анатолий', 'горский 52', 'хуйзнает', '8800', '12,45', 'залупная', 'спермоприёмник'])
    print(extract_data_from_sheet(table, info['names'][0]))