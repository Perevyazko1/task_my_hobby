from django.shortcuts import render


def home(request):
    """
    Представление из админ-панели, для рассылки новостей пользователям
    """

    return render(request, 'home.html')


def about_me(request):
    """
    Представление для отображения всех откликов на объявления пользователя
    """
    response = ''
    return render(request, 'about_me.html', {
        'responses': response})


def contacts(request):
    """
    Представление для отображения всех откликов на объявления пользователя
    """
    response = ''
    return render(request, 'contacts.html', {
        'responses': response})


