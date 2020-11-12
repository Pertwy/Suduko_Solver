grid1 = [[5, 3, 10, 10, 7, 10, 10, 10, 10],
         [6, 10, 10, 1, 9, 5, 10, 10, 10],
         [10, 9, 8, 10, 10, 10, 10, 6, 10],
         [8, 10, 10, 10, 6, 10, 10, 10, 3],
         [4, 10, 10, 8, 10, 3, 10, 10, 1],
         [7, 10, 10, 10, 2, 10, 10, 10, 6],
         [10, 6, 10, 10, 10, 10, 2, 8, 10],
         [10, 10, 10, 4, 1, 9, 10, 10, 5],
         [10, 10, 10, 10, 8, 10, 10, 7, 9]]

grid3 = [[9, 10, 10, 10, 1, 10, 10, 10, 2],
         [4, 1, 10, 10, 6, 3, 10, 10, 9],
         [10, 3, 2, 10, 10, 4, 6, 10, 10],
         [10, 10, 10, 3, 4, 10, 10, 10, 10],
         [10, 2, 8, 10, 10, 10, 10, 10, 10],
         [10, 10, 10, 5, 2, 10, 10, 10, 10],
         [10, 8, 1, 10, 10, 5, 3, 10, 10],
         [2, 7, 10, 10, 3, 1, 10, 10, 5],
         [5, 10, 10, 10, 8, 10, 10, 10, 4]]

grid4 = [[10, 10, 10, 6, 5, 10, 10, 10, 10],
         [10, 10, 8, 4, 10, 10, 9, 1, 10],
         [10, 10, 10, 10, 10, 10, 10, 8, 3],
         [10, 6, 10, 10, 10, 10, 10, 10, 10],
         [3, 5, 10, 10, 10, 10, 10, 10, 1],
         [10, 1, 9, 7, 10, 10, 10, 5, 10],
         [10, 10, 7, 10, 10, 10, 10, 10, 2],
         [1, 10, 10, 10, 10, 10, 10, 10, 10],
         [10, 10, 10, 10, 2, 9, 7, 6, 10]]


grid = [[10, 10, 1, 10, 10, 4, 10, 7, 10],
        [6, 4, 10, 2, 10, 10, 10, 10, 10],
        [8, 10, 10, 10, 1, 10, 5, 10, 9],
        [4, 10, 10, 10, 10, 2, 10, 10, 10],
        [10, 10, 10, 1, 9, 10, 10, 8, 10],
        [10, 10, 10, 7, 10, 10, 3, 10, 10],
        [3, 10, 10, 5, 10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10, 10, 7, 6, 10],
        [9, 10, 10, 10, 7, 8, 4, 10, 10]]

new_grid = grid

col_nums = []
square_nums = []
check_col_nums = []
check_row_nums = []
check_square_nums = []

new_grid_counter = 150


# def x_out():
#   pass
yep = 100

# while new_grid_counter > 1:
while yep > 1:
    print(new_grid_counter)

    for tile in range(1, 10):

        # XOut ===================================================================================================================
        for a in range(0, 3):
            for b in range(0, 3):
                # Collect numbers in each large square
                for c in range(0, 3):
                    for d in range(0, 3):
                        square_nums.append(new_grid[(a*3)+c][(b*3)+d])
                # Check that tile is in that square
                for c in range(0, 3):
                    for d in range(0, 3):
                        if new_grid[(a*3)+c][(b*3)+d] == 10 and (tile in square_nums):
                            new_grid[(a*3)+c][(b*3)+d] = "x"
                square_nums = []

        for x in range(0, 9):
            for z in range(0, 9):
                # Check the column
                if new_grid[z][x] != 10 and new_grid[z][x] != "x":
                    col_nums.append(new_grid[z][x])

            for y in range(0, 9):
                # See if tile is in the column
                if new_grid[y][x] == 10 and (tile in col_nums):
                    new_grid[y][x] = "x"

                # See if tile is in the row
                if new_grid[x][y] == 10 and (tile in new_grid[x]):
                    new_grid[x][y] = "x"

            col_nums = []


# Check squares ===================================================================================================================

        for a in range(0, 3):
            for b in range(0, 3):
                # Collect numbers in each large square
                for c in range(0, 3):
                    for d in range(0, 3):
                        check_square_nums.append(new_grid[(a*3)+c][(b*3)+d])
                count = check_square_nums.count(10)
                if count == 1:
                    ind = check_square_nums.index(10)
                    Ex = (ind % 3)
                    Why = int((ind - Ex)/3)
                    new_grid[(a*3)+Why][(b*3)+Ex] = tile
                    for J in new_grid:
                        print(J)
                    print("")
                check_square_nums = []

# XOut =========================================================================================================================

        for a in range(0, 3):
            for b in range(0, 3):
                # Collect numbers in each large square
                for c in range(0, 3):
                    for d in range(0, 3):
                        square_nums.append(new_grid[(a*3)+c][(b*3)+d])
                # Check that tile is in that square
                for c in range(0, 3):
                    for d in range(0, 3):
                        if new_grid[(a*3)+c][(b*3)+d] == 10 and (tile in square_nums):
                            new_grid[(a*3)+c][(b*3)+d] = "x"
                square_nums = []

        for x in range(0, 9):
            for z in range(0, 9):
                # Check the column
                if new_grid[z][x] != 10 and new_grid[z][x] != "x":
                    col_nums.append(new_grid[z][x])

            for y in range(0, 9):
                # See if tile is in the column
                if new_grid[y][x] == 10 and (tile in col_nums):
                    new_grid[y][x] = "x"

                # See if tile is in the row
                if new_grid[x][y] == 10 and (tile in new_grid[x]):
                    new_grid[x][y] = "x"

            col_nums = []


# Check rows ===================================================================================================================

        for x in range(0, 9):

            for y in range(0, 9):
                if new_grid[x][y] == 10:
                    check_row_nums.append([x, y])

            if len(check_row_nums) == 1:
                Ex = check_row_nums[0][0]
                Why = check_row_nums[0][1]
                new_grid[Ex][Why] = tile
                for J in new_grid:
                    print(J)
                print("")
            check_row_nums = []

# X out =================================================================================================================================

        for a in range(0, 3):
            for b in range(0, 3):
                # Collect numbers in each large square
                for c in range(0, 3):
                    for d in range(0, 3):
                        square_nums.append(new_grid[(a*3)+c][(b*3)+d])
                # Check that tile is in that square
                for c in range(0, 3):
                    for d in range(0, 3):
                        if new_grid[(a*3)+c][(b*3)+d] == 10 and (tile in square_nums):
                            new_grid[(a*3)+c][(b*3)+d] = "x"
                square_nums = []

        for x in range(0, 9):
            for z in range(0, 9):
                # Check the column
                if new_grid[z][x] != 10 and new_grid[z][x] != "x":
                    col_nums.append(new_grid[z][x])

            for y in range(0, 9):
                # See if tile is in the column
                if new_grid[y][x] == 10 and (tile in col_nums):
                    new_grid[y][x] = "x"

                # See if tile is in the row
                if new_grid[x][y] == 10 and (tile in new_grid[x]):
                    new_grid[x][y] = "x"

            col_nums = []

# Check columns ================================================================================================================

            for z in range(0, 9):
                # Check the column
                if new_grid[z][x] == 10:
                    check_col_nums.append([x, z])

            if len(check_col_nums) == 1:
                Ex = check_col_nums[0][0]
                Why = check_col_nums[0][1]
                new_grid[Why][Ex] = tile
                for J in new_grid:
                    print(J)
                print("")

            check_col_nums = []

# Reset the table to 10s =========================================================================================================

        for x in range(0, 9):
            for y in range(0, 9):
                if new_grid[x][y] == "x":
                    new_grid[x][y] = 10

        new_grid_counter = 0

        for x in range(0, 9):
            for y in range(0, 9):
                if new_grid[x][y] == 10:
                    new_grid_counter += 1

        yep -= 1
        print(new_grid_counter)


for J in new_grid:
    print(J)
print("")
