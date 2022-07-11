print("""
##### Section study #####
This script computes the calculations required to find the moment of inertia of a given section. Instructions:
 - Divide the section in elementary subsections (as rectangles, triangles, ...)
 - For each section, insert the required data
 - Press return to terminate the data collection""")

sections = []
i = 1
while True:
    print("\nSection {}".format(i))
    height = input("Height [mm]:                      ")
    if height == "":
        print("\033[A\033[A")
        print("\033[A\033[A")
        break
    
    sections.append({
        "number": i,
        "height": float(height),
        "width":  float(input("Width [mm]:                       ")),
        "gravcen":float(input("Height of center of gravity [mm]: ")),
        "type":   input("Type of section [R rectangle, T triangle]: ")
    })
    i += 1


A_tot = 0
S_tot = 0
I_tot = 0

for section in sections:
    section['area'] = section['width']*section['height'] if section["type"] == "R" else 0.5*section['width']*section['height']
    section['static moment'] = section['area']*section['gravcen']
    section['local inertia'] = section['width']*pow(section['height'],3)/12 if section["type"] == "R" else section['width']*pow(section['height'],3)/36

    A_tot += section['area']
    S_tot += section['static moment']

y_gravcen = S_tot/A_tot

for section in sections:
    section['shift'] = section['area']*pow((section['gravcen']-y_gravcen),2)
    section['global inertia'] = section['local inertia']+section['shift']
    I_tot += section['global inertia']

print("Area:\t%f mm^2\nS_tot:\t%f mm^3\nI_tot:\t%f mm^4\n"%(A_tot, S_tot, I_tot))
print("Sec |   Area  | StatMom | LocIner |  Shift  | GlobIn")
for section in sections:
    print("{0:02d}. | {1:7.1f} | {2:7.1f} | {3:7.1f} | {4:7.1f} | {5:7.1f}".format(section['number'], section['area'], section['static moment'], section['local inertia'], section['shift'], section['global inertia']))