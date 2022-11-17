# Звіт до роботи №5 
## Тема: Тестування

### Мета роботи: Навчитись працювати з тестуванням на Python. 

----
----

### Виконання роботи
- Результати виконання завданнь:
    1. # :cloud: Перевірка assert 
    ```python
    number = 2
    assert number < 0, "число має бути меншим за нуль!"
    ```
#### Рис. 1
![any text](https://github.com/TemnaOksana/2022_kn320_oop/raw/main/photo/51.jpg)
2. ## :cloud: Створила власний крок `assert` та зробила тестові превірки при введенні даних з клавіатури. Для цього використала метод `input`:
    ```python
    a = input("Введіть число- ")
    assert a.isdigit(), "ВВЕДИ ЧИСЛО!!!"
    print(f"введене число- {a}")
    ```
    #### Рис. 2
![any text](https://github.com/TemnaOksana/2022_kn320_oop/raw/main/photo/52.jpg)

3. ## :cloud: Перевірка (валідація)
```python
    class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

    #a = Figure("трапеція", 12)
    #b = Figure("квадрат", 0)
    c = Figure("квадрат", 1)
```
### Ввід фігури, якої нема в переліку дозволених
  #### Рис. 3
![any text](https://github.com/TemnaOksana/2022_kn320_oop/raw/main/photo/54.jpg)
### Ввід фігури з переліку дозволених
  #### Рис. 4
![any text](https://github.com/TemnaOksana/2022_kn320_oop/raw/main/photo/53.jpg)

4. # :cloud: Юніт тести

![any text](https://github.com/TemnaOksana/2022_kn320_oop/raw/main/photo/55.jpg)

5. # :cloud: Юніт тести з використання бібліотеки PyTest
### Я створила віртуальне середовище та інсталювала туди бібліотеку `PyTest` До `арр.ру` додав таку функцію:
```python
def test_app_triangle():
    """Test if we create triangle figure.
    """
    fig = "трикутник"
    len = 4
    col = 'blue'
    triangle = Figure(fig, len, col)
    assert triangle.type == fig, f"Фігура має бути {fig}"
```
### Ось що вивів PyTest:
```
================== test session starts ==================
platform win32 -- Python 3.10.6, pytest-7.1.3, pluggy-1.0.0
rootdir: c:\Users\Ruslan\Desktop\readme\2022_kn320_oop-2\5_lab
collected 1 item

app.py .              [100%]

================== 1 passed in 0.02s ==================
```
### А це вивід вісля запуску Test_app.py:

```
================== test session starts ==================
platform win32 -- Python 3.10.6, pytest-7.1.3, pluggy-1.0.0
rootdir: c:\Users\Ruslan\Desktop\readme\2022_kn320_oop-2\5_lab
collected 4 items

Test_app.py .F..   [100%]

================== FAILURES ==================
__________________ TestFigure.test_figure_lengh __________________

self = <Test_app.TestFigure testMethod=test_figure_lengh>

    def test_figure_lengh(self):
>       self.assertEqual(self.length, self.obj.get_figure_length,
                         "Властивість get_figure_length повертає непривильну довжину!")
E       AssertionError: 4 != 'квадрат' : Властивість get_figure_length повертає непривильну довжину!

Test_app.py:33: AssertionError
================== short test summary info ==================
FAILED Test_app.py::TestFigure::test_figure_lengh - AssertionError: 4 != 'квадрат' : Властивість get_figure_length повертає непривильну довжину!
================== 1 failed, 3 passed in 0.10s ==================
```

# :cloud: Візуалізація результатів та покриття коду Coverage (pytest-cov)

```
Name     Stmts   Miss  Cover
----------------------------
app.py      25      5    80%
----------------------------
TOTAL       25      5    80%
```
   
----
----

# Висновок: 
:cloud: Під час виконання лабораторної роботи Я навчилась працювати з тестуванням на Python.
