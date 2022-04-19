from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import toDo
from .forms import toDoForm
from .utils import getMonthByNum, genMonth, genNextPrevMonthLink


@login_required
def calendar_page(request, year=0, month=0, day=0):
    '''
    The main page of the app.
    It waits:
        - year
        - month
        - day
    All params are not necessary.
    If something is skipped it tries to use session or gets current day.
    '''

    if year == 0:
        try:
            year = request.session['cur_year']
        except KeyError:
            year = datetime.now().strftime("%Y")
    if month == 0:
        try:
            month = request.session['cur_month']
        except KeyError:
            month = datetime.now().strftime("%m")
    if day == 0:
        try:
            day = request.session['cur_day']
        except KeyError:
            day = datetime.now().strftime("%d")

    return HttpResponseRedirect('/day/{}-{}-{}/'.format(year, month, day))


@login_required
def month_page(request, year, month):
    '''
    This function return page with month by month only.
    It waits:
        - year
        - month
    Both params are mandatory.
    '''

    nextPrevMonthLink = genNextPrevMonthLink(year, month)

    toDoList = toDo.objects.filter(
        link__year=year,
        link__month=month,
        username=request.user,
    )
    selectedDate = 0

    monthContent = genMonth(year, month, request.user, selectedDate)

    request.session['cur_year'] = year
    request.session['cur_month'] = month
    request.session['cur_day'] = ''

    context = {
        'nextMonthLink': nextPrevMonthLink['nextMonthLink'],
        'prevMonthLink': nextPrevMonthLink['prevMonthLink'],
        'monthContent': monthContent,
        'toDoList': toDoList,
        'year': year,
        'monthName': getMonthByNum(month),
        'month': month,
        'today': datetime.now(),
    }
    return render(request, 'calendar_app/calendar_page.html', context)


@login_required
def day_page(request, year, month, day):
    '''
    This function returns month by date.
    It waits:
        - year
        - month
        - day
    It generates month content and list of toDo.
    '''

    nextPrevMonthLink = genNextPrevMonthLink(year, month)

    toDoList = toDo.objects.filter(
        link__year=year,
        link__month=month,
        link__day=day,
        username=request.user,
    )
    selectedDate = datetime(int(year), int(month), int(day))

    monthContent = genMonth(year, month, request.user, selectedDate)

    request.session['cur_year'] = year
    request.session['cur_month'] = month
    request.session['cur_day'] = day

    form = toDoForm()

    context = {
        'nextMonthLink': nextPrevMonthLink['nextMonthLink'],
        'prevMonthLink': nextPrevMonthLink['prevMonthLink'],
        'monthContent': monthContent,
        'toDoList': toDoList,
        'year': year,
        'monthName': getMonthByNum(month),
        'month': month,
        'selectedDate': selectedDate,
        'today': datetime.now(),
        'form': form,
    }
    return render(request, 'calendar_app/calendar_page.html', context)


@login_required
def add_event(request):
    '''
    This function creates new toDo item.
    It waits data from the frontend.
    '''

    if request.method == 'POST':
        form = toDoForm(request.POST)
        if form.is_valid():
            newEvent = form.save(commit=False)
            year = request.session['cur_year']
            month = request.session['cur_month']
            day = request.session['cur_day']
            newEvent.link = datetime(year, month, day)
            newEvent.username = request.user
            newEvent.save()
        return HttpResponseRedirect('/day/{}-{}-{}/'.format(year, month, day))
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')


@login_required
def del_event(request, id):
    '''
    This function deletes toDo item by id.
    It waits:
        -id (from url)
    '''

    event = toDo.objects.get(id=id)
    # Return 404 if something wrong and toDo owner and logged user is no
    # the same.
    if event.username != request.user:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    year = event.link.strftime("%Y")
    month = event.link.strftime("%m")
    day = event.link.strftime("%d")
    # Does nothing if event owner is not the logged in user.
    if event.username != request.user:
        return HttpResponseRedirect('/day/{}-{}-{}/'.format(year, month, day))
    event.delete()
    return HttpResponseRedirect('/day/{}-{}-{}/'.format(year, month, day))
