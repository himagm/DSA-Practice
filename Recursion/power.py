def power(base, expo):
    if expo == 0:
        return 1
    if expo == 1:
        return base
    return base * power(base, expo-1)

if __name__ == "__main__":
    print(power(2,1))