def greet():
    print("Hello, welcome to the function demo!")
    pass

greet()


def check_weather(temp):
    if temp > 35:
        print(f"The weather is hot at {temp}!!")
    elif temp == 35:
        print(f"Temprature is Ok: {temp}")
    else:
        print(f"Temprture is good{temp}")


check_weather(77)    


def return_multiple_function():
    numb = [1,2,3,4,5,6]
    first_number=numb[0]
    last_number=numb[-1]
    return first_number, last_number

first, last = return_multiple_function()

print(f"Last Number is:{last}, and First Number is:{first}")