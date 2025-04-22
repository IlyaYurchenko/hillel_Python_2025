def say_hi(name, age) -> str:
    res = f"Hi. My name is {name} and I'm {age} years old"
    print(res)
    return res

assert say_hi("Alex", 32)
assert say_hi("Frank", 68)