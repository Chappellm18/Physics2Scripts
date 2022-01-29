import math


def main():
    # this function will run the equation

    # need the distance, mass, and string length inputed by user
    r = float(input("Enter the distance between the two pith balls (cm): "))
    mass = float(input("Enter the mass of the balls (grams): "))
    l = float(input("Enter the length of the string (cm): "))

    # call the functions
    theta_calc = theta(r, l)
    print("The angle between the two pith balls is: ", theta_calc)
    mg_calc = mg(mass)
    print("The mg of the balls is: ", mg_calc)
    final_force = force(theta_calc, mg_calc)
    print("The final force applied to the balls: ", final_force)


def mg(mass):
    # this function will calculate the mg
    return mass * 9.8


def theta(r, l):
    # this function will calculate the theta
    l = (l*2)/100
    r = r/100
    return math.asin(r/l)


def force(theta, mg):
    # this function will calculate the force
    return mg * math.tan(theta)


main()
