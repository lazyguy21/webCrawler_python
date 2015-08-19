__author__ = 'ye'


# class Duck():
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#     def get_name(self):
#         print('inside the getter')
#         return self.hidden_name
#     def set_name(self, input_name):
#         print('inside the setter')
#         self.hidden_name = input_name
#     name = property(get_name, set_name)
class Duck():
    def __init__(self,input_name):
        self.__name=input_name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,input_name):
        self.__name=input_name
fowl=Duck("caonima")
print(fowl.name)
# print(fowl._name)
print(fowl._Duck__name)

from collections import namedtuple
Duck= namedtuple()