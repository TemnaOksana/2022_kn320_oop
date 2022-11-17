class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in ["квадрат", "ромб", "коло"], "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

a = Figure("квадрат", 12)
print(a.type, a.length)
b = Figure("циліндр", 10)
print(b.type, b.length)
c = Figure("коло", 1)
print(c.type, c.length)