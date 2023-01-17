from django.shortcuts import render


def home(request):
    """
    Представление, для главной страницы.
    """
    return render(request, 'home.html')


def about_me(request):
    """
    Представление, страницы о себе.
    """
    response = ''
    return render(request, 'about_me.html', {
        'responses': response})


def contacts(request):
    """
    Представление, страницы контактов.
    """
    response = ''
    return render(request, 'contacts.html', {
        'responses': response})
