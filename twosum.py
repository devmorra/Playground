def solution(number):
    if number < 0:
        return 0
    mult3 = 3
    mult5 = 5
    validnums = [0]
    while mult3 < number:
        print(mult3)
        validnums.append(mult3)
        mult3 += 3
    while mult5 < number:
        print(mult5)
        if mult5 % 3 != 0:
            validnums.append(mult5)
        mult5 += 5
    print(validnums)
    return sum(validnums)

print(solution(10))
print(solution(200))
print(solution(-10))
print(solution(0))