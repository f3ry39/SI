class Pokoj:
    def __init__(self, nazwa, jestBrudny=1):
        self.nazwa = nazwa
        self.jestBrudny = jestBrudny


class Robot:
    def __init__(self):
        self.pokoj_lewy = Pokoj("A")
        self.pokoj_prawy = Pokoj("B")
        self.pokoj_obecny = self.pokoj_lewy

    def idz_lewo(self):
        if self.pokoj_obecny == self.pokoj_prawy:
            self.pokoj_obecny = self.pokoj_lewy

    def idz_prawo(self):
        if self.pokoj_obecny == self.pokoj_lewy:
            self.pokoj_obecny = self.pokoj_prawy

    def czysc(self):
        self.pokoj_obecny.jestBrudny = 0

    def auto(self):

        licznik = 0

        while self.pokoj_lewy.jestBrudny == 1 or self.pokoj_prawy.jestBrudny == 1:
            if self.pokoj_obecny.jestBrudny:
                self.czysc()
            elif self.pokoj_obecny == self.pokoj_lewy:
                self.idz_prawo()
            elif self.pokoj_obecny == self.pokoj_prawy:
                self.idz_lewo()

            licznik = licznik + 1
            print("Step: {0}".format(licznik))
            print(self)

        return licznik

    def __str__(self):
        return "Obecny pokoj: {0}, {1} brud: {2}, {3} brud: {4}".format(self.pokoj_obecny.nazwa,
                                                                        self.pokoj_lewy.nazwa,
                                                                        self.pokoj_lewy.jestBrudny,
                                                                        self.pokoj_prawy.nazwa,
                                                                        self.pokoj_prawy.jestBrudny)


class Stan:
    def __init__(self, pokoj_obecny, brud_po_lewej, brud_po_prawej):
        self.pokoj_obecny = pokoj_obecny
        self.brud_po_lewej = brud_po_lewej
        self.brud_po_prawej = brud_po_prawej

    def __str__(self):
        return "Robot w pokoju: {0}, brud w A: {1}, brud w B: {2}".format(self.pokoj_obecny, self.brud_po_lewej,
                                                                          self.brud_po_prawej)


class Graph:
    def __init__(self):
        self.A = Stan("A", 1, 1)
        self.B = Stan("B", 1, 1)
        self.C = Stan("A", 0, 1)
        self.D = Stan("B", 1, 0)
        self.E = Stan("B", 0, 1)
        self.F = Stan("A", 1, 0)
        self.G = Stan("B", 0, 0)
        self.H = Stan("A", 0, 0)

        self.graph = {
            self.A: [self.B, self.C],
            self.B: [self.A, self.D],
            self.C: [self.A, self.E],
            self.D: [self.B, self.F],
            self.E: [self.C, self.G],
            self.F: [self.D, self.H],
            self.G: [self.H],
            self.H: [self.G]
        }

        self.visited = []
        self.queue = []

    def bfs(self):
        self.visited.append(self.A)
        self.queue.append(self.A)

        while self.queue:
            s = self.queue.pop(0)
            print(s)

            for neighbour in self.graph[s]:
                if neighbour not in self.visited:
                    self.visited.append(neighbour)
                    self.queue.append(neighbour)


if __name__ == '__main__':
    g = Graph()
    g.bfs()
