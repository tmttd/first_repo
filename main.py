## 마크다운 추가

def check_available():
    return "It works!"

def remove_odd(nums = [1, 2, 3, 4]):
    return [num for num in nums if num%2 == 0]

if __name__ == '__main__':
    # print(check_available())
    print(remove_odd())
