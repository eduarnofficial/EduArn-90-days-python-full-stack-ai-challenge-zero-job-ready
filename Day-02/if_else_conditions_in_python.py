#TOPICS REVISED OR LEARNT -DAY 2
'''
1. What are Conditional Statements?

Conditional statements allow a program to make decisions.

Condition always evaluates to:
True
False
2. Why do we need conditions?

Without conditions, code executes every time.
Conditions help execute code only when required.

3. Syntax of if Statement

if condition:
    statement
4. Indentation

Python uses indentation instead of {} braces.

Usually 4 spaces.

Wrong indentation results in:
IndentationError

5. Comparison Operators

==   Equal To
!=   Not Equal To
>    Greater Than
<    Less Than
>=   Greater Than or Equal To
<=   Less Than or Equal To

6. Simple if Statement

if condition:
    code
'''

marks= 80

if marks >50:
    print("Pass")
'''
7. if-else Statement

Exactly one block executes.

if condition:
    code1
else:
    code2
'''

age= 15

if age>= 18:
    print("Adult")
else:
    print("Minor")
'''
8. if-elif-else Ladder

Used when multiple conditions exist.

Python checks conditions from top to bottom.

Stops at first True condition.
'''

marks =75

if marks>= 90:
    print("A")

elif marks>= 80:
    print("B")

elif marks >= 70:
    print("C")

else:
    print("Fail")


'''
9. Important Rule of elif

Python stops checking after first True condition.

Wrong ordering may produce wrong results.
'''

x = 95

if x >= 50:
    print("Pass")

elif x >= 80:
    print("Distinction")

# Output: Pass


'''
10. Nested if

if inside another if.

Useful when one condition depends on another.
'''

age = 25
citizen = True

if age>= 18:
    if citizen:
        print("Eligible")


'''
11. Truthy and Falsy Values

Falsy:

False
0
0.0
''
[]
()
{}
set()
None
Everything else is Truthy.
'''
print(bool(""))
# False

print(bool("Python"))
# True


'''
12. Logical Operators

and
or
not

AND → Both conditions must be True

OR → At least one condition must be True

NOT → Reverses result
'''

age = 25
salary = 50000

if age > 18 and salary > 30000:
    print("Eligible")


'''
13. Truth Table

AND

T T -> T
T F -> F
F T -> F
F F -> F

OR

T T -> T
T F -> T
F T -> T
F F -> F

NOT

T -> F
F -> T
'''


'''
14. Operator Precedence

Highest:
not

Then:
and

Then:
or

Example:
'''

print(True or False and False)

# Evaluated as:
# True or (False and False)

# Output:
# True


'''
15. Membership Operators

in
not in

Used to check presence of value.
'''

name = "Python"

if "P" in name:
    print("Found")


'''
16. Identity Operators

is
is not

Used to compare memory identity.
'''

x = None

if x is None:
    print("No Value")


'''
17. Short Circuit Evaluation

Python stops evaluation when answer is already known.

True or something()

Second condition never executes.

False and something()

Second condition never executes.
'''


'''
18. Chained Comparisons

Python supports:

10 < x < 20

Equivalent to:

10 < x and x < 20
'''

x = 15

if 10 < x < 20:
    print("Inside")


'''
19. Ternary Operator

One-line if else.

value_if_true if condition else value_if_false
'''

age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)


'''
20. Comparing Strings

String comparison is case-sensitive.

"Kirti" != "kirti"

Ignore case using:
.lower()
.upper()
'''

name = "Kirti"

if name.lower() == "kirti":
    print("Match")


'''
21. Common Mistake

Wrong:

if x = 10:

Correct:

if x == 10:
'''


'''
22. Common Mistake

Wrong:

if x == 1 or 2 or 3:

Always True

Correct:
'''

if x in [1,2,3]:
    print("Valid")


'''
23. pass Statement

Placeholder.

Used when block is empty.
'''

if True:
    pass


'''
24. Taking Input in Conditions

Input always returns string.

Convert when required.
'''

age = int(input("Enter Age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")


'''
25. Largest of Three Numbers

Use multiple conditions with AND operator.
'''


'''
26. Leap Year Program

Important Interview Question

Rules:

Divisible by 400 -> Leap Year

Divisible by 100 -> Not Leap Year

Divisible by 4 -> Leap Year

Else -> Not Leap Year
'''


'''
27. Match Case (Python 3.10+)

Alternative to long if-elif ladders.

match variable:

    case value:
        code

    case _:
        default code
'''

day = 2

match day:

    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case _:
        print("Invalid")


'''
28. Interview Questions

Q1. Difference between if and if-else?

if:
Runs only when condition is True.

if-else:
One block always executes.


Q2. Difference between if and elif?

if starts condition chain.

elif checks only when previous conditions fail.


Q3. What is short-circuit evaluation?

Python stops evaluating logical expression once result is known.


Q4. Difference between == and is?

== -> compares values

is -> compares memory identity


Q5. Why use "is None" instead of "== None"?

Because it checks object identity and is Pythonic.


Q6. What is a ternary operator?

One-line if else expression.

result = "Pass" if marks >= 40 else "Fail"


Q7. What is the biggest beginner mistake?

Using:

if x = 10

instead of

if x == 10


Q8. Output?

if "":
    print("Yes")
else:
    print("No")

Output:
No

Because empty string is Falsy.


Q9. Output?

x = 100

if x > 50:
    print("A")

elif x > 80:
    print("B")

Output:
A

Python stops at first True condition.


Q10. When should match-case be used?

When comparing one variable against many fixed values.
'''
