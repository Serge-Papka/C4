import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree

# # создадим объект ElementTree. Он возвращается функцией parse()
# tree = etree.parse('Welcome to Python.org.html',
#                    lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью html-парсера. Сам html - это то, что мы скачали и поместили в папку из браузера.
#
# ul = tree.findall(
#     '/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li')  # помещаем в аргумент метода findall скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)
#
# # создаём цикл, в котором мы будем выводить название каждого элемента из списка
# for li in ul:
#     a = li.find(
#         'a')  # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>. Т. е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью. (Гиперссылки в html это всегда тег <a>)
#     print(a.text)  # из этого тега забираем текст, это и будет нашим названием

'''
Используя полученные знания, допишите, чтобы он показывал ещё и дату добавления новости.
Примечание: для получения атрибутов тега (т. е. его дополнительных параметров) используется метод .get(<имя атрибута>).
'''
import requests  # импортируем наш знакомый модуль
# import lxml.html
# from lxml import etree

html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта python
# print(html,5454)

# создадим объект ElementTree. Он возвращается функцией parse()
tree = etree.parse('Welcome to Python.org.html',
                   lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью html парсера
# print(777, tree)

ul = tree.findall(
    'body/div/div[3]/div/section/div[3]/div[1]/div/ul/li')  # помещаем в аргумент методу findall скопированный xpath

# создаём цикл в котором мы будем выводить название каждого элемента из списка
for li in ul:
    print(777)
    a = li.find('a')  # в каждом элементе находим где хранится название. У нас это тег <a>
    time = li.find('time')
    print(time.get('datetime'), a.text)  # из этого тега забираем текст - это и будет нашим названием






# ------------------------
'''# Напишите программу, которая будет с помощью парсера lxml доставать текст из тега tag2 следующего HTML:
<html>
 <head> <title> Some title </title> </head>
 <body>
  <tag1> some text
     <tag2> MY TEXT </tag2>
   </tag1>
 </body>
</html>'''

# import lxml.html
html = ''' <html>
 <head> <title> Some title </title> </head>
 <body>
  <tag1> some text
     <tag2> MY TEXT </tag2>
   </tag1>
 </body>
</html>
'''
tree = lxml.html.document_fromstring(html)

text = tree.xpath('/html/body/tag1/tag2/text()')

print(text)
