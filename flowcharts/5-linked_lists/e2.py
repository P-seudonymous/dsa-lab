from graphviz import Digraph
import subprocess

dot = Digraph(comment="Flowchart: Linked List Push & Search")

# Nodes
dot.node("A", "Start", shape="oval")
dot.node("B", "Initialize head = NULL, x = 21", shape="rectangle")
dot.node("C1", "push(&head, 10)", shape="rectangle")
dot.node("C2", "push(&head, 30)", shape="rectangle")
dot.node("C3", "push(&head, 11)", shape="rectangle")
dot.node("C4", "push(&head, 21)", shape="rectangle")
dot.node("C5", "push(&head, 14)", shape="rectangle")
dot.node("D", "search(head, x)", shape="diamond")
dot.node("E1", 'Print "Yes"', shape="parallelogram")
dot.node("E2", 'Print "No"', shape="parallelogram")
dot.node("F", "End", shape="oval")

# Edges
dot.edge("A", "B")
dot.edge("B", "C1")
dot.edge("C1", "C2")
dot.edge("C2", "C3")
dot.edge("C3", "C4")
dot.edge("C4", "C5")
dot.edge("C5", "D")
dot.edge("D", "E1", label="Found")
dot.edge("D", "E2", label="Not Found")
dot.edge("E1", "F")
dot.edge("E2", "F")

# Save & render
output_path = "linkedlist_search_flowchart"
dot.render(output_path, format="png", cleanup=True)

# Open automatically on Linux
subprocess.run(["xdg-open", f"{output_path}.png"])
