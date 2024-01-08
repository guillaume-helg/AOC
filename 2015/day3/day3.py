class HouseLocation:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def set_location(self, direction):
        match direction:
            case '^': self.latitude += 1
            case '>': self.longitude += 1
            case 'v': self.latitude -= 1
            case '<': self.longitude -= 1

    def get_location(self):
        return self.latitude, self.longitude


def partie1(lignes):
    hl = HouseLocation(0, 0)
    v = set()

    for c in lignes:
        hl.set_location(c)
        v.add(hl.get_location())

    return len(v)


def partie2(lignes):
    hls = HouseLocation(0, 0)
    hlsr = HouseLocation(0, 0)
    v = set()

    for i in range(0, len(lignes), 2):
        hls.set_location(lignes[i])
        hlsr.set_location(lignes[i+1])
        v.add(hls.get_location())
        v.add(hlsr.get_location())

    return len(v)


if __name__ == '__main__':
    file = open("input.txt", "r")
    lignes = file.read()
    print(f"partie 1 : {partie1(lignes)}")
    print(f"partie 2 : {partie2(lignes)}")