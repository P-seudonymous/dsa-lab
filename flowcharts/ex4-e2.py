from graphviz import Digraph
import subprocess

dot = Digraph(comment="Flowchart: Template Function maxmin()")

# Nodes
dot.node("A", "Start", shape="oval")
dot.node("B", "Display menu\n1.Int 2.Char 3.Float 4.Double", shape="parallelogram")
dot.node("C", "Input choice (ch)", shape="parallelogram")
dot.node("D", "Input n (size of array)", shape="parallelogram")
dot.node("E", "Switch(ch)", shape="diamond")

# Cases
dot.node("F1", "Read integer array", shape="parallelogram")
dot.node("F2", "Read char array", shape="parallelogram")
dot.node("F3", "Read float array", shape="parallelogram")
dot.node("F4", "Read double array", shape="parallelogram")
dot.node("FD", "Invalid choice", shape="parallelogram")

# Template function
dot.node("G", "Call maxmin(array, n)", shape="rectangle")
dot.node("H", "Sort array", shape="rectangle")
dot.node("I", "min = a[0]\nmax = a[n-1]", shape="rectangle")
dot.node("J", "Display min and max", shape="parallelogram")
dot.node("K", "End", shape="oval")

# Edges
dot.edge("A", "B")
dot.edge("B", "C")
dot.edge("C", "D")
dot.edge("D", "E")

dot.edge("E", "F1", label="1")
dot.edge("E", "F2", label="2")
dot.edge("E", "F3", label="3")
dot.edge("E", "F4", label="4")
dot.edge("E", "FD", label="default")

dot.edge("F1", "G")
dot.edge("F2", "G")
dot.edge("F3", "G")
dot.edge("F4", "G")
dot.edge("FD", "K")

dot.edge("G", "H")
dot.edge("H", "I")
dot.edge("I", "J")
dot.edge("J", "K")

# Save and render
output_path = "template_maxmin_flowchart"
dot.render(output_path, format="png", cleanup=True)

# Open (Linux)
subprocess.run(["xdg-open", f"{output_path}.png"])
