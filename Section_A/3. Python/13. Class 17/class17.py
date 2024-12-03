# Write a function to calculate the area of a circle given its radius.


def area_of_circle(radius):
    # area = pi r2
    pi = 3.14
    area = pi * (radius ** 2)
    return area
    

print(area_of_circle(3))
