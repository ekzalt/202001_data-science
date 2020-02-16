from functools import reduce, lru_cache, wraps
from operator import add, mul
from time import sleep
from collections import defaultdict, Counter, namedtuple
from dataclasses import dataclass

ints = [1, 2, 3]

print(reduce(add, ints))
print(reduce(mul, ints))

print(list(zip(range(3), 'abc', ints)))
print(list(enumerate('abc')))

for i, v in enumerate('hello'):
    print(i, v)

print('\ndecorator\n')


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        result = func(*args, **kwargs)
        print(result)

        return result
    return wrapper


@logger
@lru_cache(maxsize=5)
def my_power(num: int, p: int = 2) -> int:
    sleep(1)
    return num ** p


print(my_power.__name__)
my_power(8)
my_power(8, 2)
my_power(8, p=2)

print('\niterator\n')

for i in ints:
    print(i)

iterator = iter(ints)
iterator_reversed = reversed(ints)

while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration as e:
        print(str(e))
        break

print('after while')

d = {'a': 1, 'b': 2, 'c': 3}

for k, v in d.items():
    print((k, v))

print('\ngenerator\n')

gen = (x ** x for x in range(5) if x > 1)
print(gen)

for i in gen:
    print(i)

print([x ** x for x in range(5) if x > 1])
print([(i, j) for i in range(2) for j in range(2)])


def gen_func():
    yield from (i for i in range(3))


for i in gen_func():
    print(i)

print('\ncorutine\n')


def accumulator():
    total = 0

    while True:
        value = yield total
        print(f'accepted: {value}')

        if value is None:
            break
        else:
            total += value

    yield total


gen = accumulator()
print(next(gen))
print(gen.send(2))
print(gen.send(3))
print(gen.close())  # print(next(gen))

print('\nclass decorators\n')


def singleton(cls):
    instance = None

    @wraps(cls)
    def wrapper(*args, **kwargs):
        nonlocal instance

        if instance is None:
            instance = cls(*args, **kwargs)

        return instance
    return wrapper


@singleton
class SingleClass:
    pass


print('\ncollections\n')

chars = ['a', 'b', 'b', 'c', 'c', 'c']
chars_dict = defaultdict(int)  # support dict interface

for ch in chars:
    chars_dict[ch] += 1

print(chars_dict)

counter = Counter(chars)
print(counter)
print(counter.most_common())

# counter_a + counter_b  # a + b
# counter_a - counter_b  # a - b, values <= 0 wil be ignored
# counter_a & counter_b  # min, values <= 0 wil be ignored
# counter_a | counter_b  # max

# creating readonly dto with namedtuple
User = namedtuple('User', ['user_id', 'name', 'age'], defaults=(0, '', 0))
user = User(1, 'Vasya', 30)
print(user)
print(user.user_id)
print(user[0])
print(User())  # user from defaults


# creating dto with dataclass
@dataclass
class Order:
    order_id: int
    price: int = 0


print(Order(1, 100500))
