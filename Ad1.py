import urllib, urllib.request
from datetime import datetime


def get_data(province_id):  # Отримання тестових даних із WEB-сторінки
    url = 'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?country=UKR&provinceID={}&year1=1981&year2=2020&type=Mean'.format(province_id)

    # Відкриття WEB-сторінки можна зробити наступним чином:
    webpage = urllib.request.urlopen(url)
    text = webpage.read()

    # Отримати поточну дату і час
    now = datetime.now()
    # Згенерувати строку з поточою датою і часом та необхідним форматуванням можна за допомогою методу strftime
    date_and_time_time = now.strftime("%d.%m.%Y_%H^%M^%S")

    # Створити новий файл за допомоги функції open
    out = open('D:\\AD\\' + 'NOAA_ID' + str(province_id) + '-' + date_and_time_time + '.csv', 'wb')
    # Після відкриття у змінній text міститься текст із WEB-сторінки, який тепер можна записати у файл
    out.write(text)
    out.close()

import pandas as pd



def make_header(filepath):
    headers = ['Year', 'Week', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI', 'empty']
    dataframe = pd.read_csv(filepath, header=1, names=headers)
    dataframe.drop(dataframe.loc[dataframe['VHI'] == -1].index)
    return dataframe


