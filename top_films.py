import requests
from bs4 import BeautifulSoup
import json
import csv
import re
import time
import random

# --------------------------------------1
# url = "https://kinokrad.cc/"
#
# headers = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0"
# }
#
# count = 1
# while True:
#     try:
#         """Запрос на страницу"""
#         req = requests.get(url+f'page/{count}/', headers=headers)
#         src = req.text
#         """Проверка на существование"""
#         soup = BeautifulSoup(src, "lxml")
#         alert_block = soup.find(text=re.compile("По данному адресу публикаций на сайте не найдено, "
#                                                 "либо у вас нет доступа для просмотра информации по данному адресу."))
#         if alert_block is not None:
#             break
#
#         """Запись в файл"""
#         with open(f"data/page_{count}.html", "wb") as file:
#             file.write(src.encode())
#         print(f"page_{count}.html - created")
#         count += 1
#         time.sleep(random.randrange(2, 4))
#     except:
#         print('Ошибка!')
#         break

# --------------------------------------2
#
# count = 1
# while True:
#     films = []
#     """Считываем файл"""
#     if count == 1426:
#         break
#     with open(f"data/page_{count}.html", 'rb') as file:
#         src = file.read().decode()
#
#     soup = BeautifulSoup(src, "lxml")
#
#     all_films = soup.find_all("div", class_="shorbox")
#
#     for film in all_films:
#         try:
#             film_title = film.find("div", class_="postertitle").find('h2').find('a').text
#             if film_title == "Аполлон-10½: Приключение космического века":
#                 film_title = "Аполлон-10: Приключение космического века"
#             elif film_title == '37,2º утром':
#                 film_title = '37,2 градусов утром'
#             elif film_title == "Месть убийцы":
#                 film_title = "Месть убийцы"
#             elif film_title == '\u200bС 5 до 7. Время любовников':
#                 film_title = "С 5 до 7. Время любовников"
#         except:
#             film_title = "None"
#         try:
#             film_rating = film.find("div", class_="postertitle").find("li", class_="current-rating").text
#         except:
#             film_rating = "None"
#         try:
#             film_year = film.find("div", class_="godshort").find("span", class_="orange").text
#         except:
#             film_year = "None"
#         try:
#             film_janr = film.find("div", class_="godshort janr").find("span", class_="orange").find_all("a")
#             if not film_janr:
#                 film_janr = film.find("div", class_="godshort janr").find("span", class_="orange").text
#                 film_genre = film_janr
#             else:
#                 film_genre = film_janr[0].text
#                 for i in range(1, len(film_janr)):
#                     film_genre += f', {film_janr[i].text}'
#         except:
#             film_genre = "None"
#         films.append({
#             'title': film_title,
#             'genre': film_genre,
#             'year': film_year,
#             'rating': film_rating
#         })
#     print(f"page_{count}.html - processed")
#     # ! Запись словаря в json файл
#     # print(films)
#     with open(f"data/page_{count}.json", "w") as file:
#         json.dump(films, file, indent=4, ensure_ascii=False)
#         """Обнаружение ошибок кодировки"""
#         # j=1
#         # for elem in films:
#         #     json.dump(elem, file, indent=4, ensure_ascii=False)
#         #     print(j)
#         #     j+=1
#     count += 1

# --------------------------------------3
# count=1
# # ! Дозапись в csv файл
# with open(f"films.csv", "w", newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow(("Название",
#                     "Жанр",
#                     "Год",
#                     "Рейтинг"))
#     while True:
#         if count==1426:
#             break
#         # ! Считывание словаря из json файла
#         with open(f"data/page_{count}.json") as file:
#             films = json.load(file)
#             for film in films:
#                 writer.writerow((film["title"],
#                                 film["genre"],
#                                 film["year"],
#                                 film["rating"]))
#         print(f"page_{count}.json - processed")
#         count+=1
