from django.shortcuts import render

""" 
Этот код представляет собой набор функций, которые являются частью веб-приложения на базе фреймворка Django. 
Каждая функция отвечает за обработку HTTP-запросов к определенному URL-адресу и возвращает HTML-шаблон, 
соответствующий этой странице.

"""


def home_page(request):
    return render(request, 'home_page.html')

"""
Функция home_page обрабатывает запрос к главной странице сайта. Она принимает объект request, 
который содержит информацию о текущем HTTP-запросе, и возвращает ответ, рендерящий HTML-шаблон home_page.html.
"""

def portfolio(request):
    title = "Портфолио"
    return render(request, 'portfolio.html', {'title': title})


def architecture(request):
    title = "Архитектура"
    return render(request, 'architecture.html', {'title': title})


def improvement(request):
    title = "Благоустройство"
    return render(request, 'improvement.html', {'title': title})


def residential_interiors(request):
    title = "Жилые интерьеры"
    return render(request, 'residential_interiors.html', {'title': title})


def commercial_interiors(request):
    title = "Коммерческие интерьеры"
    return render(request, 'commercial_interiors.html', {'title': title})


def services(request):
    title = "Услуги"
    return render(request, 'services.html', {'title': title})


def contacts(request):
    title = "Контакты"
    return render(request, 'contacts.html', {'title': title})

"""
Они также принимают объект request и возвращают ответ, но дополнительно передают в контекст переменную title, 
которая используется в соответствующих HTML-шаблонах для отображения названия страницы.

Каждая из этих функций предназначена для обработки запросов к различным страницам сайта, 
таким как портфолио, архитектура, благоустройство, жилые и коммерческие интерьеры, услуги и контакты.

В целом, этот код реализует базовые маршруты для различных страниц веб-сайта, 
позволяя пользователям переходить между ними и просматривать соответствующую информацию.
"""