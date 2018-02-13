def converter(l):
    result = 0
    for idx in range(len(l)):
        result = result + l[idx] * 10**idx
    print(result)

def get_digits(num):
    digits = []
    for i in range(9,1,-1):
        while num % i == 0:
            num = num / i
            digits.append(i)
    converter(digits)

if __name__ == '__main__':
    num_of_case = int(input())
    num_list = []
    for i in range(num_of_case):
        num_list.append(int(input()))
    for num in num_list:
        if num < 10:
            print(10+num)
        elif num == 10:
            print(25)
        else:
            get_digits(num)

# No Collaborators
