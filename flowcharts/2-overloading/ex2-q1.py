from graphviz import Digraph
import subprocess

dot = Digraph(comment="Flowchart: Complex Number Operations using Friend Functions")

# Nodes
dot.node("A", "Start", shape="oval")
dot.node("B", "Create Complex objects c1(4,5) and c2(2,3)", shape="rectangle")
dot.node("C", "add(c1, c2): sum", shape="rectangle")
dot.node("D", "subtract(c1, c2): diff", shape="rectangle")
dot.node("E", "multiply(c1, c2): prod", shape="rectangle")
dot.node("F", "divide(c1, c2): quot", shape="rectangle")
dot.node("G", "Display sum, diff, prod, quot", shape="parallelogram")
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
output_path = "complex_friend_flowchart"
dot.render(output_path, format="png", cleanup=True)

# Open (Linux)
subprocess.run(["xdg-open", f"{output_path}.png"])
