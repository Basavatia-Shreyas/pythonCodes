def given():
    print("                       |")
    print("       Statement       |           Reason       ")
    print("                       |")
    print("__________________________________________________")
    print("                       |")
    print("                       |           Given        ")
    print("                       |")

def chart_header():
    chart_title = input("Enter the chart title y/n?")
    if chart_title.lower() == "y":
        given()
    else:
        pass

def refelxive():
    congruence_equal = input("using congruence or equality c/e").upper()
    angle_segment = input("Segment or an angle s/a").upper()
    if angle_bisector() == "A":
        hello = "angle"
    elif angle_bisector() == "S":
        hello = "Segment"
    value = input("enter the {}".format(hello))

    chart_header()

    if congruence_equal == "E" and angle_segment == "S":
        print("{} = {}                | Reflexive Property".format(value, value))
        print("                       |")
    elif congruence_equal == "E" and angle_segment == "A":
        print("m<{} = m<{}          | Reflexive Property".format(value, value))
        print("                       |")
    elif congruence_equal == "C" and angle_segment == "S":
        print("{} is congruent to {}  | Reflexive Property".format(value, value))
        print("                       |")
    elif congruence_equal == "C" and angle_segment == "A":
        print("<{} is congruent to   |".format(value))
        print("<{}                   | Reflexive Property".format(value))
        print("                       |")

def verticle_angles():
    angle_one = input("Enter one angle").upper()
    angle_two = input("Enter another angle").upper()

    chart_header()

    print("                       |")
    print("<{} is congruent to   | Intersecting lines form congruent VA")
    print("<{}                   |")
    print("                       |")

def perpendicular():
    choose = input("forwards or reverse(f) or (r)").upper()
    angle_one = input("Enter an angle").upper()
    angle_two = input("Enter another angle").upper()

    chart_header()
    if choose == "F":
        print("                       |")
        print("<{} ~= <{}           | _|_ form congruent ~= right <'s")
        print("                       |")
    elif choose == "R":
        print("                       |")
        print("<{} and <{} are      | _|_ form congruent ~= right <'s")
        print("right <'s              |")
        print("                       |")

def angle_bisector():
    angle_one = input("Enter an angle").upper()
    angle_two = input ("Enter another angle").upper()

    chart_header()

    print("<{} and <{} are      |".format(angle_one, angle_two))
    print("congruent              | Definition of angle bisector")
    print("                       |")

def addition():
    sum_one = input("enter sum one")
    sum_two = input("enter sum two")
    seg_one_one = input("enter seg one of sum one")
    seg_one_two = input("enter seg two of sum one")
    seg_two_one = input("enter seg one of sum two")
    seg_two_two = input("enter seg two of sum two")
    angle_seg = input("Angle or Segment")

    chart_header()

    print("                       |")
    print("                       |")
    print("                       |")
    print("                       |")



