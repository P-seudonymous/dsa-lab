from graphviz import Digraph
import os

# Create a flowchart
flowchart = Digraph(format="png")
flowchart.attr(rankdir="TB", size="10")

# Nodes
flowchart.node("Start", "Start", shape="oval")
flowchart.node("Obj", "Create object of class B", shape="rectangle")
flowchart.node("Get", "Call get() method\n(Input a and b)", shape="parallelogram")
flowchart.node("Add", "Call add() method", shape="rectangle")
flowchart.node("Calc", "c = a + b", shape="rectangle")
flowchart.node("Print", "Display result: a + b = c", shape="parallelogram")
flowchart.node("End", "End", shape="oval")

# Edges
flowchart.edges(
    [
        ("Start", "Obj"),
        ("Obj", "Get"),
        ("Get", "Add"),
        ("Add", "Calc"),
        ("Calc", "Print"),
        ("Print", "End"),
    ]
)

# Save and render the flowchart
output_path = flowchart.render("flowchart", cleanup=True)

# Automatically open the PNG using xdg-open (Linux)
os.system(f"xdg-open {output_path}")
