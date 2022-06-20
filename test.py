import configparser

name = "Варианты обновления"
# первый шаг:  Получить объект конфигурации
config = configparser.ConfigParser()


config.read("update.ini")
 # Шаг третий:Получить значение опции
try:
   auto = config.get("эль примо","биби")
   noupdate = config.get("эль примо","эдгар")
except Exception as e:
    print(e)
# Шаг 2: Добавьте название раздела
config.add_section('эль примо')
# Шаг третий:Добавить вариант
config.set("эль примо", "эдгар", "хуесос")
config.set("эль примо", "биби", "лофа")
config.set("эль примо", "вольт", "хуесос")
# Шаг 4: Создайте файл конфигурации
file = open("update.ini", mode="w")
config.write(file)
print(">> Конфигурационный файл ini записан успешно")