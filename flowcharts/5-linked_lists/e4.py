from graphviz import Digraph
import subprocess

dot = Digraph(comment="Flowchart: Doubly Linked List (push_front & PrintList)")

# Nodes
dot.node("A", "Start", shape="oval")
dot.node("B", "Initialize head = NULL", shape="rectangle")
dot.node("C1", "push_front(10)\n(head -> 10)", shape="rectangle")
dot.node("C2", "push_front(20)\n(head -> 20 <-> 10)", shape="rectangle")
dot.node("C3", "push_front(30)\n(head -> 30 <-> 20 <-> 10)", shape="rectangle")
dot.node("D", "PrintList()\nOutput: 30 20 10", shape="parallelogram")
dot.node("E", "End", shape="oval")

# Edges
dot.edge("A", "B")
dot.edge("B", "C1")
dot.edge("C1", "C2")
dot.edge("C2", "C3")
dot.edge("C3", "D")
dot.edge("D", "E")

# Save & render
output_path = "doubly_linkedlist_flowchart"
dot.render(output_path, format="png", cleanup=True)

# Auto-open (Linux)
subprocess.run(["xdg-open", f"{output_path}.png"])
