# def multiply(number):
#     """THIS FUNCTION MULTIPLIES NUMBERS BY 3"""

#     print("The answer is : ", number * 3)

# multiply(2)




# name = "Adedibu"

# def print_name():

#     global name

#     name = "bolu"
#     print(name)

# print_name()
# print(name)





# import requests

# url_to_get = "http://checklight.pythonanywhere.com/streets"
# response_data = ""

# def make_request(url):
#     global response_data

#     response = requests.get(url)
#     response_data = response

# def check_for_success():

#     if response_data.status_code == 200:
#         print("Request was successful")

# def json_or_content():

#     try:
#         response_data.json()
#         print("data type is json")

#     except:
#         response_data.content
#         print("data type is HTML >>>>> use content")


# make_request(url_to_get)
# check_for_success()
# json_or_content()



import requests

url_to_get = "http://checklight.pythonanywhere.com/streets"
response_data = ""

def make_request(url):
    global response_data

    response = requests.get(url)
    response_data = response

def check_for_success():

    if response_data.status_code == 200:
        print("Request was successful")


def json_or_content():

    try:
        response_data.json()
        print("data type is json")
        print(keys)

    except:
        response_data.content
        print("data type is HTML")

def print_keys():
    data = response_data.json
    keys = data.keys()
    print(keys)
    

make_request(url_to_get)
check_for_success()
json_or_content()
print(keys)