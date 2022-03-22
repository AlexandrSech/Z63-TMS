import csv

filename = "people.csv"

people = [
    ["Relevskiy", "Pavel", 25],
    ["Kochegarov", "Kirill", 14],
    ["Nesterov", "Dmitriy", 8],
    ["Kuvshinov", "Oleg", 56],
    ["Sexy", "Mariya", 18]
]

with open("/homework_10/filename", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(people)