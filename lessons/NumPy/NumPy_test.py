# Для этого напишите функцию shuffle_seed(<array>),  которая принимает на вход массив из чисел,
# генерирует случайное число для seed в диапазоне от 0 до 2**32 - 1 (включительно) и возвращает
# кортеж: перемешанный с данным seed массив (исходный массив должен оставаться без изменений),
# а также seed, с которым этот массив был получен.
def shuffle_seed(array):
    seed = np.random.randint(0,2**32-1)
    np.random.seed(seed)
    return tuple(np.random.permutation(array),seed)

# Напишите функцию min_max_dist, которая принимает на вход неограниченное число векторов через запятую.
# Гарантируется, что все векторы, которые передаются, одинаковой длины.
# Функция возвращает минимальное и максимальное расстояние между векторами в виде кортежа.
import numpy as np
def min_max_dist(*args):
    list_vecs = list(args)
    min_dist = max_dist = np.linalg.norm(list_vecs[0]-list_vecs[1])
    for i in range(len(list_vecs)):
        for j in range(i+1,len(list_vecs)):
            dist = np.linalg.norm(list_vecs[i]-list_vecs[j])
            min_dist = min(min_dist, dist)
            max_dist = max(max_dist, dist) 
    return (min_dist,max_dist)
vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7,8,9])
 
print(min_max_dist(vec1, vec2, vec3))


# Напишите функцию any_normal, которая принимает на вход неограниченное число векторов через запятую.
# Гарантируется, что все векторы, которые передаются, одинаковой длины.
# Функция возвращает True, если есть хотя бы одна пара перпендикулярных векторов. Иначе возвращает False.

import numpy as np
def any_normal(*args):
    list_vecs = list(args)
    for i in range(len(list_vecs)):
        for j in range(i+1,len(list_vecs)):
            if not np.dot(list_vecs[i],list_vecs[j]):
                return True
    return False
vec1 = np.array([2, 1])
vec2 = np.array([-1, 2])
vec3 = np.array([3, 4])
 
print(any_normal(vec1, vec2))

# Напишите функцию get_loto(num), генерирующую трёхмерный массив случайных целых чисел от 1 до 100 (включительно).
# Это поля для игры в лото.
# Трёхмерный массив должен состоять из таблиц чисел формы 5х5, то есть итоговая форма — (num, 5, 5).
# Функция возвращает полученный массив.

def get_loto(num):
    return np.random.randint(1,101,size=(num,5,5))
    
    
# Напишите функцию get_unique_loto(num).
# Она так же, как и функция в задании 10.10, генерирует num полей для игры в лото,
# однако теперь на каждом поле 5х5 числа не могут повторяться.
# Функция также должна возвращать массив формы num x 5 x 5.
def get_unique_loto(num):
    sample = np.arange(1,101)
    res = list()
    for i in range(num):
        res.append(np.random.choice(sample,size=(5,5),replace=False))
    return np.array(list)


