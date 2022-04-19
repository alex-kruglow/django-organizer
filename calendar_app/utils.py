from datetime import datetime, timedelta

from .models import toDo


def getMonthByNum(num):
    '''
    This function returns name of month by gotten number.
    '''

    date = datetime(2000, int(num), 1)
    return date.strftime("%B")


def getNumDaysOfMonth(year, month):
    '''
    This function returns number of days by month.
    '''

    month = int(month)
    year = int(year)
    curMonth = datetime(year, month, 1)
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
    nextMonth = datetime(year, month, 1)
    return (nextMonth - curMonth).days


def genMonth(year, month, user, selectedDate=0):
    '''
    Params:
        - year
        - month
        - user
        - selectedDate
    It generates month. Month is an array with weeks.
    Weeks contains 7 days.
    Days is dict: date, active, contained, selected.
    '''

    # Generating start date and end date.
    refPoint = datetime(int(year), int(month), 1)
    startDate = refPoint
    monthSize = getNumDaysOfMonth(year, month)
    endDate = startDate + timedelta(days=monthSize)

    while (
        startDate.strftime("%a") != 'Mon'
    ):
        startDate -= timedelta(days=1)
    while (
        endDate.strftime("%a") != 'Sun'
    ):
        endDate += timedelta(days=1)

    # Generationg month object
    date = startDate
    weekDays = []
    monthWeeks = []
    while date <= endDate:
        dateToAdd = {}
        dateToAdd['date'] = date
        # Check if it is today.
        if date.strftime("%Y%m%d") == datetime.now().strftime("%Y%m%d"):
            dateToAdd['active'] = True
        else:
            dateToAdd['active'] = False

        # Check if a day contains events
        toDoForDay = toDo.objects.filter(
            link__year=str(dateToAdd['date'].strftime("%Y")),
            link__month=str(dateToAdd['date'].strftime("%m")),
            link__day=str(dateToAdd['date'].strftime("%d")),
            username=user
        )
        if toDoForDay:
            dateToAdd['contained'] = True
        else:
            dateToAdd['contained'] = False

        # Check if a day is selected
        if dateToAdd['date'] == selectedDate:
            dateToAdd['selected'] = True
        else:
            dateToAdd['selected'] = False

        # Checking that the day is in needed month.
        if dateToAdd['date'].strftime("%m") == refPoint.strftime("%m"):
            dateToAdd['disabled'] = False
        else:
            dateToAdd['disabled'] = True

        # If the day is Sunday put week in the month.
        if date.strftime("%a") != 'Sun':
            weekDays.append(dateToAdd)
        else:
            weekDays.append(dateToAdd)
            monthWeeks.append(weekDays)
            weekDays = []

        date += timedelta(days=1)
    return monthWeeks


def genNextPrevMonthLink(year, month):
    '''
    This function generates next and prev month links.
    It wants:
        - year
        - month
    It returns dict with nextMonthLink and prevMonthLink.
    '''

    if int(month) == 12:
        nextMonth = 1
        nextYear = int(year) + 1
    else:
        nextMonth = int(month) + 1
        nextYear = year
    nextMonthLink = '{}-{}'.format(str(nextYear), str(nextMonth))

    if int(month) == 1:
        nextMonth = 12
        nextYear = int(year) - 1
    else:
        nextMonth = int(month) - 1
        nextYear = year
    prevMonthLink = '{}-{}'.format(str(nextYear), str(nextMonth))
    return {'nextMonthLink': nextMonthLink, 'prevMonthLink': prevMonthLink}
