import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sts

class Simulator:
    arr = []

    def __str__(self):
        return 'Класс "Стохастический симулятор распределений"'

    def __init__(self, n): # Конструктор класса
        # Генерируем массив случайных равномерно распределенных величин
        self.norm_rv = sts.norm(loc = 2.0, scale = 0.5)
        self.arr = np.linspace(0, 10, n)
        self.size = n
        print('Массив arr равномерно распределенных чисел: \n', self.arr)

    def Gaussian(self):
        # Генерируем выборку на основе массива, определенного в конструкторе
        cdf = self.norm_rv.cdf(self.arr)
        print('Массив величин распределенных по закону нормального распределения: \n', cdf, )
        plt.title('Нормальное распределение')
        plt.plot(self.arr, cdf)
        plt.ylabel('$F(x)$')
        plt.xlabel('$x$')
        plt.grid(True)
        plt.show()

    def Exponential(self):
        rv = sts.expon()
        # Генерируем выборку на основе массива, определенного в конструкторе
        cdf = rv.cdf(self.arr)
        print('Массив величин распределенных по закону экспоненциального распределения: \n', cdf)
        plt.title('Экспоненциальное распределение')
        plt.plot(self.arr, cdf)
        plt.ylabel('$F(x)$')
        plt.xlabel('$x$')
        plt.grid(True)
        plt.show()

    def Cauchy(self):
        rv = sts.cauchy()
        # Генерируем выборку на основе массива, определенного в конструкторе
        cdf = rv.cdf(self.arr)
        print('Массив величин распределенных по закону распределения Коши: \n', cdf)
        plt.title('Распределение Коши')
        plt.plot(self.arr, cdf)
        plt.ylabel('$F(x)$')
        plt.xlabel('$x$')
        plt.grid(True)
        plt.show()

    def Poisson(self):
        lambd = 5 # Параметр лямбда Пуассоновского распределения
        rv = sts.poisson(lambd)
        # Генерируем выборку на основе массива, определенного в конструкторе
        cdf = rv.cdf(self.arr)
        print('Массив величин распределенных по закону распределения Пуассона: \n', cdf)
        plt.title('Распределение Пуассона')
        plt.plot(self.arr, cdf)
        plt.ylabel('$F(x)$')
        plt.xlabel('$x$')
        plt.grid(True)
        plt.show()

    def Chi_Square(self):
        k = 1 # Натуральный параметр k распределения хи-квадрат
        rv = sts.chi2(k)
        # Генерируем выборку на основе массива, определенного в конструкторе
        cdf = rv.cdf(self.arr)
        print('Массив величин распределенных по закону распределения Хи-квадрат: \n', cdf)
        plt.title('Распределение хи-квадрат')
        plt.plot(self.arr, cdf)
        plt.ylabel('$F(x)$')
        plt.xlabel('$x$')
        plt.grid(True)
        plt.show()

    def Binomial(self):
        rv = sts.binom(self.size, 0.1) # Параметры - количество и вероятность
        # Генерируем выборку на основе массива, определенного в конструкторе
        cdf = rv.cdf(self.arr)
        print('Массив величин распределенных по закону биномиального распределения: \n', cdf)
        plt.title('Биномиальное распределение')
        plt.plot(self.arr, cdf)
        plt.ylabel('$F(x)$')
        plt.xlabel('$x$')
        plt.grid(True)
        plt.show()

Sim = Simulator(100) # Создаем объект класса с размером выборки 100
print(Sim)
# Методы класса
Sim.Gaussian()
Sim.Exponential()
Sim.Cauchy()
Sim.Poisson()
Sim.Chi_Square()
Sim.Binomial()