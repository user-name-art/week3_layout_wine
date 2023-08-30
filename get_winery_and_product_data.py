import datetime
import pandas
import collections


def get_winary_age():
    winery_founded_days = datetime.date.today() - datetime.date(year=1920, month=1, day=1)
    winery_age = winery_founded_days.days // 365

    return winery_age
    

def get_correct_winery_age(winery_age):
    template_age = 'лет'

    if (2 <= winery_age % 10 <= 4) and not (11<= winery_age <=14):
        template_age = 'года'
    elif (winery_age % 10 == 1) and not (winery_age == 11):
        template_age = 'год'

    return f'{winery_age} {template_age}'


def get_wines_from_file(filename):
    excel_data_df = pandas.read_excel(filename, keep_default_na=False)
    column_names = excel_data_df.columns.ravel()
    categories = excel_data_df[column_names[0]].tolist()
    wines = excel_data_df.to_dict(orient='records')

    wine_by_category = collections.defaultdict(list)

    for number, type_of_wine in enumerate(wines):
        wine = wine_by_category[categories[number]] 
        wine.append(type_of_wine)

    return wine_by_category    
