# Types of functions:
# 1. Global
# 2. Local (invested in other functions)
# 3. Methods (functions associated with any object)
# 4. Anonymous (do not have a name and are declared at the place of use - they are represented by lambda expression


def sum_of_cubes(x, y):  # Global function (1)

    # Local function (2) (it "sees" only the code inside SUM_OF_Cubes ())
    def cube(a):
        return a**3
    return cube(x) + cube(y)  # Return returns the result of performing
                              # who caused this function

print(sum_of_cubes(2,4))

class Car:
    def move(self, x):  # Method (3)
        self.x += x


players = [{"name": "Yuri", "rank": 5},
           {"name": "Sergey", "rank": 3},
           {"name": "Maxim", "rank": 4}]

# Anonymous function (4) (lambda-expression)
# In the Sorted () functions is used to determine the sort order

print(sorted(players, key=lambda player: player["name"]))  # Sorting by NAME
# [{'rank': 4, 'name': 'Maxim'}, {'rank': 3, 'Name': 'Sergei'}, {'rank': 5, 'Name': 'Yuri']

print(sorted(players, key=lambda player: player["rank"]))  # Sorting by Rank
# [{'rank': 3, 'name': 'Sergei'}, {'rank': 4, 'name': 'Maxim'}, {'rank': 5, 'Name': 'Yuri']
