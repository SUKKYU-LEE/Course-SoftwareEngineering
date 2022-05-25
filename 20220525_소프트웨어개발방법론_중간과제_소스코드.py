# -*- coding: utf-8 -*-
"""
Created on Wed May 25 20:09:44 2022

@author: User
"""
# 원의 둘래와 넓이를 구하는 클래스와 객체 생성
import math
class Circle:
    def __init__(self, radius=1):
        self.radius = radius
    def setRadius(self, radius=1):
        self.radius = radius
    def getRadius(self):
        return self.radius
    def getParameter(self):
        return 2 * math.pi * self.radius
    def getArea(self):
        return math.pi * math.pow(self.radius, 2)
    
circle1 = Circle()
print("반지름이", circle1.getRadius(), "인 원의 넓이는", circle1.getArea(), "입니다.")

circle2 = Circle(25)
print("반지름이", circle2.getRadius(), "인 원의 넓이는", circle2.getArea(), "입니다.")

circle3 = Circle(125)
print("반지름이", circle3.getRadius(), "인 원의 넓이는", circle3.getArea(), "입니다.")
    
    
    