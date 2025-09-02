from graphviz import Digraph
import subprocess

dot = Digraph(comment="Flowchart: Increasing Sequences of Length k")

# Main program
dot.node("A", "Start", shape="oval")
dot.node("B", "Input n, k", shape="parallelogram")
dot.node("C", "Call generate([], 1, n, k)", shape="rectangle")
dot.node("D", "End", shape="oval")

# Recursive function block
dot.node("E", "generate(seq, start, n, k)", shape="rectangle")
dot.node("F", "Is length(seq) == k?", shape="diamond")
dot.node("G", "Print sequence", shape="parallelogram")
dot.node("H", "For i = start to n", shape="diamond")
dot.node("I", "Append i to seq", shape="rectangle")
dot.node("J", "Recursive call:\ngenerate(seq, i+1, n, k)", shape="rectangle")
dot.node("K", "Backtrack: remove i", shape="rectangle")

# Edges main
dot.edge("A", "B")
dot.edge("B", "C")
dot.edge("C", "D")

# Edges recursive
dot.edge("E", "F")
dot.edge("F", "G", label="Yes")
dot.edge("F", "H", label="No")
dot.edge("H", "I", label="For each i")
dot.edge("I", "J")
dot.edge("J", "K")
dot.edge("K", "H")

# Save and render
output_path = "increasing_sequences_flowchart"
dot.render(output_path, format="png", cleanup=True)

# Open (Linux only)
subprocess.run(["xdg-open", f"{output_path}.png"])
