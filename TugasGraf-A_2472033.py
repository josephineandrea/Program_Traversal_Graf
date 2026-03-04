# Method Traversal Graf dengan BFS dan DFS diambil
# dari power point "Struktur Graf"
# 2472033 Josephine Andrea Sanjaya

## Definisi Kelas ##
## Definisi Kelas TraversalGraf : kelas untuk
## melakukan traversal graf dengan metode BFS dan DFS
## Definisi Atribut
## N : jumlah simpul pada graf (integer)
## matriks : matriks adjacency untuk menyimpan data graf
## (array 2 dimensi)
## abjad : list untuk menyimpan nama simpul pada graf
## (array of string)

class TraversalGraf():
    
    ## Definisi Konstruktor
    # Kamus Lokal
    # size : ukuran array (integer)
    # i : variabel pengendali for (integer)
    def __init__(self, size):
        self.N = size
        self.matriks = [None] * self.N
        for i in range(0, self.N, 1):
            self.matriks[i] = [None] * self.N
        self.abjad = [None] * self.N
        for i in range(0, self.N, 1):
            self.abjad[i] = chr(ord('A') + i)
        return
    
    ## Definisi Method fillMatriks(self)
    # method untuk mengisi matriks adjacency
    # Kamus Lokal
    # i : variabel pengendali for (integer), baris
    # j : variabel pengendali for (integer), kolom
    def fillMatriks(self):
        for i in range(0, self.N, 1):
            print("=======================")
            print(f"Baris {i}")
            print("=======================")
            for j in range(0, self.N, 1):
                print(f"Kolom {j}: ", end="")
                self.matriks[i][j] = int(input())
        return
    
    ## Definisi Method printMatriks(self)
    # method untuk mencetak matriks adjacency
    # Kamus Lokal
    # i : variabel pengendali for (integer), baris
    # j : variabel pengendali for (integer), kolom
    def printMatriks(self):
        for i in range(0, self.N, 1):
            for j in range(0, self.N, 1):
                print(self.matriks[i][j], end=" ")
            print()
        return
    
    ## Definisi Method traversalBfs(self, simpulAwal)
    # method untuk melakukan traversal BFS pada graf
    # Kamus Lokal
    # Q : queue untuk menyimpan simpul yang akan dikunjungi (Queue)
    # visited : list untuk menyimpan boolean untuk simpul (array of boolean)
    # w : variabel untuk menyimpan simpul yang sedang dikunjungi (integer)
    # simpulAwal : simpul awal untuk traversal (integer)
    # i : variabel pengendali for (integer)
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

    ## Definisi Method traversalDfs(self, simpulAwal)
    # method untuk melakukan traversal DFS pada graf
    # Kamus Lokal
    # visited : list untuk menyimpan boolean untuk simpul (array of boolean)
    # w : variabel untuk menyimpan simpul yang sedang dikunjungi juga 
    # pengendali for (integer)
    # simpulAwal : simpul awal untuk traversal (integer)
    def traversalDfs(self, simpulAwal, visited):
        print(self.abjad[simpulAwal], end=" ")
        visited[simpulAwal] = True
        for w in range (0, self.N, 1):
            if(self.matriks[simpulAwal][w] == 1):
                if(visited[w] == False):
                    self.traversalDfs(w, visited)

## Definisi Kelas ##
## Definisi Kelas Queue : kelas untuk
## menyimpan simpul yang akan dikunjungi pada traversal BFS
## Definisi Atribut
## head : indeks untuk simpul pertama pada queue (integer)
## tail : indeks untuk simpul terakhir pada queue (integer)
## maxEl : ukuran maksimal queue (integer)
## items : array untuk menyimpan simpul pada queue (array of integer)

class Queue():
    
    ## Definisi Konstruktor
    # Kamus Lokal
    # size : ukuran queue (integer)
    def __init__(self, size):
        self.head = 0
        self.tail = 0
        self.maxEl = size
        self.items = [None] * (self.maxEl+1)
    
    ## Definisi Method insert(self, X)
    # Kamus Lokal
    # X : nilai yang akan ditambahkan (integer)
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
    
    ## Definisi Method delete()
    # Kamus Lokal
    # X : nilai yang akan dibuang (integer)
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

## Program utama ##
# Kamus Lokal
# totalSimpul : jumlah simpul yang diinput user (integer)
# graf : inisiasi objek dari kelas TraversalGraf (TraversalGraf)
# visited : list untuk menyimpan boolean untuk simpul (array of boolean)
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