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
   for person in person_list:
       age.append(person.age)
   age_mean = statistics.mean(age)
   age_median = statistics.median(age)
   age_mode = statistics.mode(age)

   return age_mean, age_median, age_mode


# person_list = [Person("Kyoungmin", 73)  , Person("Mercedes", 24) , Person("Avanika", 48) , Person("Marta", 24)]

# print(basic_stats(person_list))
