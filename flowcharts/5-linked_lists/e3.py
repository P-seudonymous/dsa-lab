from graphviz import Digraph
import subprocess

dot = Digraph(comment="Flowchart: Linked List Insert, Delete at Tail & Print")

# Nodes
dot.node("A", "Start", shape="oval")
dot.node("B", "Initialize head = NULL", shape="rectangle")

# Insert operations
dot.node("C1", "insertAtFirst(head, 5)", shape="rectangle")
dot.node("C2", "insertAtFirst(head, 4)", shape="rectangle")
dot.node("C3", "insertAtFirst(head, 3)", shape="rectangle")
dot.node("C4", "insertAtFirst(head, 2)", shape="rectangle")
dot.node("C5", "insertAtFirst(head, 1)", shape="rectangle")

# Print before delete
dot.node("D", "printNode(head)\nOutput: 1->2->3->4->5", shape="parallelogram")

# Delete at tail
dot.node("E", "deleteAtTail(head)\n(Delete last node)", shape="rectangle")

# Print after delete
dot.node("F", "printNode(head)\nOutput: 1->2->3->4", shape="parallelogram")

dot.node("G", "End", shape="oval")

# Edges
dot.edge("A", "B")
dot.edge("B", "C1")
dot.edge("C1", "C2")
dot.edge("C2", "C3")
dot.edge("C3", "C4")
dot.edge("C4", "C5")
dot.edge("C5", "D")
dot.edge("D", "E")
dot.edge("E", "F")
dot.edge("F", "G")

# Save and render
output_path = "linkedlist_insert_delete_flowchart"
dot.render(output_path, format="png", cleanup=True)

# Open automatically on Linux
subprocess.run(["xdg-open", f"{output_path}.png"])
