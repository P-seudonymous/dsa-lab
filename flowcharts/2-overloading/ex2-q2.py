from graphviz import Digraph
import subprocess

dot = Digraph(comment="Flowchart: Unary Operator Overloading (++ and --)")

# Nodes
dot.node("A", "Start", shape="oval")
dot.node("B", "Create Counter object c(5)", shape="rectangle")
dot.node("C", "Display initial value", shape="parallelogram")
dot.node("D", "++c (calls operator++())", shape="rectangle")
dot.node("E", "Display after increment", shape="parallelogram")
dot.node("F", "--c (calls operator--())", shape="rectangle")
dot.node("G", "Display after decrement", shape="parallelogram")
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
output_path = "unary_operator_overloading_flowchart"
dot.render(output_path, format="png", cleanup=True)

# Open (Linux)
subprocess.run(["xdg-open", f"{output_path}.png"])
