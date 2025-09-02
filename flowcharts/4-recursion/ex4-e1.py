from graphviz import Digraph
import subprocess

dot = Digraph(comment="Flowchart: Factorial with and without Recursion")

# Nodes
dot.node("A", "Start", shape="oval")
dot.node("B", "Input num", shape="parallelogram")
dot.node("C", "Call fact(num)\n(Iterative factorial)", shape="rectangle")
dot.node("D", "Compute factorial using loop", shape="rectangle")
dot.node("E", "Return fac", shape="rectangle")
dot.node("F", "Display non-recursive factorial", shape="parallelogram")
dot.node("G", "Call fact_recur(num)\n(Recursive factorial)", shape="rectangle")
dot.node(
    "H",
    "If num == 1?\nYes → return 1\nNo → return num * fact_recur(num-1)",
    shape="diamond",
)
dot.node("I", "Return result", shape="rectangle")
dot.node("J", "Display recursive factorial", shape="parallelogram")
dot.node("K", "End", shape="oval")

# Edges
dot.edge("A", "B")
dot.edge("B", "C")
dot.edge("C", "D")
dot.edge("D", "E")
dot.edge("E", "F")
dot.edge("F", "G")
dot.edge("G", "H")
dot.edge("H", "I")
dot.edge("I", "J")
dot.edge("J", "K")

# Save and render
output_path = "factorial_flowchart"
dot.render(output_path, format="png", cleanup=True)

# Open (Linux)
subprocess.run(["xdg-open", f"{output_path}.png"])
