
def cube (a):
    b = a ** 3
    c = (4 * a) ** 2
    return b, c

cube_volume, cube_area = cube(4)

print('Объем куба равен =', cube_volume)
print('Площадь одной грани куба равна =', cube_area)

exit()

edge_cube = 5
cube_volume = edge_cube ** 5
cube_area = edge_cube ** 2 * 4
print('Объем куба равен =', cube_volume)
print('Площадь одной грани куба равна =', cube_area)
