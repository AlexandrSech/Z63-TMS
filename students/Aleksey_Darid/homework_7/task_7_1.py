
def du_sm(du):
    sm=2.54*du
    return sm
    
def sm_du(sm):
    du=0.3937*sm
    return du
    
def ml_km(ml):
    km=1.60934*ml
    return km

def km_ml(km):
    ml=0.62137*km
    return ml
while True:
    x=int(input("Если хотите превести дюймы в санциметры нажмите 1 \nЕсли санциметры в дюймы нажмите 2 \nЕсли хотите перевести мили в километры нажмите 3 \nКилометры в мили нажмите 4 \n(Для выхода нажмите 0) "))
    if x==1:
        dumi=du_sm(int(input("Ввеите число ")))
        print(dumi, "см")
    elif x==2:
        sant=sm_du(int(input("Ввеите число ")))
        print(sant, "дюйм")
    elif x==3:
        mil=ml_km(int(input("Ввеите число ")))
        print(mil, "км")
    elif x==4:
        kilom=km_ml(int(input("Ввеите число ")))
        print(kilom, "мили")
    elif x==0:
        break
    else:
        print("Проверьте пораметры ввода")
