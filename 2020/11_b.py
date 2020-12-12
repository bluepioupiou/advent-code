import unittest
import itertools


def get_seats_from_file(file):
    file = open(file, 'r')
    lines = file.readlines()
    file_seats = [[file_seat for file_seat in line.strip()] for line in lines]
    file.close()
    return file_seats


def get_number_of_occupied_seats(test_seats, a, b):
    occupied = 0
    # print("inspecting neighbors for cell {}-{}:{}".format(i, j, seat))
    for x, y in list(itertools.product(range(-1, 2), range(-1, 2))):
        if x != 0 or y != 0:
            for multiply in range(1, 9):
                new_i = (a + multiply * x)
                new_j = (b + multiply * y)
                if 0 <= new_i < len(test_seats) and 0 <= new_j < len(test_seats[a]):
                    # print("-- neighbor {}/{}:{}".format(i + x, j + y, seats[i + x][j + y]))
                    neighbour = test_seats[new_i][new_j]
                    if neighbour == "#":
                        occupied += 1
                        break
                    if neighbour == "L":
                        break
    return occupied


def get_result_seats_from_previous_state(previous):
    result = []
    for i, row in enumerate(previous):
        new_row = []
        for j, seat in enumerate(row):
            visible_occupied = get_number_of_occupied_seats(previous, i, j)
            if seat == "#" and visible_occupied >= 5:
                new_row.append("L")
            elif seat == "L" and visible_occupied == 0:
                new_row.append("#")
            else:
                new_row.append(seat)

        result.append(new_row)
    return result


def format_for_console(array):
    return "\n".join(["".join(row) for row in array])


# Strips the newline character
def main():
    seats = get_seats_from_file('11.txt')
    print("from \n{}".format("\n".join(["".join(row) for row in seats])))
    while True:
        result = get_result_seats_from_previous_state(seats)
        # print("from \n{}".format("\n".join(["".join(row) for row in seats])))
        print("to \n{}".format(format_for_console(result)))
        if format_for_console(result) == format_for_console(seats):
            break
        else:
            seats = result
    print("found {}".format(sum([row.count("#") for row in result])))


if __name__ == "__main__":
    main()


class Test11(unittest.TestCase):
    def test_get_number_of_occupied_seats_simple(self):
        test_seats = get_seats_from_file('test_11_8.txt')
        self.assertEqual(get_number_of_occupied_seats(test_seats, 4, 3), 8)

    def test_get_number_of_occupied_seats_hidden(self):
        test_seats = get_seats_from_file('test_11_L.txt')
        self.assertEqual(get_number_of_occupied_seats(test_seats, 1, 1), 0)

    def test_get_number_of_occupied_seats_empty_visible(self):
        test_seats = get_seats_from_file('test_11_empty.txt')
        self.assertEqual(get_number_of_occupied_seats(test_seats, 3, 3), 0)

    def test_get_result_seats_from_previous_state_1(self):
        test_seats = get_seats_from_file('test_11_transform1.txt')
        result_seats = get_seats_from_file('test_11_transform2.txt')
        result = get_result_seats_from_previous_state(test_seats)
        self.assertEqual(format_for_console(result_seats), format_for_console(result))
