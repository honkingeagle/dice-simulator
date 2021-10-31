import random
from tabulate import tabulate

class Main:
    def __init__(self):
        self.counter_face_1 = 0
        self.counter_face_2 = 0
        self.counter_face_3 = 0
        self.counter_face_4 = 0
        self.counter_face_5 = 0
        self.counter_face_6 = 0

        self.percentage_face_1 = 0
        self.percentage_face_2 = 0
        self.percentage_face_3 = 0
        self.percentage_face_4 = 0
        self.percentage_face_5 = 0
        self.percentage_face_6 = 0

    def calculateRandomness(self):
        n = random.random()
        if n > 0 and n <= 1/6: 
            return 1
        elif n > 1/6 and n <= 2/6:
            return 2
        elif n > 2/6 and n <= 3/6:
            return 3
        elif n > 3/6 and n <= 4/6:
            return 4
        elif n > 5/6 and n <= 6/6:
            return 5
        else:   
            return 6
    
    def calculateFrequency(self):
       for _ in range(1000):
          n = self.calculateRandomness()
          if n == 1:
            self.counter_face_1 += 1
          elif n == 2:
            self.counter_face_2 += 1
          elif n == 3:
            self.counter_face_3 += 1
          elif n == 4:
            self.counter_face_4 += 1
          elif n == 5:
            self.counter_face_5 += 1
          else:
            self.counter_face_6 += 1
            
       self.calculatePercentage()
       self.createTable()
       


    def calculatePercentage(self):
        self.percentage_face_1 = self.counter_face_1/1000*100
        self.percentage_face_2 = self.counter_face_2/1000*100
        self.percentage_face_3 = self.counter_face_3/1000*100
        self.percentage_face_4 = self.counter_face_4/1000*100
        self.percentage_face_5 = self.counter_face_5/1000*100
        self.percentage_face_6 = self.counter_face_6/1000*100

    def createTable(self):
      table = [
        ['Face','Frequency','Percentage'],
        ['1', self.counter_face_1, self.percentage_face_1],
        ['2', self.counter_face_2, self.percentage_face_2],
        ['3', self.counter_face_3, self.percentage_face_3],
        ['4', self.counter_face_4, self.percentage_face_4],
        ['5', self.counter_face_5, self.percentage_face_5],
        ['6', self.counter_face_6, self.percentage_face_6]
        ]
      print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))


exampleRoll = Main()
exampleRoll.calculateFrequency()