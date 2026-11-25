from django.shortcuts import render
from django.shortcuts import redirect
from .models import Review
from .forms import ReviewForm


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

def reviews_page(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewForm()

    reviews = Review.objects.filter(is_checked=True)

    context = {
        'title': 'Книга отзывов',
        'form': form,
        'reviews': reviews,
    }

    return render(request, 'reviews.html', context)