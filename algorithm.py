def bellman_ford(nodes, edges, source):
    dist = {node: float('inf') for node in nodes}
    dist[source] = 0
    steps = []

    for _ in range(len(nodes) - 1):
        updated = False
        for edge in edges:
            u, v, w = edge["from_node"], edge["to_node"], edge["weight"]
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        steps.append(dist.copy())
        if not updated:
            break

    for edge in edges:
        u, v, w = edge["from_node"], edge["to_node"], edge["weight"]
        if dist[u] + w < dist[v]:
            return {"error": "Negative weight cycle detected"}

    return {"steps": steps, "final": dist}
