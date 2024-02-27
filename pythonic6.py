# 6. 실용성은 순수성보다 중요하다 (Practicality beats purity)
# 실용적인 코드 작성이 이론적으로 완벽한 코드보다 더 중요합니다. 파이썬은 실제 문제를 해결하는 데 초점을 맞춥니다.

# - **기능적 접근 대신 실용적 접근**:
result = list(map(lambda x : x ** 2, filter(lambda x : x % 2 == 0, range(10))))
print(result)

result = [x ** 2 for x in range(10) if x % 2 == 0]
print(result)

# 성능을 위한 실용적 최적화:
def is_prime_1(n):
    return n > 1 and all(n % i for i in range(2,n))
def is_prime_2(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
        return True
    
print(is_prime_1(10007))
print(is_prime_2(10007))

class Animal:
    pass
class Dog(Animal):
    pass

def make_sound(animal_type):
    sounds = {'dog':'bark','cat':'meow'}
    return sounds.get(animal_type,'unknown')