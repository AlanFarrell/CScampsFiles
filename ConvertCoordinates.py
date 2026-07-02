from math import sqrt, atan2, degrees

def coordinateCovert(satellite_position):
    x, y, z = satellite_position
    lat = atan2(z, sqrt(x * x + y * y))
    lon = atan2(y, x)

    return degrees(lat), degrees(lon)