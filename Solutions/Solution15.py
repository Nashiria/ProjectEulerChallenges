# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?


def Way(dimension):
    length=dimension*2
    pascal=[1]
    for _ in range(length):
        pascal=[1]+[pascal[i]+pascal[i+1] for i in range(len(pascal)-1)]+[1]
    return pascal[len(pascal)//2]
print(Way(20))
