from graphviz import Digraph
import subprocess

# Create Digraph object
dot = Digraph(comment="Flowchart for C++ Program")

# Flowchart nodes
dot.node("A", "Start", shape="oval")
dot.node("B", "Create derive2 object a", shape="rectangle")

# Method calls with I/O
dot.node("C", "getdata():\nPrompt & Read x", shape="parallelogram")
dot.node("D", "readdata():\nPrompt & Read y", shape="parallelogram")
dot.node("E", "indata():\nPrompt & Read z", shape="parallelogram")
dot.node("F", "product():\nDisplay x*y*z", shape="parallelogram")

dot.node("G", "End", shape="oval")

# Connect the nodes in sequence
dot.edge("A", "B")
dot.edge("B", "C")
dot.edge("C", "D")
dot.edge("D", "E")
dot.edge("E", "F")
dot.edge("F", "G")

# Save and render
output_path = "flowchart"
dot.render(output_path, format="png", cleanup=True)

# Open image (works on Linux)
subprocess.run(["xdg-open", f"{output_path}.png"])
