from graph import Graph


def first(original, firstpoint):  # алгоритм Прима
    graph = Graph()
    graph.connections(firstpoint)
    while len(original) != len(graph):
        min_a = None
        min_b = None
        min_w = None
        for a in graph:
            con_a = original.connections(a)
            for b in filter(lambda l: l not in graph, con_a):
                if min_w is None or min_w > con_a[b]:
                    min_a = a
                    min_b = b
                    min_w = con_a[b]

        if min_a is not None:
            graph.set(min_a, min_b, min_w)

    return graph


def second(original):  # алгоритм с отбрасыванием максимальных соединений
    edges = []
    graph = Graph(original)
    for a in graph:
        con_a = graph.connections(a)
        for b in con_a:
            edges.append((a, b, con_a[b]))

    for edge in sorted(edges, key=lambda l: -l[2]):
        graph.remove(edge[0], edge[1])

    return graph


graph = Graph().console()
print("=" * 96)

for point in graph:
    result = first(graph, point)
    print("1 алгоритм, начало с " + point + ", результат: " + str(result.sum()) + ", данные: " + str(result))

result = second(graph)
print("2 алгоритм, результат: " + str(result.sum()) + ", данные: " + str(result))
