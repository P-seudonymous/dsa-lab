from graphviz import Digraph


def add_common_nodes(g, title):
    g.attr(label=title, labelloc="t", fontsize="18", fontname="Arial", nodesep="0.5")
    g.attr(
        "node",
        fontname="Arial",
        shape="ellipse",
        style="filled",
        fillcolor="lightyellow",
    )


# 1️⃣ Graph Implementation (Directed / Undirected)
g1 = Digraph("Graph_Implementation", format="png")
add_common_nodes(g1, "Graph Implementation (Directed / Undirected)")

g1.node("A", "Start", shape="ellipse", fillcolor="lightgreen")
g1.node("B", "Initialize Graph(V, directed)", shape="rectangle")
g1.node("C", "Add Edge(u, v)", shape="rectangle")
g1.node("D", "Is graph directed?", shape="diamond", fillcolor="lightblue")
g1.node("E", "Add Edge(v, u)", shape="rectangle")
g1.node("F", "Print adjacency list", shape="parallelogram", fillcolor="lightpink")
g1.node("G", "End", shape="ellipse", fillcolor="lightgreen")

g1.edge("A", "B")
g1.edge("B", "C")
g1.edge("C", "D")
g1.edge("D", "F", label="Yes")
g1.edge("D", "E", label="No")
g1.edge("E", "F")
g1.edge("F", "G")
g1.render("graph_implementation_flowchart", cleanup=True)


# 2️⃣ Weighted / Unweighted Graph
g2 = Digraph("Weighted_Graph", format="png")
add_common_nodes(g2, "Weighted / Unweighted Graph")

g2.node("A", "Start", shape="ellipse", fillcolor="lightgreen")
g2.node("B", "Initialize Graph(V, directed, weighted)", shape="rectangle")
g2.node("C", "Add Edge(u, v, w)", shape="rectangle")
g2.node("D", "Is graph weighted?", shape="diamond", fillcolor="lightblue")
g2.node("E", "Use weight w", shape="rectangle")
g2.node("F", "Use weight = 1", shape="rectangle")
g2.node("G", "Is graph directed?", shape="diamond", fillcolor="lightblue")
g2.node("H", "Add reverse edge(v, u)", shape="rectangle")
g2.node("I", "Print adjacency list", shape="parallelogram", fillcolor="lightpink")
g2.node("J", "End", shape="ellipse", fillcolor="lightgreen")

g2.edge("A", "B")
g2.edge("B", "C")
g2.edge("C", "D")
g2.edge("D", "E", label="Yes")
g2.edge("D", "F", label="No")
g2.edge("E", "G")
g2.edge("F", "G")
g2.edge("G", "I", label="Yes")
g2.edge("G", "H", label="No")
g2.edge("H", "I")
g2.edge("I", "J")
g2.render("weighted_graph_flowchart", cleanup=True)


# 3️⃣ BFS Level of Node (Level Order Traversal)
g3 = Digraph("BFS_Level", format="png")
add_common_nodes(g3, "Find Level of Node using BFS")

g3.node("A", "Start", shape="ellipse", fillcolor="lightgreen")
g3.node("B", "Initialize queue, level[] = -1", shape="rectangle")
g3.node("C", "Push node 0, level[0] = 0", shape="rectangle")
g3.node("D", "Queue not empty?", shape="diamond", fillcolor="lightblue")
g3.node("E", "u = q.front(); q.pop()", shape="rectangle")
g3.node("F", "For each v in adj[u]", shape="rectangle")
g3.node("G", "level[v] == -1 ?", shape="diamond", fillcolor="lightblue")
g3.node("H", "level[v] = level[u] + 1; q.push(v)", shape="rectangle")
g3.node("I", "End For", shape="rectangle")
g3.node("J", "Return level[X]", shape="parallelogram", fillcolor="lightpink")
g3.node("K", "End", shape="ellipse", fillcolor="lightgreen")

g3.edge("A", "B")
g3.edge("B", "C")
g3.edge("C", "D")
g3.edge("D", "E", label="Yes")
g3.edge("D", "J", label="No")
g3.edge("E", "F")
g3.edge("F", "G")
g3.edge("G", "H", label="Yes")
g3.edge("G", "I", label="No")
g3.edge("H", "I")
g3.edge("I", "D")
g3.edge("J", "K")
g3.render("bfs_level_flowchart", cleanup=True)

print(
    "✅ Flowcharts generated:\n- graph_implementation_flowchart.png\n- weighted_graph_flowchart.png\n- bfs_level_flowchart.png"
)
