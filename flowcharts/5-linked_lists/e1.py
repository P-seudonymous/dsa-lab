from graphviz import Digraph
import subprocess

dot = Digraph(comment="Flowchart: Linked List Insertion and Printing")

# Nodes
dot.node("A", "Start", shape="oval")
dot.node("B", "Initialize head = NULL", shape="rectangle")
dot.node("C", "push(&head, 7)", shape="rectangle")
dot.node("D", "push(&head, 1)", shape="rectangle")
dot.node("E", "push(&head, 8)", shape="rectangle")
dot.node("F", "push(&head, 4)", shape="rectangle")
dot.node("G", 'Print "Created list is:"', shape="parallelogram")
dot.node("H", "printlist(head)\nTraverse until NULL\nPrint data", shape="rectangle")
dot.node("I", "End", shape="oval")

# Edges
dot.edge("A", "B")
dot.edge("B", "C")
dot.edge("C", "D")
dot.edge("D", "E")
dot.edge("E", "F")
dot.edge("F", "G")
dot.edge("G", "H")
dot.edge("H", "I")

# Save & Render
output_path = "linkedlist_flowchart"
dot.render(output_path, format="png", cleanup=True)

# Open (Linux only)
subprocess.run(["xdg-open", f"{output_path}.png"])
