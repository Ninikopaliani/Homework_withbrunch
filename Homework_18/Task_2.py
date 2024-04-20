def midpoint(x1, y1, x2, y2):
    mid_x = (x1 + x2) // 2
    mid_y = (y1 + y2) // 2
    return mid_x, mid_y


def main():
    mid_x, mid_y = midpoint(26, 1, 456, 194)
    print("Middle of the point x1 and x2 is: ", mid_x)
    print("Middle of the point y1 and y2 is: ", mid_y)


if __name__ == '__main__':
    main()