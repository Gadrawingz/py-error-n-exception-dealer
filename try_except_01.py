def test_exception():
    try:
        # Division by zero raises an exception
        number1 = 10
        number2 = 0

        result = number1 / number2
        print(result)

    except ZeroDivisionError:
        print("Ouch, You can't divide",number1, "over 0")
    else:
        # Exception didn't occur, we're good.
        pass
    finally:
        # Executed after running code & all exceptions have been handled,
        # Even if a new exception is raised while handling.
        print("We're done with that.")

test_exception()
