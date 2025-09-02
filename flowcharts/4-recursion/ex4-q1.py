from graphviz import Digraph
import subprocess

dot = Digraph(comment="Flowchart: Sine Approximation using Series")

# Nodes
dot.node("A", "Start", shape="oval")
dot.node("B", "Input x (degrees), n", shape="parallelogram")
dot.node("C", "Convert x to radians\nx = x * (π/180)", shape="rectangle")
dot.node("D", "Initialize sum=0, sign=+1", shape="rectangle")
dot.node("E", "i = 1", shape="rectangle")
dot.node("F", "i <= n ?", shape="diamond")
dot.node("G", "Compute term = x^(2i-1)/(2i-1)!", shape="rectangle")
dot.node("H", "sum = sum + sign * term", shape="rectangle")
dot.node("I", "sign = -sign", shape="rectangle")
dot.node("J", "i = i + 1", shape="rectangle")
dot.node("K", "Output sum (Approx sin(x))", shape="parallelogram")
dot.node("L", "End", shape="oval")

# Edges
dot.edge("A", "B")
dot.edge("B", "C")
dot.edge("C", "D")
dot.edge("D", "E")
dot.edge("E", "F")
dot.edge("F", "G", label="Yes")
dot.edge("G", "H")
dot.edge("H", "I")
dot.edge("I", "J")
dot.edge("J", "F")
dot.edge("F", "K", label="No")
dot.edge("K", "L")

# Save and render
output_path = "sine_series_flowchart"
dot.render(output_path, format="png", cleanup=True)

# Open (Linux only)
subprocess.run(["xdg-open", f"{output_path}.png"])
