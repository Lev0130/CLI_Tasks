import json, argparse, re
from datetime import date

date_today = date.today()
nums = []
tasks = []

with open("data.json", "r", encoding = "utf-8") as file:
        try:
            data = json.load(file)
        except:
            data = {}
        if data == {}:
            num = 0
        else:
            for key in data:
                nums.append(int(key))
            num = max(nums)
print(num)
                
def add(activity):
    with open("data.json", "w", encoding = "utf-8") as file:
        data[num + 1] = {}
        data[num + 1]["date"] = str(date_today)
        data[num + 1]["task"] = activity
        data[num + 1]["state"] = "pending"
        json.dump(data, file, indent = 4)
add("tarea1")

def see_tasks():
    with open("data.json", "r", encoding = "utf-8") as file:
        new_data = {}
        data = json.load(file)
        for key, values in data.items():
            print("KEY:", key)
            print("VALUES:", values)
            date_day = values["today"]
            if date_day in new_data:
                new_data[date_day][key] = {values["task"], values["state"]}
            else:
                new_data[date_day] = {}
                new_data[date_day][key] = {values["task"], values["state"]}
        print(new_data)

see_tasks()
                