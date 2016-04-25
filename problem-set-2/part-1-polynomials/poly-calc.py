# 6.00 Problem Set 2
#
# Successive Approximation
#

# Print evaluation of polynomial

def print_evaluation(poly, x):

    print "\n\n----------------------------------------------------\n\n\nResult: " + str(evaluate_poly(poly,x))

# Calculate evaluation of polynomial
def evaluate_poly(poly, x):

    i = 0
    result = 0.0

    for coefficient in poly:

        exponent = len(poly) - 1 - i
        result += (coefficient * (x ** exponent))
        print "\n----------------------------------------------------\n\nEvaluating " + str(coefficient) + "x ^ " + str(exponent)
        print "\n" + str(coefficient) + " * " + str(x) + " ^ " + str(exponent)  + " = " + str(coefficient * (x ** exponent))
        print "\nTotal: " + str(result)
        i+=1

    return result



# Print derivative of polynomial
def print_derivative(poly):

    print_poly(poly)
    print "\n\n\n----------------------------------------------------\n\n\n f'" + get_string(compute_derivative(poly))

# Calculate derivative of polynomial
def compute_derivative(poly):

    i = 0
    derivative = []

    if len(poly) == 1:
        print "\n\n\n----------------------------------------------------\n\n\nf'(x) = 0"
    else:
        for coefficient in poly[0:len(poly)-1]:
            exponent = len(poly) - 1 - i
            derivative.append(coefficient * exponent)
            i += 1

    return derivative


# Print root of polynomial
def print_root(poly, x_0, epsilon):

    root = compute_root(poly, x_0, epsilon)
    print "\n\n\n----------------------------------------------------\n\n\nEstimated root of f" + get_string(poly) + " = " + str(root[0])
    print "Number of iterations to find root: " + str(root[1])

# Calculate root
def compute_root(poly, x_0, epsilon):

    # 1 calculate f(x_0)
    # 2 if absolute value of f(x_0) is less than epsilon, it's close enough
    # 3 else, x_n+1 = x_n - f(x_n)/f`(x_n)

    i = 1
    x = [x_0]

    # while still searching for the root
    while True:
        # find a new x
        x.append(x[i-1] - evaluate_poly(poly,x[i-1])/evaluate_poly(compute_derivative(poly),x[i-1]))
        print "New x: x_" + str(i) + " = " + str(x[i])

        # if x_i is close enough to a root, return value and break loop
        if abs(evaluate_poly(poly, x[i])) < epsilon:
            root = (x[i], i+1)
            return root
            break

        i+=1



def get_string(poly):

    poly_string = "(x) = "
    i = 0

    for coefficient in poly:

        exponent = len(poly) - 1 - i

        # if it does not evaluate to zero
        if coefficient != 0:

            # if not the first value AND not the last, add a plus sign to the string
            if i != 0 and i != len(poly):
                poly_string += " + "

            # add value to the string, remove .0 's
            if coefficient - int(coefficient) == 0.0:
                poly_string += str(int(coefficient))
            else:
                poly_string += str(coefficient)
            # if exponent is NOT equal to zero, add x to the string
            if exponent != 0:
                poly_string += "x"
                # if exponent is NOT equal to one, add the exponent to the string
                if exponent != 1:
                    poly_string += "^" + str(exponent)

        i += 1

    return poly_string


def print_poly(poly):

    print "\n\n\n----------------------------------------------------\n\n\n f" + get_string(poly)


choice = 1

# Program Selection #
switch = {
    1: print_evaluation,
    2: print_derivative,
    3: print_root,
    4: print_poly,
}

# Program Begins #
while choice != 0:

    choice = int(raw_input("\n\n----------------------------------------------------\n\nWhat would you like to do?\n\n\t1: Evaluate a Polynomial Expression\n\t2: Compute Derivative of a Polynomial\n\t3: Compute Root of a Polynomial\n\t4: Print a Polynomial\n\t0: Exit Program\n\n>>>\t\t"))
    if choice == 0:
        print "\n\n---------------------------------\n    >>>> Exiting Program <<<<\n---------------------------------"
        break

    poly_input = raw_input("\n\nEnter the coefficients of your polynomial, separated by a comma and a space,\nin order from the largest exponent of x to the smallest.\n\nExample: 3x^3 - 2x^2 -1 should be input as: 3, -2, 0, -1\n\n\n>>>\t\t")

    poly = [float(x) for x in poly_input.split(', ')]

    if choice == 1:
        x = float(input("\nEnter a value for x:\t"))
        switch[choice](poly,x)

    elif choice == 3:
        x_0 = float(input("\nEnter a value for x_0 :\t"))
        epsilon = float(input("\nEnter a value for epsilon:\t"))
        switch[choice](poly,x_0,epsilon)

    else:
        switch[choice](poly)
