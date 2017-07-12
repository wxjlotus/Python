# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 09:49:11 2017

@author: wangxj
"""

#_DEBUG = True
def ml_std_weight(height):
      standard_weight = (height - 100)*0.9
      return standard_weight

def fml_std_weight(height):
      standard_weight = (height - 100)*0.9 - 2.5
      return standard_weight

def bmi(height, weight, gender):
#      import pdb
#      if _DEBUG == True:
#            pdb.set_trace()
      if gender != 'male' and gender !='female':
            print("input error")
      elif gender == 'male':
            standard_weight = ml_std_weight(height)
      else:
            standard_weight = fml_std_weight(height)
      if weight <= (standard_weight*0.9):
            print ("You BMI is -1")
      elif  weight <(standard_weight*1.1):
            print ("You BMI is 0")
      elif  weight <(standard_weight*1.2):
            print ("You BMI is 1")
      elif  weight <(standard_weight*1.3):
            print ("You BMI is 2")
      elif  weight <(standard_weight*1.5):
            print ("You BMI is 3")
      else:
            print ("You BMI is 4")

if __name__ == "__main__":
      bmi(178,81,'male')