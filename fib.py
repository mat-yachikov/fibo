# Рекурсивная функция для чисел Фибоначчи
def fib(n):
    # Условия выхода из рекурсии
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        # Рекурсивный вызов
        return fib(n-1) + fib(n-2)


# Ввод кол-ва чисел
n = int(input())
# Список для чисел
nums = []
# Открываем файл
f = open('out.txt', 'w')

# Заполняем список
for i in range(n):
    nums.append(fib(i))

# Вывод на консоль
for i in range(n):
    print(nums[i], end=' ')
print('\n')
for i in range(n):
    print(bin(nums[i]), end=' ')
print('\n')
for i in range(n):
    print(hex(nums[i]), end=' ')

# Вывод в файл
for i in range(n):
    f.write(str(nums[i])+'\t'+str(bin(nums[i]))+'\t'+str(hex(nums[i]))+'\n')

# Закрываем файл
f.close()
