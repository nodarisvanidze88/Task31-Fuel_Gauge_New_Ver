from Fuel_Gauge_new_ver import gauge
from Fuel_Gauge_new_ver import convert
import pytest

def main():
    testConverter()

def testConverter():
    assert convert("4/5") == 80
    assert convert("1/5") == 20
    assert convert("-5/5") == -100
    with pytest.raises(ValueError, match=r"Result percentage must be between 0 and 100"):
        convert("5/-5")
    with pytest.raises(ValueError, match=r"Result percentage must be between 0 and 100"):
        convert("5/4")
    with pytest.raises(ValueError, match=r"Division should be between integers"):
        convert("Cat/Dog")
    with pytest.raises(ZeroDivisionError, match=r"Division by 0 is impossible"):
        convert("10/0")
    with pytest.raises(ValueError, match=r"Division should be between integers"):
        convert("10.5/20.5")
    with pytest.raises(ValueError, match=r'Need use division \"\\"'):
        convert("12345")
    with pytest.raises(ValueError, match=r'Need use division \"\\"'):
        convert("5+5")
    assert convert("-10/-5") == 200
    assert convert("1/100") == 1
    assert convert("4/4") == 100

def testGauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(-100) == "E"
    assert gauge(100) == "F"
    assert gauge(200) == "F"
    assert gauge(80) == "80%"
    assert gauge(20) == "20%"


if __name__ == "__main__":
    main()
