from graphviz import Digraph
import subprocess

dot = Digraph(comment="Flowchart for Multiple Inheritance Addition Program")

# Nodes
dot.node("A", "Start", shape="oval")
dot.node("B", "Create Sum object", shape="rectangle")
dot.node("C", "inputA(): Read a", shape="parallelogram")
dot.node("D", "inputB(): Read b", shape="parallelogram")
dot.node("E", "calculate(): c = a + b", shape="rectangle")
dot.node("F", "display(): Output c", shape="parallelogram")
dot.node("G", "End", shape="oval")

# Edges
dot.edge("A", "B")
dot.edge("B", "C")
dot.edge("C", "D")
dot.edge("D", "E")
dot.edge("E", "F")
dot.edge("F", "G")

# Save and render
output_path = "multiple_inheritance_addition"
dot.render(output_path, format="png", cleanup=True)

# Open (Linux only)
subprocess.run(["xdg-open", f"{output_path}.png"])
