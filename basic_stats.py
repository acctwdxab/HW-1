import statistics

class Person:
   """
    Contains the person's name and age.
    """
   def __init__(self, name, age):
       """
       This init method takes two values - name and age - and uses them
       to initialize the data members.
       """
       self.name = name
       self.age = age


def basic_stats(person_list):
   """
   This function takes as a parameter a list of Person objects and
   returns a tuple containing the mean, median, and mode of all the
   ages.
   """


   age = []


   for p in person_list:
       age.append(p.age)
       age_mean = statistics.mean(age)
       age_median = statistics.median(age)
       age_mode = statistics.mode(age)
       return age_mean, age_median, age_mode

#
# p1 = Person("Kyoungmin", 73)
# p2 = Person("Mercedes", 24)
# p3 = Person("Avanika", 48)
# p4 = Person("Marta", 24)
#
#
# person_list = [p1, p2, p3, p4]
#
#
# print(basic_stats(person_list))