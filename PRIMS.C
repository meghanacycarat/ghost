#include <stdio.h>
#include <stdbool.h>
#include <limits.h>

#define MAX_VERTICES 100

int graph[MAX_VERTICES][MAX_VERTICES];
int numVertices;

int findMinimumKey(int key[], bool mstSet[], int n) {
    int minKey = INT_MAX;
    int minIndex = -1;
    for (int v = 0; v < n; v++) {
        if (!mstSet[v] && key[v] < minKey) {
            minKey = key[v];
            minIndex = v;
        }
    }
    return minIndex;
}

void printMST(int parent[], int n) {
    printf("Edge \tWeight\n");
    for (int i = 1; i < n; i++) {
        printf("%d - %d \t%d\n", parent[i], i, graph[i][parent[i]]);
    }
}

void primMST(int n) {
    int parent[n];
    int key[n];
    bool mstSet[n];

    for (int i = 0; i < n; i++) {
        key[i] = INT_MAX;
        mstSet[i] = false;
    }

    key[0] = 0;
    parent[0] = -1;

    for (int count = 0; count < n - 1; count++) {
        int u = findMinimumKey(key, mstSet, n);
        mstSet[u] = true;

        for (int v = 0; v < n; v++) {
            if (graph[u][v] && !mstSet[v] && graph[u][v] < key[v]) {
                parent[v] = u;
                key[v] = graph[u][v];
            }
        }
    }

    printMST(parent, n);
}

int main() {
    printf("Enter the number of vertices: ");
    scanf("%d", &numVertices);
    printf("Enter the adjacency matrix:\n");
    for (int i = 0; i < numVertices; i++) {
        for (int j = 0; j < numVertices; j++) {
            scanf("%d", &graph[i][j]);
        }
    }
    printf("Minimum Spanning Tree:\n");
    primMST(numVertices);
    return 0;
}
