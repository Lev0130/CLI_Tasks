"""
Nombre: CLI Tasks 
Librerías: argparse json? 
set arguments: add, list, done 
return: date number task state 

creamos diccionario/documento (load, documento json a diccionario)

Add, creamos diccionario con fecha de hoy,
añadimos a ese diccionario otro diccionario 
con una dupla número tarea a la que le 
asignamos pending o done (true false). Todo dependiendo del número identificativo

List, imprimimos el diccionario / documento JSON (pretified)

Done, buscamos ese número en el diccionario y cambiamos su estado.

data = {
  "1": {"task": "...", "date": "2026-03-23", "state": "pending"},
  "2": {"task": "...", "date": "2026-03-23", "state": "done"},
  "3": {"task": "...", "date": "2026-03-24", "state": "pending"}
}

2026-03-23
  [1] Finish log analyzer (pending)
  [2] Write README (done)

2026-03-24
  [3] Start CLI tasks project (pending)
  
  
Cosas que añadir:
    que se guarde en la carpeta del archivo con pathlib
        Obtener la ruta del script
        Obtener su carpeta
        Construir la ruta al JSON desde ahí
  
"""
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

                
def add(activity):
    with open("data.json", "w", encoding = "utf-8") as file:
        data[num + 1] = {}
        data[num + 1]["date"] = str(date_today)
        data[num + 1]["task"] = activity
        data[num + 1]["state"] = "pending"
        json.dump(data, file, indent = 4)

def see_tasks():
    with open("data.json", "r", encoding = "utf-8") as file:
        new_data = {}
        data = json.load(file)
        for key, values in data.items():
            date_day = values["date"]
            if date_day in new_data:
                new_data[date_day][key] = {"task":values["task"], "state":values["state"]}
            else:
                new_data[date_day] = {}
                new_data[date_day][key] = {"task":values["task"], "state":values["state"]}
        dates = []
        for fecha, datos in new_data.items():
            if fecha not in dates:
                print(fecha)
                dates.append(fecha)
                for number,values in datos.items():
                    print(str("   ["+ number+ "] "+ str(values["task"] + " ("+ values["state"] + ")")))
            else:
                for number,values in datos.items():
                    print(str("   ["+ number+ "] "+ values["task"] + values["state"]))
                    
def done(num):
    number = str(num)
    with open("data.json", "r", encoding = "utf-8") as file:
        data = json.load(file)
        for key, values in data.items():
            if number == key:
                values["state"] = "done"
                print(data[number]["task"] + " " + data[number]["state"])
                break
            else:
                continue
    with open("data.json", "w", encoding = "utf-8") as file:   
        json.dump(data, file, indent = 4)  
            
def index():
    print("""
         This is a CLI program that helps you skedule your tasks.
         Write  
          """)

                
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add", help="Add a task")
add_parser.add_argument("activity")
subparsers.add_parser("list")
done_parser = subparsers.add_parser("done")
done_parser.add_argument("number")

args = parser.parse_args()

if args.command == "add":
    add(args.activity)

elif args.command == "list":
    see_tasks()
elif args.command == "done":
    done(args.number)
else:
    index()

