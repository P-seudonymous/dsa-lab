from graphviz import Digraph
import subprocess

dot = Digraph(comment="Flowchart: Hybrid Inheritance R = (a+b)*(c-d)")

# Nodes
dot.node("A", "Start", shape="oval")
dot.node("B", "Create Result object", shape="rectangle")
dot.node("C", "readValues(): Input a, b, c, d", shape="parallelogram")
dot.node("D", "computeSum(): sum_ab = a + b", shape="rectangle")
dot.node("E", "computeDiff(): diff_cd = c - d", shape="rectangle")
dot.node("F", "computeResult(): R = sum_ab * diff_cd", shape="rectangle")
dot.node("G", "display(): Output R", shape="parallelogram")
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
output_path = "hybrid_inheritance_flowchart"
dot.render(output_path, format="png", cleanup=True)

# Open (Linux)
subprocess.run(["xdg-open", f"{output_path}.png"])
