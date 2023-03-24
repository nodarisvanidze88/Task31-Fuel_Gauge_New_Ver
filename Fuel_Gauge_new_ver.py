def main():
    print("Please use only division")
    user = input("Fraction: ")
    print(gauge(convert(user)))


def convert(fraction):
    fraction = list(fraction)
    try:
        ind = fraction.index("/")
    except:
        pass
    if "/" not in fraction:
        raise ValueError('Need use division \"\\"')
    try:
        x = int("".join(map(str, fraction[:ind])))
        y = int("".join(map(str, fraction[ind+1:])))
    except:
        raise ValueError("Division should be between integers")
    if fraction.count("/") > 1:
        raise ValueError("Incorrect Division")
    if y == 0:
        raise ZeroDivisionError("Division by 0 is impossible")
    if x > y:
        raise ValueError("Result percentage must be between 0 and 100")
    result = (x / y) * 100
    return result


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
