def GeometricSum(k):
    if k == 0:
        return 1
    else:
        return 1/(2**k) + GeometricSum(k-1)

def main():
    k = int(input())
    result = GeometricSum(k)
    print("{:.5f}".format(result))

if __name__ == "__main__":
    main()
