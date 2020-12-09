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

def midpoint():
    segment_one = input("Enter a segment").upper()
    segment_two = input("Enter another segment").upper()

    chart_header()

    print("__     __              |")
    print("{} and {}              |".format(segment_one, segment_two))
    print("are congruent          | Definition of a midpoint")

def linear_pairs():
    angle_one = input("Enter a given angle").upper()
    angle_two = input("Enter angle your trying to prove").upper()
    angle_three = input("Enter another given angle").upper()
    angle_four = input("Enter another angle your trying to prove").upper()

    chart_header()

    print("<{} and <{}          |".format(angle_one, angle_two))
    print("<{} and <{}          |".format(angle_three, angle_four))
    print("are adjacent angles    | Definition of adjacent angles")
    print("                       |")
    print("<{} and <{}          |".format(angle_one, angle_two))
    print("<{} and <{}          |".format(angle_three, angle_four))
    print("are linear pairs       | Definition of linear pairs")
    print("                       |")
    print("<{} and <{}          |".format(angle_one, angle_two))
    print("<{} and <{}          |".format(angle_three, angle_four))
    print("are supplimentary      | Linear pairs are supplimentary")
    print("                       |")
    print("<{} and <{}          |".format(angle_two, angle_four))
    print("are congruent          | Suppliments of congruent angles are congruent")
    print("                       |")
def altitude():
    line_one = input("Enter the line that is an altitude").upper()
    line_two = input("Enter the other line").upper()
    angle_one = input("Enter one right angle").upper()
    angle_two = input("Enter another right angle").upper()

    chart_header()

    print("__                     |")
    print("{} is perpendicular    |".format(line_one))
    print("   __                  |")
    print("to {}                  | Definition of altitude".format(line_two))
    print("                       |")
    print("<{} and <{} are right|".format(angle_one, angle_two))
    print("angles                 | Definition of perpendicular lines")
    print("                       |")
    print("<{} and <{} are      |".format(angle_one, angle_two))
    print("congruent              | Right angles are congruent")
    print("                       |")
def median():
    midpoint_one = input("Enter midpoint").upper()
    line = input("Enter a line").upper()
    segment_one = input("Enter a segment").upper()
    segment_two = input("Enter another segment").upper()

    chart_header()

    print("{} is a midpoint of     |".format(midpoint_one))
    print("__                     |")
    print("{}                     | Definition of a median".format(line))
    print("                       |")
    print("__     __              |")
    print("{} and {}              |".format(segment_one, segment_two))
    print("are congruent          | Definition of a midpoint")


def segment_bisector():
    midpoint = input("Enter a midpoint").upper()
    line = input("Enter a line").upper()
    seg_one = input("Enter one congruent segment").upper()
    seg_two = input("Enter anther congruent segment").upper()

    chart_header()

    print("point {} is a           |".format(midpoint))
    print("            __         |")
    print("midpoint of {}         | Definition of a segment bisector".format(line))
    print("                       |")
    print("__                 __  |")
    print("{} is congruent to {}  | Definition of a midpoint".format(seg_one, seg_two))
    print("                       |")
def verticle_angles():
    va_one =input("Enter the first angle").upper()
    va_two = input("Enter the second angle").upper()

    chart_header()

    print("<{} and <{} are      |".format(va_one, va_two))
    print("verticle angles        | Definition of verticle angles")
    print("                       |")
    print("<{} and <{} are      | ".format(va_one, va_two))
    print("congruent              | Verticle angles are congruent")
    print("                       |")
def perpendicular():
    angle_one = input("Enter an angle").upper()
    angle_two = input("Enter angle two").upper()

    chart_header()

    print("<{} and <{} are      |".format(angle_one, angle_two))
    print("right angles           | Definition of perpendicular")
    print("                       |")
    print("<{} and <{} are      |".format(angle_one, angle_two))
    print("congruent              | Right angles are congruent")
    print("                       |")
def angle_bisector():
    angle_one = input("Enter an angle").upper()
    angle_two = input ("Enter another angle").upper()

    chart_header()

    print("<{} and <{} are      |".format(angle_one, angle_two))
    print("congruent              | Definition of angle bisector")
    print("                       |")

def congruence():
    line_one = input("Enter a line").upper()
    line_two = input("Enter another line").upper()

    chart_header()

    print("{} = {}                | Definition of congruent".format(line_one, line_two))

def transitive_property():
    pass

def addition_postulate():
    short_seg_one = input("Enter a short segment").upper()
    short_seg_two = input("Enter another short segment").upper()
    long_seg_one = input("Enter a long segment").upper()
    long_seg_two = input("Enter another long segment").upper()
    peice_same = input("Enter a piece that is in both long segments").upper()
    angles_lines = input("l for line and a for angle").upper()


    chart_header()

    if angles_lines == "L":

        print("{} is congruent to     |".format(peice_same))
        print("{}                     | Reflexive property".format(peice_same))
        print("                       |")
        print("{} = {} and {} = {}    | Definition of congruence".format(short_seg_one, short_seg_two, peice_same, peice_same))
        print("                       |")
        print("{} + {} = {} + {}      | Addition postulate".format(short_seg_one, peice_same, short_seg_two, peice_same))
        print("                       |")
        print("{} = {} + {}           |".format(long_seg_one, short_seg_one, peice_same))
        print("{} = {} + {}           | Partition postulate".format(long_seg_two, short_seg_two, peice_same))
        print("                       |")
        print("{} = {}                | Substitution postulate".format(long_seg_one, long_seg_two))
        print("                       |")
        print("__                     |")
        print("{} is congruent to     |".format(long_seg_one))
        print("__                     |")
        print("{}                     |".format(long_seg_two))
        print("                       |")

    else:

        print("<{} is congruent to     |".format(peice_same))
        print("<{}                     | Reflexive property".format(peice_same))
        print("                       |")
        print("m<{} = m<{} and        | Definition of congruence".format(short_seg_one, short_seg_two))
        print("m<{} = m<{}            |".format(peice_same, peice_same))
        print("                       |")
        print("m<{} + m<{} =          | Addition postulate".format(short_seg_one, peice_same))
        print("m<{} + m<{}            |".format(short_seg_two, peice_same))
        print("                       |")
        print("m<{} = m<{} + m<{}     |".format(long_seg_one, short_seg_one, peice_same))
        print("m<{} = m<{} + m<{}     | Partition postulate".format(long_seg_two, short_seg_two, peice_same))
        print("                       |")
        print("m<{} = m<{}            | Substitution postulate".format(long_seg_one, long_seg_two))
        print("                       |")
        print("m<{} is congruent to   |".format(long_seg_one))
        print("m<{}                   |".format(long_seg_two))
        print("                       |")

def subtraction_postulate():
    long_seg_one = input("Enter a long segment").upper()
    long_seg_two = input("Enter another long segment").upper()
    short_seg_one = input("Enter a short segment").upper()
    short_seg_two = input("Enter another short segment").upper()
    peice_same = input("Enter a piece that is in both long segments").upper()
    angles_lines = input("l for line and a for angle proof").upper()

    chart_header()

    if angles_lines == "L":

        print("{} is congruent to     |".format(peice_same))
        print("{}                     | Reflexive property".format(peice_same))
        print("                       |")
        print("{} = {} and {} = {}    | Definition of congruence".format(long_seg_one, long_seg_two, peice_same,peice_same))
        print("                       |")
        print("{} + {} = {} + {}      | Subtraction prostulate".format(long_seg_one, peice_same, long_seg_two, peice_same))
        print("                       |")
        print("{} = {} - {}           |".format(short_seg_one, long_seg_one, peice_same))
        print("{} = {} - {}           | Partition postulate".format(short_seg_two, long_seg_two, peice_same))
        print("                       |")
        print("{} = {}                | Substitution postulate".format(short_seg_one, short_seg_two))
        print("                       |")
        print("__                     |")
        print("{} is congruent to     |".format(short_seg_one))
        print("__                     |")
        print("{}                     |".format(short_seg_two))
        print("                       |")

    else:

        print("<{} is congruent to     |".format(peice_same))
        print("<{}                     | Reflexive property".format(peice_same))
        print("                       |")
        print("m<{} = m<{} and        | Definition of congruence".format(long_seg_one, long_seg_two))
        print("m<{} = m<{}            |".format(peice_same, peice_same))
        print("                       |")
        print("m<{} - m<{} =          | Subtraction postulate".format(long_seg_one, peice_same))
        print("m<{} - m<{}            |".format(long_seg_two, peice_same))
        print("                       |")
        print("m<{} = m<{} - m<{}     |".format(short_seg_one, long_seg_one, peice_same))
        print("m<{} = m<{} - m<{}     | Partition postulate".format(short_seg_two, long_seg_two, peice_same))
        print("                       |")
        print("m<{} = m<{}            | Substitution postulate".format(short_seg_one, short_seg_two))
        print("                       |")
        print("m<{} is congruent to   |".format(short_seg_one))
        print("m<{}                   |".format(short_seg_two))
        print("                       |")



def main():
    print("type lp, a, m, sb, va, p, ag, c, tp, ap, sp ")
    print("(Linear pairs, altitude, median, segment bisector, verticle angles, perpendicular,")
    print("angle bisector, congruence, transitive property, addition postulate, subtraction postulate)")
    which_one = input()

    if which_one == "lp":
        linear_pairs()
    elif which_one == "a":
        altitude()
    elif which_one == "m":
        median()
    elif which_one == "sb":
        segment_bisector()
    elif which_one == "va":
        verticle_angles()
    elif which_one == "p":
        perpendicular()
    elif which_one == "ag":
        angle_bisector()
    elif which_one == "c":
        congruence()
    elif which_one == "tp":
        transitive_property()
    elif which_one == "ap":
        addition_postulate()
    elif which_one == "sp":
        subtraction_postulate()
    else:
        exit()

main()

def U_continue():
    what_u_want = input("do you want to run the program again y/n?").upper()
    if what_u_want == "Y":
        return True
    else:
        return False

while U_continue() == True:
    main()