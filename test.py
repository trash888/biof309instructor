import argparse

parser = argparse.ArgumentParser(description="our countdown")
parser.add_argument("y", help="start int", type=int)
parser.add_argument("x", help="stop int", type=int)

args = parser.parse_args()

def countdown_from_y_to_x(y, x):
    """greatest function ever"""
    if (y > x):
        #y is greater than x
        print("y:", y, "x:", x)
        i=y
        while i>=x:
            #do something
            print(i)
            i=i-1
    else:
        #less than 25
        print("first number is equal or smaller. halting.")
    return("success")

countdown_from_y_to_x(args.y, args.x)
