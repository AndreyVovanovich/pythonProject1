from django.shortcuts import render
from django.http import HttpResponseRedirect
from manage import cursor
from .forms import NameForm
from .models import SearchingUsers


# Create your views here.

def get_name(request):
    print('Получен метод запроса: ', request.method)
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            print('Введеное значение: ', form.cleaned_data['user_name'])

            SearchingUsers.ByName = form.cleaned_data['user_name']
            return HttpResponseRedirect('user/search')
        else:
            print('Form is not valid')
        return render(request, 'users/index.html', {'form': form})

    #Запрос данных из БД

def user_by_name(request):
    print('Получили: ', SearchingUsers.ByName)
    substring = '%'+ SearchingUsers.ByName + '%'
    sql = "select first_name, last_name, date_of_brith from user where first_name like %s order by first_name"
    cursor.execute(sql,substring)
    user_info=list()
    for r in cursor:
         sublist= [[r[0],r[1],str(r[2])]]
         user_info += sublist
    return render(request, 'users/results.html',
              {'user': user_info, 'substring': substring})

