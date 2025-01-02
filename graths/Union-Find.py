class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))  # Каждый элемент — родитель сам себе
        self.rank = [0] * size  # Все элементы имеют ранг 0

    def find(self, x):
        if self.parent[x] != x:
            # Рекурсивное обновление родителя
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Присоединяем меньшее дерево к большему
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

def test_union_find():
    uf = UnionFind(10)

    # Объединяем множества
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(2, 3)

    # Проверяем связь между элементами
    assert uf.connected(1, 4) == True, "1 и 4 должны быть соединены"
    assert uf.connected(1, 5) == False, "1 и 5 не должны быть соединены"

    # Проверяем корректность Find
    assert uf.find(1) == uf.find(4), "Корни 1 и 4 должны совпадать"

    print("Все тесты пройдены!")

# Запуск тестов
test_union_find()