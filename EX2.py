print("Summation of harmonic series")
def cal(n):
        if n < 2:
            return 1

        else:
            return 1 / n + (cal(n - 1))

print("Limit = 1 Value = ",cal(1))
print("Limit = 2 Value = ",cal(2))
print("Limit = 3 Value = ",cal(3))
print("Limit = 4 Value = ",cal(4))
print("Limit = 5 Value = ",cal(5))
print("Limit = 6 Value = ",cal(6))
print("Limit = 7 Value = ",cal(7))
print("Limit = 8 Value = ",cal(8))
print("Limit = 9 Value = ",cal(9))
print("Limit = 10 Value = ",cal(10))
print(cal(10))