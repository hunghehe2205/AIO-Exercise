import torch
import torch.nn as nn
from abc import ABC, abstractmethod

# Exercise 1


class SoftMax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        sum_exp = x_exp.sum(0, keepdims=True)
        return x_exp / sum_exp


class SoftMax_Stable:
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdims=True)
        x_exp = torch.exp(x - x_max.values)
        sum_exp = x_exp.sum(0, keepdims=True)
        return x_exp / sum_exp


# Exercise2

class Human(ABC):
    def __init__(self, name: str, year: int):
        self._name = name
        self._year = year

    def get_year(self):
        return self.__year

    @abstractmethod
    def describe(self):
        pass


class Student(Human):
    def __init__(self, name: str, year: int, grade: str):
        super().__init__(name=name, year=year)
        self.__grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - year: {self._year} - Grade: {self.__grade}")


class Teacher(Human):
    def __init__(self, name: str, year: int, subject: str):
        super().__init__(name=name, year=year)
        self.__subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - year: {self._year} - Subject: {self.__subject}")


class Doctor(Human):
    def __init__(self, name: str, year: int, specialist: str):
        super().__init__(name=name, year=year)
        self.__specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - year: {self._year} - Specialist: {self.__specialist}")


class Ward:
    def __init__(self, name: str):
        self.__name = name
        self.__list_people = list()

    def add_human(self, human: Human):
        self.__list_people.append(human)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for p in self.__list_people:
            p.describe()

    def count_doctor(self):
        counter = 0
        for p in self.__list_people:
            if isinstance(p, Doctor):  # if type(p) is Doctor:
                counter += 1
        return counter

    def sort_age(self):
        self.__list_people.sort(key=lambda x: x.get_yob(), reverse=True)

    def compute_average(self):
        counter = 0
        total_year = 0
        for p in self.__list_people:
            if isinstance(p, Teacher):  # if type(p) is Teacher:
                counter += 1
                total_year += p.get_yob()
        return total_year/counter

# Exercise3


class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def pop(self):
        if self.is_empty():
            raise Exception("Underflow")
        return self.__stack.pop()

    def push(self, value):
        if self.is_full():
            raise Exception("Overflow")

        self.__stack.append(value)

    def top(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.__stack[-1]

# Exercise4


class MyQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def dequeue(self):
        if self.is_empty():
            raise Exception("Underflow")
        return self.__queue.pop(0)

    def enqueue(self, value):
        if self.is_full():
            raise Exception("Overflow")
        self.__queue.append(value)

    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.__queue[0]


queue = MyQueue(capacity=5)
queue.enqueue(1)
queue.enqueue(2)
print(queue.front())
