days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
'''
def how_many_days(months):
    return days_in_month[months-1]

print(how_many_days(1))

print(how_many_days(12))
print(how_many_days(10))

print(how_many_days(13))

mixed_up = ['apple',3,'orange',4,[1,2,['alpha','beta']]]
'''
beatles = [['John', 1940],
           ['Paul',1942],
           ['George',1943],
           ['Ringo',1940]
           ]

print (beatles[1])

countries = [['China','Beijing',1350],
             ['India','Delhi',1250],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

print (countries[1][1])

y= countries[0][2]/countries[2][2]

print(y)
