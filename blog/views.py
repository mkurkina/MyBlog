from django.shortcuts import render


def main_page(request):
    context = {
        'title': 'Главная страница блога',
        'description': 'Добро пожаловать в мой блог!',
        'posts': [
            {
                'title': 'Дизайн в современном мире',
                'preview': 'Дизайн — это не только красота, но и удобство.',
            },
        ],
    }
    return render(request, 'index.html', context)


def about_page(request):
    context = {
        'title': 'О блоге',
    }
    return render(request, 'about.html', context)


def post_page(request):
    context = {
        'title': 'Дизайн в современном мире',
    }
    return render(request, 'post.html', context)
