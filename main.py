# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
# from week0 import matrix, swap, boat
# from week1 import carlist, fibonacci
# from week2 import mathy, fibonacci_class, advy, palindrome, mathyc
import week0.boat as week_zero_boat
import week0.matrix as week_zero_matrix
import week0.swap as week_zero_swap
import week1.list as week_one_list
import week2.math as week_two_math

week0_menu = [
    ["Boat", week_zero_boat.boat],
    ["Matrix", week_zero_matrix.matrix],
    ["Swap", week_zero_swap.swap],
]

data_menu = [
    ["For", week_one_list.for_print_data],
    ["While", week_one_list.while_print_data],
    ["Recursive", week_one_list.recursive_print_data],
]

math_menu = [
    ["Factorial", week_two_math.factorial_helper],
    ["Least Common Multiple", week_two_math.lcm],
    ["Factors", week_two_math.factors],
    ["Primes", week_two_math.primes]
]

# week2_menu = [
#     ["Math", "math.py"],
#     ["On top of the Mountains?", advy.mountain],
#     ["Navigating a lake?", advy.lake]
# ]


def menu(title, options):
    # header for menu
    # Menu banner
    border = "=" * 25
    banner = f"\n{border}\n{title}\n{border}"
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")
    # end validation try

    menu(title, options)  # recursion, start menu over again


# def math_menu
# using sub menu list above:
# sub_menu works similarly to menu()
def _data_menu():
    title = "Data SubMenu"
    menu(title, data_menu)


# def math_menu
# using sub menu list above:
# sub_menu works similarly to menu()
def _math_menu():
    title = "Math SubMenu"
    menu(title, math_menu)


# def adventure menu
# using sub menu list above:
# sub_menu works similarly to menu()
def _week_0_menu():
    title = "Week 0 Menu"
    menu(title, week0_menu)


def driver():
    title = "Main Menu"
    menu_list = [["Data", _data_menu],
                 ["Math", _math_menu],
                 ["Week 0", _week_0_menu],
                 ]
    menu(title, menu_list)


if __name__ == "__main__":
    driver()