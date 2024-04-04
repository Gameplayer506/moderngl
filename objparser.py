
def obj_parse(filename):
    def intlist(inlist):
        outlist = []
        for each in inlist:
            outlist.append(int(each))
        return outlist
    with open(filename, "r") as file:
        line = file.readline()

        vertices = []
        indices = []

        while line:
            if line[0] == "v" and line[1] == " ":
                points = line.split(" ")
                
                xyz = (float(points[1]), float(points[3]), float(points[2]))
                vertices.append(tuple(xyz))
            elif line[0] == "f":
                verts = line.split(" ")
                for i in range(len(verts)-3):
                    a = intlist(verts[1].split("/"))
                    b = intlist(verts[3+i].split("/"))
                    c = intlist(verts[2+i].split("/"))
                    indices.append((a,b,c))


            line = file.readline()
    return [vertices, indices]
if __name__ == "__main__":
    print(obj_parse("cube.obj")[0], "\n", obj_parse("cube.obj")[1])