udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(p):
    total_student = 0
    total_tution = 0
    for colleague, student, tution in p:
        total_student = total_student +student
        total_tution = total_tution +student*tution
    return total_student, total_tution


print (total_enrollment(usa_univs))
