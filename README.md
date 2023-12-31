# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

Скачайте код
```
https://github.com/user-name-art/week3_layout_wine.git
```
При необходимости создайте виртуальное окружение. Например: 
```
python -m venv .venv
``` 
Установите зависимости:
```
pip install -r requirements.txt
``` 
Запустите сайт:
```
python3 main.py
```
Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

Для отображения информации о напитках понадобится файл **.env** (смотри **.env.template** для примера). 
* **WINE_FILENAME** должна содержать название файла с данными типа **.xlsx**. По умолчанию используется **wine3.xlsx**.
  
Структура файла в качестве примера:
![wine](https://github.com/user-name-art/week3_layout_wine/assets/112713337/01532806-7aa0-42b4-9891-8e4b23c6875b)

Допускается произвольное название всех столбцов, при этом группировка напитков по группам будет производиться согласно данным из первого столбца.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
