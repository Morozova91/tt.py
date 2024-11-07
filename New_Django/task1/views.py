# Задача "Время объединять", все данные из task4 модуля urbanProject
# все представления
# представления из task5
from django.core import paginator
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
#
# from .models import Buyer, Game
# from .forms import UserRegister
from .models import Post
from django.core.paginator import Paginator


# Create your views here.
def post_list(request):
    post_list = Post.objects.all().order_by('-created_at')
    paginator = Paginator(post_list, 3)  # 3 поста на странице

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'post_list.html', {'posts': posts, 'paginator': paginator})
# def platform(request):
#     return render(request, 'platform.html')
#
# def cart(request):
#     return render(request, 'cart.html')
#
# def menu(request):
#     games = Game.objects.all()
#
#     return render(request, 'games.html', {'games':games})
#
#
#
# # Create your views here.
# def sign_up_by_django(request):
#     users = Buyer.objects.all()
#     info = {}
#     if request.method == 'POST':
#         form = UserRegister(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             repeat_password = form.cleaned_data['repeat_password']
#             age = form.cleaned_data['age']
#             if password == repeat_password and int(age) >= 18 and username not in users:
#                 Buyer.objects.create(name=username, balance=800.0, age=age)
#                 return HttpResponse(f"Приветствуем, {username}!")
#             if username in users:
#                 info['error'] = 'Пользователь уже существует'
#             elif age < 18:
#                 info['error'] = 'Вы должны быть старше 18'
#             elif password != repeat_password:
#                 info['error'] = 'Пароли не совпадают'
#
#
#
#     return render(request, 'registration_page.html', info)


