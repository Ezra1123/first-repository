import requests

response = requests.get("http://checklight.pythonanywhere.com/streets")

data = response.json()
streets_list = data["streets"]

# for street in streets_list:
#     print(street["name"])

# for street in streets_list:
#      print(street["name"].ljust(25),"|", street["state"].ljust(6), "|", street["status"],"|", street["avg_power"])


#history

adenuga = streets_list[13]["history"]
adenuga_timeline = adenuga["time_line"]

# for timeline in adenuga_timeline:
#     print(timeline["time"], "|", timeline["status"])



for timeline in adenuga_timeline:

    if timeline["status"] == 1:
        print(timeline["time"], "|", "ON")
    elif timeline["status"] == 0:
        print(timeline["time"], "|", "OFF")