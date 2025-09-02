from graphviz import Digraph
import subprocess

dot = Digraph(
    comment="Flowchart for Hierarchical Inheritance Addition & Multiplication"
)

# Nodes
dot.node("A", "Start", shape="oval")
dot.node("B", "Create Addition & Multiplication objects", shape="rectangle")
dot.node("C", "input(): Read a & b", shape="parallelogram")
dot.node("D", "sum(): c = a + b", shape="rectangle")
dot.node("E", "displaySum(): Output c", shape="parallelogram")
dot.node("F", "product(): d = a * b", shape="rectangle")
dot.node("G", "displayProduct(): Output d", shape="parallelogram")
dot.node("H", "End", shape="oval")

# Edges
dot.edge("A", "B")
dot.edge("B", "C")
dot.edge("C", "D")
dot.edge("D", "E")
dot.edge("E", "F")
dot.edge("F", "G")
dot.edge("G", "H")

# Save and render
output_path = "hierarchical_inheritance_flowchart"
dot.render(output_path, format="png", cleanup=True)

# Open on Linux
subprocess.run(["xdg-open", f"{output_path}.png"])
