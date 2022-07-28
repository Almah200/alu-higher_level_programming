#!/usr/bin/python3
''''Defined a class Student.'''


class Student:
    '''.instatiated a class.'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        '''.defined a public method.'''
    def to_json(self):
        return student.__dict__
