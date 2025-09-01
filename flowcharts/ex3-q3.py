from graphviz import Digraph
import subprocess

dot = Digraph(comment="Flowchart: Invoke Derived Method via Base Pointer")

# Nodes
dot.node("A", "Start", shape="oval")
dot.node("B", "Declare base pointer (Formula *ptr)", shape="rectangle")
dot.node("C", "Create MathExpression object", shape="rectangle")
dot.node("D", "ptr = &object", shape="rectangle")
dot.node("E", "ptr->compute() (dynamic dispatch)", shape="rectangle")
dot.node("F", "Input a, b, c", shape="parallelogram")
dot.node("G", "Calculate result = (a + b) * c", shape="rectangle")
dot.node("H", "Display result", shape="parallelogram")
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

# Save and render
output_path = "derived_via_base_pointer"
dot.render(output_path, format="png", cleanup=True)

# Open (Linux)
subprocess.run(["xdg-open", f"{output_path}.png"])
