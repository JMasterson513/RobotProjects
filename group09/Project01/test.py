perimeter = 2.0
velocity = .150

def sideLength(N):
    return perimeter / N

def sideDriveTime(N):
    sideLength = sideLength(N)
    return sideLength / velocity

def totalAngle(N):
    return (N-2)*180

def interiorAngle(N):
    totalAngle = totalAngle(N)
    
