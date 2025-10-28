#include <bits/stdc++.h>
using namespace std;

class Graph {
    int V;
    bool directed;
    vector<vector<int>> adj;
public:
    Graph(int V, bool directed = false) : V(V), directed(directed), adj(V) {}

    void addEdge(int u, int v) {
        adj[u].push_back(v);
        if (!directed) adj[v].push_back(u);
    }

    void printGraph() {
        for (int i = 0; i < V; i++) {
            cout << i << ": ";
            for (int v : adj[i]) cout << v << " ";
            cout << "\n";
        }
    }
};

int main() {
    Graph g(5, false); // false → undirected, true → directed
    g.addEdge(0, 1);
    g.addEdge(0, 4);
    /*g.addEdge(1, 2);
    g.addEdge(1, 3);
    g.addEdge(1, 4);
    g.addEdge(2, 3);*/
    g.printGraph();
}

