# intro-to-cs

Assignments from MIT's Introduction to Computer Science and Programming class on OpenCourseware: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/

>_I did these assignments a little bit differently than the instructor suggests. This is a free course and, as such, there is no feedback or evaluation. So I decided to have some fun :)_

>_Kimberly The Geek_

# problem-set-1

## Paying Off Credit Card Debt
### Problem 1: 
#### Paying the Minimum

Write a program to calculate the credit card balance after one year if a person only pays the
minimum monthly payment required by the credit card company each month. 

### Problem 2: 
#### Paying Off Debt in a Year

Now write a program that calculates the minimum fixed monthly payment needed in order pay
off a credit card balance within 12 months. We will not be dealing with a minimum monthly
payment rate. 

### Problem 3: 
#### Use Bisection Searching to Improve Algorithmic Efficiency

Write a program that uses these bounds and bisection search (for more info check out the
Wikipedia page here) to find the smallest monthly payment to the cent (no more multiples of
$10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how
fast it is. Produce the output in the same format as you did in problem 2. 

_________________________





# problem-set-2

## Part 1 - Successive Approximation

### Problem 1:
#### Evaluting Polynomials

Implement the `evaluate_poly` function. This function evaluates a polynomial function for the
given x value. It takes in a tuple of numbers poly and a number x. By number, we mean
that x and each element of poly is a float. `evaluate_poly` takes the polynomial represented
by poly and computes its value at x. It returns this value as a float. 

### Problem 2:
#### Derivatives of Polynomials

Implement the `compute_deriv` function. This function computes the derivative of a polynomial
function. It takes in a tuple of numbers `poly` and returns the derivative, which is also a
polynomial represented by a tuple. 

### Problem 3:
#### Implementing Newton's Method of Successive Approximation

Implement the `compute_root` function. This function applies Newton’s method of successive
approximation as described above to find a root of the polynomial function. It takes in a tuple of
numbers `poly`, an initial guess `x_0`, and an error bound `epsilon`. It returns a tuple. The first
element is the root of the polynomial represented by `poly`; the second element is the number of
iterations it took to get to that root.

The function starts at `x_0`. It then applies Newton’s method. It ends when it finds a root `x` such
that the absolute value of f(x) is less than `epsilon`, i.e. f(x) is close enough to zero. It returns the
root it found as a float. 

## Part 2 - Hangman

### Problem 4: 
#### A Word Game

Implement a function, `hangman()`, that will start up and carry out an interactive Hangman game
between a player and the computer.

For this problem, you will need the code files ps2_hangman.py and words.txt, which were
included in the zip file from the top of this homework. Make sure your file runs properly before
editing. You should get the following output when running the unmodified version
of ps2_hangman.py:

>`Loading word list from file...`
>`55900 words loaded.`

You will want to do all of your coding for this problem within this file as well because you will
be writing a program that depends on each function you write. 

