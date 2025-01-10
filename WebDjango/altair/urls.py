from django.urls import path
from .views import *


"""
Данный код определяет маршруты (URL-адреса) для веб-приложения на основе фреймворка Django. 
Он создает соответствие между конкретными URL-путями и функциями-обработчиками (представлениями), 
которые будут вызываться при обращении к этим путям.
Импорт модулей:
- Импортируется функция path из модуля django.urls, которая используется для определения маршрутов.
- Также импортируются все функции из файла views.py текущего приложения (с помощью *), 
чтобы они были доступны для привязки к маршрутам.

"""

urlpatterns = [
    path('', home_page, name='home_page'),
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio/architecture/', architecture, name='architecture'),
    path('portfolio/improvement/', improvement, name='improvement'),
    path('portfolio/residential_interiors/', residential_interiors, name='residential_interiors'),
    path('portfolio/commercial_interiors/', commercial_interiors, name='commercial_interiors'),
    path('services/', services, name='services'),
    path('contacts/', contacts, name='contacts'),

]

"""
Этот фрагмент кода создает список маршрутов, определяющих, какие функции должны выполняться при доступе к определенным URL-адресам:
   
   - Если пользователь перейдет на корневой путь (''), будет вызвана функция home_page, соответствующая главной странице сайта.
   - Путь /portfolio/ вызывает функцию portfolio, отвечающую за страницу портфолио.
   - Аналогично, пути /portfolio/architecture/, /portfolio/improvement/, /portfolio/residential_interiors/, 
   /portfolio/commercial_interiors/ вызывают соответствующие функции для отображения информации об архитектуре, 
   благоустройстве, жилых интерьерах и коммерческих интерьерах соответственно.
   - Путь /services/ запускает функцию services, показывающую страницу услуг.
   - Наконец, путь /contacts/ открывает контактную форму, обработанную функцией contacts.

Каждый маршрут имеет имя (например, name='home_page'), которое позволяет ссылаться на него внутри
других частей проекта, таких как шаблоны или другие представления.
"""