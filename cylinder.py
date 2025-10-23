#cylinder volume and surface area
import math
radius=float(input("ENTER THE RADIUS OF THE CYLINDER"))
height=float(input("ENTER THE HEIGHT OF THE CYLINDER"))
volume=math.pi*radius**2*height
surfacearea=2*math.pi*radius*(radius+height)
print("THE VOLUME OF THE CYLINDER IS", volume)
print("THE SURFACE AREA OF THE CYLINDER IS", surfacearea)
