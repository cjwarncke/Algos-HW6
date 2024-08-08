def Prims(G):
    result = []
    visited = [0]

    while len(visited) < len(G):
        min_weight = 1e20
        for a in visited:
            for b in range(len(G)):
                if b not in visited:
                    weight = G[a][b]
                    if weight < min_weight and weight > 0:
                        min_weight = weight
                        new_node = b
                        edge = (a,b,weight)
        visited.append(new_node)
        result.append(edge)
    return result
