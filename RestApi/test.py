import requests

BASE_URL = "http://127.0.0.1:5000/"

# data = [{"likes":78 , "name":"jim" , "views":900},
#         {"likes":200 , "name":"jinder" , "views":989},
#         {"likes":1000 , "name":"kane" , "views":329}]

# for i in range(len(data)):
#     response = requests.put(BASE_URL + "video/" + str(i), json=data[i])
#     print(response.json())

# response = requests.delete(BASE_URL + "video/0")
# print(response)
# input()
# response = requests.get(BASE_URL + "video/2")
# print(response.json())
response = requests.patch(BASE_URL + "video/2", {})
print(response.json())