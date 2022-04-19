# HW: Создать пакет - (cars)
# создать модули такие как (create_car, get_car_info)
# create_cars —> Создать Абстрактный класс (Car)
# Создать методы для Car - (start_engine, stop_engine)
# get_car_info —> def get_car_info(car): —> car_info
# создать main.py файл и там использовать все ваши модули в пакете (cars)

class Car:
    def __init__(self, title, model):
        self.title = title
        self.model = model

    def start_engine(self):
        print("start engine ")

    def stop_engine(self):
        print("engine stoped")

    def __str__(self):
        return f"Title-{self.title}\n" \
               f"Model-{self.model}"

