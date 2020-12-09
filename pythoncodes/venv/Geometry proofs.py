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
def defi_verticle_angles():
    va_one = input("Enter the first angle").upper()
    va_two = input("Enter the second angle").upper()

    chart_header()

    print("<{} and <{} are      |".format(va_one, va_two))
    print("verticle angles        | Definition of verticle angles")
    print("                       |")
def right_angles_congruent():
    angle_one = input("Enter an angle").upper()
    angle_two = input("Enter angle two").upper()

    chart_header()

    print("<{} and <{} are      |".format(angle_one, angle_two))
    print("congruent              | Right angles are congruent")
    print("                       |")
def defi_altitude():
    line_one = input("Enter the line that is an altitude").upper()
    line_two = input("Enter the other line").upper()

    chart_header()

    print("__                     |")
    print("{} is perpendicular    |".format(line_one))
    print("   __                  |")
    print("to {}                  | Definition of altitude".format(line_two))
    print("                       |")
def transitive_property_one():
    equal_congruent = input("Equality or congruence? e/c").upper()
    angle_segment = input("angle or aegment a/s").upper()
    thing_one = input("thing one").upper()
    thing_two = input("thing two").upper()

    chart_header()

    if equal_congruent == "E" and angle_segment == "A":
        print("m<{} = m<{}          |".format(thing_one, thing_two))
        print("                       |")
    elif equal_congruent == "E" and angle_segment == "S":
        print("{} = {}                |".format(thing_one, thing_two))
        print("                       |")
    elif equal_congruent == "C" and angle_segment == "A":
        print("<{} is congruent to   |".format(thing_one))
        print("<{}                   |".format(thing_two))
        print("                       |")
    elif equal_congruent == "C" and angle_segment == "S":
        print("__                 __  |")
        print("{} is congruent to {}  |".format(thing_one, thing_two))
        print("                       |")

def substitution_postulate():
    num_lines = input("How many lines do you need? 1-3")
    if num_lines == "1":
        thing_one = input("Enter what you want on the line(Must be 23 characters)")
        print("{}|".format(thing_one))
        print("                       |")
    elif num_lines == "2":
        thing_one = input("Enter what you want on the line(Must be 23 characters)")
        thing_two = input("Enter what you want on the line(Must be 23 characters)")
        print("{}|".format(thing_one))
        print("{}|".format(thing_two))
        print("                       |")
    elif num_lines == "3":
        thing_one = input("Enter what you want on the line(Must be 23 characters)")
        thing_two = input("Enter what you want on the line(Must be 23 characters)")
        thing_three = input("Enter what you want on the line(Must be 23 characters)")
        print("{}|".format(thing_one))
        print("{}|".format(thing_two))
        print("{}|".format(thing_three))
        print("                       |")
def addition_postulate_one():
    pass
def subtraction_postulate_one():
    pass
def halves_postulate():
    pass
def partition_postulate():
    pass

def midpoint():
    segment_one = input("Enter a segment").upper()
    segment_two = input("Enter another segment").upper()

    chart_header()

    print("__     __              |")
    print("{} and {}              |".format(segment_one, segment_two))
    print("are congruent          | Definition of a midpoint")

def linear_pairs():
    state_congruence = input("Do you want to state congruence y/n").upper()
    # angle_one and #angle_two are adjacent. angle_three and angle_four are adjacent
    angle_one = input("Enter a given angle").upper()
    angle_two = input("Enter angle your trying to prove").upper()
    angle_three = input("Enter annother given angle").upper()
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
    if state_congruence == "Y":
        print("<{} and <{}          |".format(angle_two, angle_four))
        print("are congruent          | Suppliments of congruent angles are congruent")
        print("                       |")
def altitude():
    state_congruence = input("Do you want to state congruence y/n").upper()
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
    if state_congruence =="Y":
        print("<{} and <{} are      |".format(angle_one, angle_two))
        print("congruent              | Right angles are congruent")
        print("                       |")
def median():
    state_congruence =input("Do you want to state congruence y/n").upper()
    # Segment_one and segment_two form line which is split by midpoint_one
    midpoint_one = input("Enter midpoint").upper()
    line = input("Enter a line").upper()
    segment_one = input("Enter a segment").upper()
    segment_two = input("Enter another segment").upper()

    chart_header()

    print("{} is a midpoint of     |".format(midpoint_one))
    print("__                     |")
    print("{}                     | Definition of a median".format(line))
    print("                       |")
    if state_congruence == "Y":
        print("__     __              |")
        print("{} and {}              |".format(segment_one, segment_two))
        print("are congruent          | Definition of a midpoint")


def segment_bisector():
    state_congruence = input("Do you want to state congruence y/n").upper()
    # Segment_one and segment_two form line which is split by midpoint_one
    midpoint = input("Enter a midpoint").upper()
    line = input("Enter a line").upper()
    seg_one = input("Enter one congruent segment").upper()
    seg_two = input("Enter anther congruent segment").upper()

    chart_header()

    print("point {} is a           |".format(midpoint))
    print("            __         |")
    print("midpoint of {}         | Definition of a segment bisector".format(line))
    print("                       |")
    if state_congruence == "Y":
        print("__                 __  |")
        print("{} is congruent to {}  | Definition of a midpoint".format(seg_one, seg_two))
        print("                       |")
def verticle_angles():
    state_congruence = input("Do you want to state congruence").upper()
    va_one =input("Enter the first angle").upper()
    va_two = input("Enter the second angle").upper()

    chart_header()

    print("<{} and <{} are      |".format(va_one, va_two))
    print("verticle angles        | Definition of verticle angles")
    print("                       |")
    if state_congruence == "Y":
        print("<{} and <{} are      | ".format(va_one, va_two))
        print("congruent              | Verticle angles are congruent")
        print("                       |")
def perpendicular():
    state_congruence = input("Do you want to state congruence").upper()
    angle_one = input("Enter an angle").upper()
    angle_two = input("Enter angle two").upper()

    chart_header()

    print("<{} and <{} are      |".format(angle_one, angle_two))
    print("right angles           | Definition of perpendicular")
    print("                       |")
    if state_congruence == "Y":
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
    shapes_numbers = input("Use shapes or numbers s/h").upper()
    lines_angles = input("Use angles or lines a/l").upper()
    piece_one = input("Enter one piece").upper()
    piece_two = input("Enter another piece").upper()
    piece_three = input("Enter another piece").upper()

    if shapes_numbers == "S":
        if lines_angles == "L":
            print("__                  __ |")
            print("{} is congruent to  {} | Transitive Property".format(piece_one, piece_two))
            print("                       |")
            print("__                  __ |")
            print("{} is congruent to  {} | Transitive Property".format(piece_two, piece_three))
            print("                       |")
        elif lines_angles == "A":
            print("<{} is congruent to   | Transitive Property".format(piece_one))
            print("<{}                   |".format(piece_two))
            print("                       |")
            print("<{} is congruent to   | Transitive Property".format(piece_two))
            print("<{}                   |".format(piece_three))
            print("                       |")
    elif shapes_numbers == "N":
        if lines_angles == "L":
            print("{} = {}                | Transitive Property".format(piece_one, piece_two))
            print("                       |")
            print("{} = {}                | transitive Property".format(piece_two, piece_three))
            print("                       |")
        elif lines_angles == "A":
            print("m<{} = m<{}           | Transitive Property".format(piece_one, piece_two))
            print("                       |")
            print("m<{} = m<{}           | Transitive Property".format(piece_two, piece_three))
            print("                       |")

def addition_postulate():
    state_congruence = input("Do you want to state congruence").upper()
    reflex = input("Include reflexive property? y/n").upper()
    shapes_numbers = input("Include shapes to numbers? y/n").upper()
    short_seg_one = input("Enter a short segment").upper()
    short_seg_two = input("Enter another short segment").upper()
    long_seg_one = input("Enter a long segment").upper()
    long_seg_two = input("Enter another long segment").upper()
    if reflex == "Y":
        peice_same = input("Enter a piece that is in both long segments").upper()
    else:
        short_seg_three = input("Enter a short segment").upper()
        short_seg_four = input("enter another short segment").upper()
    angles_lines = input("l for line and a for angle").upper()


    chart_header()

    if angles_lines == "L":

        if reflex == "Y":
            print("{} is congruent to     |".format(peice_same))
            print("{}                     | Reflexive property".format(peice_same))
            print("                       |")
        if shapes_numbers == "Y":
            if reflex == "Y":
                print("{} = {} and {} = {}    | Definition of congruence".format(short_seg_one, short_seg_two, peice_same, peice_same))
                print("                       |")
            elif reflex == "N":
                print("{} = {} and {} = {}    | Definition of congruence".format(short_seg_one, short_seg_two, short_seg_three, short_seg_four))
                print("                       |")
        if reflex == "Y":
            print("{} + {} = {} + {}      | Addition postulate".format(short_seg_one, peice_same, short_seg_two, peice_same))
            print("                       |")
            print("{} = {} + {}           |".format(long_seg_one, short_seg_one, peice_same))
            print("{} = {} + {}           | Partition postulate".format(long_seg_two, short_seg_two, peice_same))
            print("                       |")
        elif reflex == "N":
            print("{} + {} = {} + {}      | Addition postulate".format(short_seg_one, short_seg_three, short_seg_two,short_seg_four))
            print("                       |")
            print("{} = {} + {}           |".format(long_seg_one, short_seg_one, short_seg_three))
            print("{} = {} + {}           | Partition postulate".format(long_seg_two, short_seg_two, short_seg_four))
            print("                       |")
        print("{} = {}                | Substitution postulate".format(long_seg_one, long_seg_two))
        print("                       |")
        if state_congruence == "Y":
            print("__                     |")
            print("{} is congruent to     |".format(long_seg_one))
            print("__                     |")
            print("{}                     |".format(long_seg_two))
            print("                       |")

    else:

        if reflex == "Y":
            print("<{} is congruent to     |".format(peice_same))
            print("<{}                     | Reflexive property".format(peice_same))
            print("                       |")
        if shapes_numbers == "Y":
            if reflex == "Y":
                print("m<{} = m<{} and        | Definition of congruence".format(short_seg_one, short_seg_two))
                print("m<{} = m<{}            |".format(peice_same, peice_same))
                print("                       |")
            elif reflex == "N":
                print("m<{} = m<{} and        | Definition of congruence".format(short_seg_one, short_seg_two))
                print("m<{} = m<{}            |".format(short_seg_three, short_seg_four))
                print("                       |")
        if reflex == "Y":
            print("m<{} + m<{} =          | Addition postulate".format(short_seg_one, peice_same))
            print("m<{} + m<{}            |".format(short_seg_two, peice_same))
            print("                       |")
            print("m<{} = m<{} + m<{}     |".format(long_seg_one, short_seg_one, peice_same))
            print("m<{} = m<{} + m<{}     | Partition postulate".format(long_seg_two, short_seg_two, peice_same))
            print("                       |")
        elif reflex == "N":
            print("m<{} + m<{} =          | Addition postulate".format(short_seg_one, short_seg_three))
            print("m<{} + m<{}            |".format(short_seg_two, short_seg_four))
            print("                       |")
            print("m<{} = m<{} + m<{}     |".format(long_seg_one, short_seg_one, peice_same))
            print("m<{} = m<{} + m<{}     | Partition postulate".format(long_seg_two, short_seg_two, peice_same))
            print("                       |")
        print("m<{} = m<{}            | Substitution postulate".format(long_seg_one, long_seg_two))
        print("                       |")
        if state_congruence == "Y":
            print("m<{} is congruent to   |".format(long_seg_one))
            print("m<{}                   |".format(long_seg_two))
            print("                       |")

def subtraction_postulate():
    state_congruence = input("Do you want to state congruence").upper()
    reflex = input("Include reflexive property? y/n").upper()
    shapes_numbers = input("Include shapes to numbers? y/n").upper()
    long_seg_one = input("Enter a long segment").upper()
    long_seg_two = input("Enter another long segment").upper()
    short_seg_one = input("Enter a short segment").upper()
    short_seg_two = input("Enter another short segment").upper()
    angles_lines = input("l for line and a for angle proof").upper()
    if reflex == "Y":
        peice_same = input("Enter a piece that is in both long segments").upper()
    else:
        short_seg_three = input("Enter a short segment").upper()
        short_seg_four = input("enter another short segment").upper()

    chart_header()

    if angles_lines == "L":

        if reflex == "Y":
            print("{} is congruent to     |".format(peice_same))
            print("{}                     | Reflexive property".format(peice_same))
            print("                       |")
        if shapes_numbers == "Y":
            if reflex == "Y":
                print("{} = {} and {} = {}    | Definition of congruence".format(long_seg_one, long_seg_two, peice_same,peice_same))
                print("                       |")
            elif reflex == "N":
                print("{} = {} and {} = {}    | Definition of congruence".format(long_seg_one, long_seg_two, short_seg_three,short_seg_four))
                print("                       |")
        if reflex == "Y":
            print("{} - {} = {} - {}      | Subtraction prostulate".format(long_seg_one, peice_same, long_seg_two, peice_same))
            print("                       |")
            print("{} = {} - {}           |".format(short_seg_one, long_seg_one, peice_same))
            print("{} = {} - {}           | Partition postulate".format(short_seg_two, long_seg_two, peice_same))
            print("                       |")
        elif reflex == "N":
            print("{} - {} = {} - {}      | Subtraction prostulate".format(long_seg_one,short_seg_three, long_seg_two, short_seg_four))
            print("                       |")
            print("{} = {} - {}           |".format(short_seg_one, long_seg_one, short_seg_three))
            print("{} = {} - {}           | Partition postulate".format(short_seg_two, long_seg_two, short_seg_four))
            print("                       |")
        print("{} = {}                | Substitution postulate".format(short_seg_one, short_seg_two))
        print("                       |")
        if state_congruence == "Y":
            print("__                     |")
            print("{} is congruent to     |".format(short_seg_one))
            print("__                     |")
            print("{}                     |".format(short_seg_two))
            print("                       |")

    else:

        if reflex == "Y":
            print("<{} is congruent to     |".format(peice_same))
            print("<{}                     | Reflexive property".format(peice_same))
            print("                       |")
        if shapes_numbers == "Y":
            if reflex == "Y":
                print("m<{} = m<{} and        | Definition of congruence".format(long_seg_one, long_seg_two))
                print("m<{} = m<{}            |".format(peice_same, peice_same))
                print("                       |")
            elif reflex == "N":
                print("m<{} = m<{} and        | Definition of congruence".format(long_seg_one, long_seg_two))
                print("m<{} = m<{}            |".format(short_seg_three, short_seg_four))
                print("                       |")
        if reflex == "Y":
            print("m<{} - m<{} =          | Subtraction postulate".format(long_seg_one, peice_same))
            print("m<{} - m<{}            |".format(long_seg_two, peice_same))
            print("                       |")
            print("m<{} = m<{} - m<{}     |".format(short_seg_one, long_seg_one, peice_same))
            print("m<{} = m<{} - m<{}     | Partition postulate".format(short_seg_two, long_seg_two, peice_same))
            print("                       |")
        elif reflex == "Y":
            print("m<{} - m<{} =          | Subtraction postulate".format(long_seg_one, short_seg_three))
            print("m<{} - m<{}            |".format(long_seg_two, short_seg_four))
            print("                       |")
            print("m<{} = m<{} - m<{}     |".format(short_seg_one, long_seg_one, short_seg_three))
            print("m<{} = m<{} - m<{}     | Partition postulate".format(short_seg_two, long_seg_two, short_seg_four))
            print("                       |")
        print("m<{} = m<{}            | Substitution postulate".format(short_seg_one, short_seg_two))
        print("                       |")
        if state_congruence == "Y":
            print("m<{} is congruent to   |".format(short_seg_one))
            print("m<{}                   |".format(short_seg_two))
            print("                       |")


def halves():
    seg_angle_bisector = input("Midpoint or angle bisector m/ab").upper()
    shapes_numbers = input("Do you want to convert shapes to numbers y/n").upper()
    state_congruence = input("Do you want to state congruence y/n").upper()
    if seg_angle_bisector == "AB":
        # whole_seg_one and whole_seg_two get bisected
        whole_angle_one = input("Enter one whole angle").upper()
        whole_angle_two = input("Enter another whole angle").upper()
        ab_one = input("Enter an angle bisector").upper()
        #bisected_one and bisected_two are congruent and bisected_three and bisected_four are congruent
        #You are trying to prove bisected_one is congruent to bisected_three
        bisected_one = input("Enter the angle created by bisector").upper()
        bisected_two = input("Enter another angle created by bisector").upper()
        ab_two = input("Enter another angle bisector").upper()
        bisected_three = input("Enter the angle created by bisector").upper()
        bisected_four = input("Enter the angle created by bisector").upper()
    elif seg_angle_bisector == "M":
        # whole_seg_one and whole_seg_two get bisected
        whole_seg_one = input("Enter one whole segment").upper()
        whole_seg_two = input("Enter another whole segment").upper()
        m_one = input("Enter an midpoint").upper()
        #bisected_one and bisected_two are congruent and bisected_three and bisected_four are congruent
        #You are trying to prove bisected_one is congruent to bisected_three
        bisected_one = input("Enter the segment created by bisector").upper()
        bisected_two = input("Enter another segment created by bisector").upper()
        m_two = input("Enter another segment bisector").upper()
        bisected_three = input("Enter the segment created by bisector").upper()
        bisected_four = input("Enter the segment created by bisector").upper()

    chart_header()

    if seg_angle_bisector == "AB":
        print("<{} is congruent to   |".format(bisected_one))
        print("<{} and <{} is       | Definition of Angle Bisector".format(bisected_two, bisected_three))
        print("congruent to <{}      |".format(bisected_four))
        print("                       |")
    elif seg_angle_bisector == "M":
        print("__                 __  |")
        print("{} is congruent to {}  |".format(bisected_one, bisected_two))
        print("    __                 |")
        print("and {} is              | Definition of Midpoint".format(bisected_three))
        print("             __        |")
        print("congruent to {}        |".format(bisected_four))
        print("                       |")
    if shapes_numbers == "Y":
        if seg_angle_bisector == "M":
            print("{} = {} and {} = {}    | Definition of congruence".format(bisected_one,bisected_two, bisected_three, bisected_four))
            print("{} = {}                |".format(whole_seg_one, whole_seg_two))
            print("                       |")
        elif seg_angle_bisector == "AB":
            print("m<{} = m<{}, m<{} = | Definition of congruence".format(bisected_one, bisected_two, bisected_three))
            print("m<{}, m<{} = m<{}   |".format(bisected_four, whole_angle_one, whole_angle_two))
            print("                       |")
    if seg_angle_bisector == "M":
        #partition, 2x substitution, halves
        print("{} = {} + {}           |".format(whole_seg_one, bisected_one, bisected_two))
        print("{} = {} + {}           | Partition Postulate".format(whole_seg_two, bisected_three, bisected_four))
        print("                       |")
        print("{} = 2 {}              |".format(whole_seg_one, bisected_one))
        print("{} = 2 {}              | Substitution Postulate".format(whole_seg_two, bisected_three))
        print("                       |")
        print("2 {} = 2 {}            | Substitution Postulate".format(bisected_one, bisected_three))
        print("                       |")
        print("{} = {}                | Halves Postulate".format(bisected_one, bisected_three))
        print("                       |")

    elif seg_angle_bisector =="AB":
        # partition, 2x substitution, halves
        print("m<{} = m<{} + m<{}  |".format(whole_angle_one, bisected_one, bisected_two))
        print("m<{} = m<{} + m<{}  | Partition Postulate".format(whole_angle_two, bisected_three, bisected_four))
        print("                       |")
        print("m<{} = 2 m<{}        |".format(whole_angle_one, bisected_one))
        print("m<{} = 2 m<{}        | Substitution Postulate".format(whole_angle_two, bisected_three))
        print("                       |")
        print("2 m<{} = 2 m<{}      | Substitution Postulate".format(bisected_one, bisected_three))
        print("                       |")
        print("m<{} = m<{}          | Halves Postulate".format(bisected_one, bisected_three))
        print("                       |")
    if state_congruence == "Y":
        if seg_angle_bisector == "M":
            print("__                     |")
            print("{} is congruent to     |".format(bisected_one))
            print("__                     |")
            print("{}                     |".format(bisected_three))
            print("                       |")
        elif seg_angle_bisector == "AB":
            print("m<{} is congruent to   |".format(bisected_one))
            print("m<{}                   |".format(bisected_three))
            print("                       |")
def main():
    print("type lp, a, m, sb, va, p, ag, c, tp, ap, sp, h, o ")
    print("(Linear pairs, altitude, median, segment bisector, verticle angles, perpendicular,")
    print("angle bisector, congruence, transitive property, addition postulate, subtraction postulate, halves, other)")
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
    elif which_one == "h":
        halves()
    elif which_one == "o":
        pass
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