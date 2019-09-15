class Graph:
    def __init__(self, source=None):
        self._map = {}  # {'A':{'B':32, ...}, ...}
        if type(source) == Graph:
            for a in source:
                con_a = source.connections(a)
                for b in con_a:
                    self.set(a, b, con_a[b])

    def __str__(self):
        return str(self._map)

    def __iter__(self):
        return iter(self._map)

    def __copy__(self):
        return Graph(self)

    def __len__(self):
        return len(self._map)

    def __contains__(self, item):
        return item in self._map

    def console(self):
        print("Для возвращения на первый шаг или завершения ввода на первом шаге нажмите ENTER, оставив строку пустой.")
        while True:
            a = input("1. Введите название первой точки: ")
            if not a:
                if self.check(True):
                    break
                else:
                    continue

            b = input("2. Введите название второй точки: ")
            if not b:
                continue

            terminate = False
            while True:
                w = input("3. Введите расстояние между " + a + " и " + b + ": ")
                if not w:
                    terminate = True
                    break

                try:
                    w = float(w)
                    break
                except ValueError:
                    print("Неправильное число '" + w + "'")

            if terminate:
                continue

            self.set(a, b, w, True)

        return self

    def set(self, a, b, weight, printout=False):
        self.connections(a, printout)[b] = weight
        self.connections(b, printout)[a] = weight

    def remove(self, a, b, printout=False):
        graph = Graph(self)
        try:
            del graph.connections(a, printout)[b]
            del graph.connections(b, printout)[a]
            if not graph.check(printout):
                return False
        except KeyError:
            return False

        del self.connections(a, printout)[b]
        del self.connections(b, printout)[a]
        return True

    def connections(self, a, printout=False):
        if a not in self._map:
            self._map[a] = {}
            if printout:
                print("Создана точка", a)
        return self._map[a]

    def dfs(self, visited, a=None):
        if a is None:
            for point in self:
                a = point
                break
            else:
                return True

        if a in visited:
            return True

        visited.add(a)
        for b in filter(lambda l: l not in visited, self.connections(a)):
            self.dfs(visited, b)

    def check(self, printout=False):
        visited = set()
        self.dfs(visited)
        result = len(visited) == len(self._map)
        if printout and not result:
            print("Граф не соединён!")
        return result

    def sum(self):
        result = 0
        for con_a in self._map.values():
            for w in con_a.values():
                result += w

        return result / 2
