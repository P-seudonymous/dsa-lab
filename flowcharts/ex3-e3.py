from graphviz import Digraph
import subprocess

# Create Digraph
dot = Digraph(comment="Flowchart for Virtual Function Example")

# Nodes
dot.node("A", "Start", shape="oval")
dot.node("B", "Declare base* bptr", shape="rectangle")
dot.node("C", "Declare derived d", shape="rectangle")
dot.node("D", "bptr = &d", shape="rectangle")
dot.node(
    "E", "bptr->print()\n(dynamic dispatch → derived::print)", shape="parallelogram"
)
dot.node("F", "bptr->show()\n(static binding → base::show)", shape="parallelogram")
dot.node("G", "End", shape="oval")

# Edges
dot.edge("A", "B")
dot.edge("B", "C")
dot.edge("C", "D")
dot.edge("D", "E")
dot.edge("E", "F")
dot.edge("F", "G")

# Save and render
output_path = "virtual_flowchart"
dot.render(output_path, format="png", cleanup=True)

# Open with xdg-open (Linux)
subprocess.run(["xdg-open", f"{output_path}.png"])
