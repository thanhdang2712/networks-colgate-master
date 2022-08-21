import wikipedia as wk
import pprint

# Constants
DEPTH = 2

def dfs(node, graph, visited, cur_depth):
    # print(node)
    if node not in visited:
        visited.add(node)

        if cur_depth < DEPTH:
            try:
                page = wk.page(node)
                neighbors = page.links
                graph[node] = neighbors

                for n in neighbors:
                    dfs(n, graph, visited, cur_depth + 1)
            except:
                pass

def main():
    start = wk.page("Cox-Zucker machine")
    graph = {start.title : start.links}
    
    visited = set()
    dfs(start.title, graph, visited, 0)
    pprint.pprint(graph)


if __name__ == "__main__":
    main()