
# IT 405L - LABORATORY ACTIVITY 1
# Logical Operators and an Expression Evaluator
# Student: Peteros, Eljie J.
# Student Number: 2310240-1

# STEP 2: Logical AND, OR, and NOT


def my_and(a, b):
    return (a, b) == (True, True)


def my_or(a, b):
    return (a, b) != (False, False)


def my_not(a):
    return a == False


# STEP 3: Logical implication
# A implies B is false only when A is True and B is False.


def my_implies(a, b):
    return (a, b) != (True, False)


# STEP 5: Expression evaluator


def evaluate(expr):
    # Return the value if the expression is a Boolean
    if isinstance(expr, bool):
        return expr

    operation = expr[0]

    # Handle NOT, which has one operand
    if operation == "not":
        return my_not(evaluate(expr[1]))

    # Evaluate the two operands
    a = evaluate(expr[1])
    b = evaluate(expr[2])

    if operation == "and":
        return my_and(a, b)
    elif operation == "or":
        return my_or(a, b)
    elif operation == "implies":
        return my_implies(a, b)
    else:
        raise ValueError("Unknown operation: " + str(operation))


# STEP 4: Test all Boolean combinations


if __name__ == "__main__":

    values = [True, False]

    print("AND TESTS")
    for a in values:
        for b in values:
            print(a, b, "=", my_and(a, b))

    print("\nOR TESTS")
    for a in values:
        for b in values:
            print(a, b, "=", my_or(a, b))

    print("\nNOT TESTS")
    for a in values:
        print(a, "=", my_not(a))

    print("\nIMPLIES TESTS")
    for a in values:
        for b in values:
            print(a, b, "=", my_implies(a, b))

    # STEP 6: Test at least six expressions

    print("\nEXPRESSION TESTS")

    tests = [
        ("and", True, True),
        ("or", False, True),
        ("not", False),
        ("implies", True, False),
        ("and", True, ("not", False)),
        ("or", False, ("and", True, ("not", False)))
    ]

    for expr in tests:
        print(expr, "=", evaluate(expr))

    # Required expression from the instructor's parameter file

    EXPR = (
        "implies",
        ("and", ("or", True, False), ("and", False, False)),
        ("implies", ("implies", False, True), ("not", False))
    )

    print("\nREQUIRED EXPR")
    print("EXPR =", evaluate(EXPR))

    # STEP 7: Show why tuple evaluation raises an error.
    # Keep this separate so the other tests can finish first.

    print("\nSTEP 7 TEST")

    try:
        expr = ("or", True, ("and", 1 / 0, False))
        print(evaluate(expr))
    except ZeroDivisionError as error:
        print(type(error).__name__ + ":", error)
