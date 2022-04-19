from django.urls import path
from .views import calendar_page, month_page, day_page, add_event, del_event

urlpatterns = [
    path('calendar/', calendar_page, name='calendar_page'),
    path('month/<int:year>-<int:month>/', month_page, name='month_page'),
    path('day/<int:year>-<int:month>-<int:day>/', day_page, name='day_page'),
    path('add_event/', add_event, name="add_event"),
    path('del_event/<int:id>/', del_event, name="del_event"),
]
