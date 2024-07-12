
#! Operator overloading
class Number:
    def __init__(self,num):
        self.num = num
    
    def __add__(self, obj):
        return self.num + obj.num

    def __sub__(self, obj):
        return self.num - obj.num

    def __mul__(self, obj):
        return self.num * obj.num

    def __truediv__(self, obj):
        return self.num / obj.num

    def __floordiv__(self, obj):
        return self.num // obj.num

    def __mod__(self, obj):
        return self.num % obj.num

    def __pow__(self, obj):
        return self.num ** obj.num

    def __lt__(self, obj):
        return self.num < obj.num

    def __gt__(self, obj):
        return self.num > obj.num

    def __eq__(self, obj):
        return self.num == obj.num
    
    def __str__(self):
        return str(self.num)
    
    def _len_(self):
        return len(str(self.num))


n1 = Number(6)
n2 = Number(5)

print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
print(n1 // n2)
print(n1 % n2)
print(n1 ** n2)
print(n1 < n2)
print(n1 > n2)
print(n1 == n2)
print(n1)
a = len(str(n1))
print(a)