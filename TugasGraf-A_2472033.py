class TraversalGraf():
    def __init__(self, size):
        self.N = size
        self.matriks = [None] * self.N
        for i in range(0, self.N, 1):
            self.matriks[i] = [None] * self.N
        self.abjad = [None] * self.N
        for i in range(0, self.N, 1):
            self.abjad[i] = chr(ord('A') + i)
        return
    
    def fillMatriks(self):
        for i in range(0, self.N, 1):
            print("=======================")
            print(f"Baris {i}")
            print("=======================")
            for j in range(0, self.N, 1):
                print(f"Kolom {j}: ", end="")
                self.matriks[i][j] = int(input())
        return
    
    def printMatriks(self):
        for i in range(0, self.N, 1):
            for j in range(0, self.N, 1):
                print(self.matriks[i][j], end=" ")
            print()
        return
    
    def traversalBfs(self, simpulAwal):
        Q = Queue(self.N)
        visited = [False] * self.N
        visited[simpulAwal] = True
        Q.insert(simpulAwal)
        
        while(Q.head != 0 and Q.tail != 0):
            w = Q.delete()
            print(self.abjad[w], end=" ")
            for i in range(0, self.N, 1):
                if(self.matriks[w][i] == 1 and visited[i] == False):
                    visited[i] = True
                    Q.insert(i)
        return

    def traversalDfs(self, simpulAwal, visited):
        print(self.abjad[simpulAwal], end=" ")
        visited[simpulAwal] = True
        for w in range (0, self.N, 1):
            if(self.matriks[simpulAwal][w] == 1):
                if(visited[w] == False):
                    self.traversalDfs(w, visited)
    
class Queue():
    def __init__(self, size):
        self.head = 0
        self.tail = 0
        self.maxEl = size
        self.items = [None] * (self.maxEl+1)
    
    def insert(self, X):
        if(self.head == 0 and self.tail == 0):
            self.head = 1
            self.tail = 1
        else:
            if(self.tail == self.maxEl):
                self.tail = 1
            else:
                self.tail += 1
        self.items[self.tail] = X
        return
    
    def delete(self):
        X = self.items[self.head]
        if(self.head == self.tail):
            self.head = 0
            self.tail = 0
        else:
            if(self.head == self.maxEl):
                self.head = 1
            else:
                self.head += 1
        return X

def main():
    totalSimpul = int(input("Jumlah Simpul: "))
    graf = TraversalGraf(totalSimpul)
    graf.fillMatriks()
    visited = [False] * graf.N
    
    print()
    print("========================")
    print("Matriks Adjacency: ")
    print("========================")
    graf.printMatriks()
    
    print()
    print("========================")
    print("Traversal BFS: ")
    print("========================")
    graf.traversalBfs(0)
    
    print()
    print()
    print("========================")
    print("Traversal DFS: ")
    print("========================")
    graf.traversalDfs(0, visited)
if __name__ == '__main__':
    main()