from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

def home(request):
    page = requests.get('https://www.mygov.in/covid-19')
    soup = BeautifulSoup(page.content, 'html.parser')

    information = soup.find_all(class_='information_row')[0]

    date = information.find('span').get_text()
    total_active_case = information.find(class_='iblock active-case').find(class_ = 'icount').get_text()
    Cured_Discharged = information.find(class_='iblock discharge').find(class_ = 'icount').get_text()
    dead_case = information.find(class_='iblock death_case').find(class_ = 'icount').get_text()
    migrated = information.find(class_='iblock migared_case').find(class_ = 'icount').get_text()

    state_count = soup.find_all(class_ = 'views-row')
    detail = [[] for i in range(len(state_count)) ]
    for i in range(len(state_count)):
        detail[i].append(state_count[i].find(class_ = 'st_name').get_text())
        detail[i].append(state_count[i].find(class_ = 'tick-confirmed').find('small').get_text())
        detail[i].append(state_count[i].find(class_ = 'tick-active').find('small').get_text())
        detail[i].append(state_count[i].find(class_ = 'tick-discharged').find('small').get_text())
        detail[i].append(state_count[i].find(class_ = 'tick-death').find('small').get_text())

    context = {
        "detail":detail,
        "Date":date,
        "TotalCase":total_active_case,
        "TotalRecoverCase":Cured_Discharged,
        "TotalDeadCase":dead_case,
        "Migrated" :migrated,
    }
    return render(request,'index.html',context)

def state(request):
        page = requests.get('https://www.mygov.in/covid-19')
        soup = BeautifulSoup(page.content, 'html.parser')
        state_count = soup.find_all(class_ = 'views-row')
        detail = [[] for i in range(len(state_count)) ]
        for i in range(len(state_count)):
            detail[i].append(state_count[i].find(class_ = 'st_name').get_text())
            detail[i].append(state_count[i].find(class_ = 'tick-confirmed').find('small').get_text())
            detail[i].append(state_count[i].find(class_ = 'tick-active').find('small').get_text())
            detail[i].append(state_count[i].find(class_ = 'tick-discharged').find('small').get_text())
            detail[i].append(state_count[i].find(class_ = 'tick-death').find('small').get_text())

        context = {
            "detail":detail,
        }
        return render(request,'State.html',context)



