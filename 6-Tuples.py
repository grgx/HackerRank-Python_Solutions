# https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))

    print(hash(t))