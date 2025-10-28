#include <bits/stdc++.h>
using namespace std;

int findLevel(int V, vector<vector<int>>& adj, int X) {
    vector<int> level(V, -1);
    queue<int> q;
    q.push(0);
    level[0] = 0;

    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u]) {
            if (level[v] == -1) {
                level[v] = level[u] + 1;
                q.push(v);
            }
        }
    }
    return (X >= V) ? -1 : level[X];
}

int main() {
    int V = 6;
    vector<vector<int>> adj(V);
    vector<pair<int,int>> edges = {{0,1},{0,2},{1,3}};
    for (auto [u,v] : edges) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int X = 5;
    cout << "Level of node " << X << " is " << findLevel(V, adj, X) << endl;
}

