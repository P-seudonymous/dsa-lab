from graphviz import Digraph
import subprocess

dot = Digraph(comment="Flowchart: Recursive Prime Check")

# Main flow
dot.node("A", "Start", shape="oval")
dot.node("B", "Input n", shape="parallelogram")
dot.node("C", "Call isPrime(n, 2)", shape="rectangle")
dot.node("D", 'Display "Prime" or "Not Prime"', shape="parallelogram")
dot.node("E", "End", shape="oval")

# Recursive function
dot.node("F", "isPrime(n, i)", shape="rectangle")
dot.node("G", "n <= 2 ?", shape="diamond")
dot.node("H", "Return (n == 2)", shape="rectangle")
dot.node("I", "n % i == 0 ?", shape="diamond")
dot.node("J", "Return false", shape="rectangle")
dot.node("K", "i * i > n ?", shape="diamond")
dot.node("L", "Return true", shape="rectangle")
dot.node("M", "Return isPrime(n, i+1)", shape="rectangle")

# Edges main
dot.edge("A", "B")
dot.edge("B", "C")
dot.edge("C", "D")
dot.edge("D", "E")

# Edges recursive
dot.edge("F", "G")
dot.edge("G", "H", label="Yes")
dot.edge("G", "I", label="No")
dot.edge("I", "J", label="Yes")
dot.edge("I", "K", label="No")
dot.edge("K", "L", label="Yes")
dot.edge("K", "M", label="No")

# Save and render
output_path = "prime_recursive_flowchart"
dot.render(output_path, format="png", cleanup=True)

# Open image (Linux only)
subprocess.run(["xdg-open", f"{output_path}.png"])
