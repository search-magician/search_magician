import scrapper
from graph import Graph
import htmlScrapper

def BFS(g, start, levels):
    s = set()
    queue = []
    queue.append([start,0])
    s.add(start)
    while(len(queue) > 0):
        node = queue.pop(0)
        level = node[1]
        print("========== Video ID: ",node[0], ", level = ", node[1],"======")
        if level > levels:
            return s
        node = node[0]
        children = htmlScrapper.main(node)
        for child in children:
            if child not in s:
                s.add(child)
                print(child)
                queue.append([child,level + 1])
                g.addEdge(node, child)
    return s

if __name__ == '__main__':
    print("How many levels of scrapping you want to get?")
    levels = int(input())
    start = 'sd7dSHU4BKs' ###The Start Video_Id entry
    g = Graph()
    s = BFS(g, start, levels)
    print("Number of results: ", len(s))