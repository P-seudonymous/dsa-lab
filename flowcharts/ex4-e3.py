from graphviz import Digraph
import subprocess

dot = Digraph(comment="Flowchart: Template Bubble Sort (Single Combined)")

# Nodes
dot.node("A", "Start", shape="oval")
dot.node(
    "B",
    "Initialize arrays:\na[6]={17,16,15,14,9,-1}\nb[4]={z,b,x,a}",
    shape="rectangle",
)

# Sorting integers
dot.node("C", "Call bubble(a,6)", shape="rectangle")
dot.node("D", "Outer loop i=0..n-2", shape="diamond")
dot.node("E", "Inner loop j=0..n-2", shape="diamond")
dot.node("F", "If a[j] > a[j+1]?", shape="diamond")
dot.node("G", "Swap a[j], a[j+1]", shape="rectangle")
dot.node("H", "Sorted integers ready", shape="rectangle")
dot.node("I", "Display sorted integers", shape="parallelogram")

# Sorting characters
dot.node("J", "Call bubble(b,4)", shape="rectangle")
dot.node("K", "Outer loop i=0..n-2", shape="diamond")
dot.node("L", "Inner loop j=0..n-2", shape="diamond")
dot.node("M", "If b[j] > b[j+1]?", shape="diamond")
dot.node("N", "Swap b[j], b[j+1]", shape="rectangle")
dot.node("O", "Sorted chars ready", shape="rectangle")
dot.node("P", "Display sorted chars", shape="parallelogram")

dot.node("Q", "End", shape="oval")

# Edges (main + function combined flow)
dot.edge("A", "B")
dot.edge("B", "C")
dot.edge("C", "D")
dot.edge("D", "E")
dot.edge("E", "F")
dot.edge("F", "G", label="Yes")
dot.edge("F", "E", label="No", constraint="false")
dot.edge("G", "E")
dot.edge("E", "D")
dot.edge("D", "H")
dot.edge("H", "I")

dot.edge("I", "J")
dot.edge("J", "K")
dot.edge("K", "L")
dot.edge("L", "M")
dot.edge("M", "N", label="Yes")
dot.edge("M", "L", label="No", constraint="false")
dot.edge("N", "L")
dot.edge("L", "K")
dot.edge("K", "O")
dot.edge("O", "P")
dot.edge("P", "Q")

# Save and render
output_path = "bubble_sort_one_flowchart"
dot.render(output_path, format="png", cleanup=True)

# Open (Linux only)
subprocess.run(["xdg-open", f"{output_path}.png"])
