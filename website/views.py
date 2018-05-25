from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate, login, logout

from .models import Book


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'website/index.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.order_by('id')


class DetailView(generic.DetailView):
    model = Book
    template_name = 'website/book.html'


@login_required
def add(request):
    book = Book()
    context = {'book': book, 'errors': []}

    if request.POST:
        try:
            save(book, request.POST)
            return HttpResponseRedirect(reverse('website:index'))
        except (KeyError, ValueError) as e:
            context['errors'] = e

    return render(request, 'website/form.html', context)


@login_required
def edit(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {'errors': []}
    if request.POST:
        try:
            save(book, request.POST)
            context['success'] = True
        except (KeyError, ValueError) as e:
            context['errors'] = e

    context['book'] = book
    return render(request, 'website/form.html', context)


@login_required
def delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return HttpResponseRedirect(reverse('website:index'))


def login_view(request):
    context = {}

    if request.user.is_authenticated:
        return redirect(reverse('website:index'))

    if request.POST:
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('website:index'))
        else:
            context['errors'] = True
    return render(request, 'website/auth/login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('website:index'))


def register(request):
    context = {}

    if request.user.is_authenticated:
        return redirect(reverse('website:index'))

    if request.POST:
        try:
            print("df")
        except:
            print("")
    return render(request, 'website/auth/register.html', context)


def register_confirmation(request):
    context = {}
    if request.user.is_authenticated:
        return redirect(reverse('website:index'))
    return render(request, 'website/register_confirm.html', context)


@login_required
def profile(request):
    context = {}
    return render(request, 'website/auth/profile.html', context)


def save(book, data):
    book.title = data['title']
    book.author = data['author']
    book.isbn = data['isbn']
    book.print_year = data['print_year']
    book.description = data['description']
    book.save()
    return True


def example(request, question_id):
    # template = loader.get_template('website/index.html')
    # raise Http404("Question does not exist")
    # question = get_object_or_404(Question, pk=question_id)
    return HttpResponse("this IS example view" % question_id)
