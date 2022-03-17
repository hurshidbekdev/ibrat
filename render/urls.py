from django .urls import path
from .views import home
from .views import aloqa
from .views import yangiliklar
from .views import UzTarih
from .views import malumotlar
from .views import send



urlpatterns = [
    path('',home,name='home'),
    path('aloqa', aloqa, name='aloqa'),
    path('yangiliklar',yangiliklar,name='yangiliklar'),
    path('UzTarih', UzTarih, name='UzTarih'),
    path('malumotlar', malumotlar, name='malumotlar'),
    path('send/',send)

]