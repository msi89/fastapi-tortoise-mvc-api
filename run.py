import uvicorn
from core.settings import HOST_NAME, PORT, DEBUG


if __name__ == "__main__":
    uvicorn.run('core:app', host=HOST_NAME, port=PORT, debug=DEBUG)


# class User():
#     name: str
#     email: str

#     def __init__(self, name, email):
#         self.name = name
#         self.email = email

#     def __str__(self):
#         return self.name


# user = User(name='Marcel', email='marcel@gmail.com')

# print(dict(user.__dict__))
