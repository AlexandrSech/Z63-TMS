from datetime import datetime, timedelta

trains = {
    "#_1": {
        "Point_departure": "Borisov",
        "Time_departure": datetime(2021, 12, 30, 17, 00),
        "Point_arrival": "Minsk",
        "Time_arrival": datetime(2021, 12, 30, 18, 30),
    },
    "#_2": {
        "Point_departure": "Saint_Petersburg",
        "Time_departure": datetime(2021, 12, 30, 00, 00),
        "Point_arrival": "Vladivostok",
        "Time_arrival": datetime(2022, 1, 5, 13, 00),
    },
    "#_3": {
        "Point_departure": "Minsk",
        "Time_departure": datetime(2021, 12, 30, 12, 00),
        "Point_arrival": "Moscow",
        "Time_arrival": datetime(2022, 1, 1, 10, 00),
    },
    "#_4": {
        "Point_departure": "Vitebsk",
        "Time_departure": datetime(2021, 12, 31, 5, 00),
        "Point_arrival": "Grodno",
        "Time_arrival": datetime(2021, 12, 31, 22, 00),
    },
    "#_5": {
        "Point_departure": "London",
        "Time_departure": datetime(2021, 12, 30, 11, 10),
        "Point_arrival": "Paris",
        "Time_arrival": datetime(2022, 3, 14, 12, 00),
    }
}


for key in trains.keys():
    travel_time = trains[key]["Time_arrival"] - trains[key]["Time_departure"]

    if travel_time > timedelta(hours=7, minutes=20):
        print(f"Поезд {key}: {trains[key]['Point_departure']} - {trains[key]['Point_arrival']} был в пути {travel_time}")