# # Decorator function
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# # Apply the decorator using the @ syntax
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# # Call the decorated function
# say_hello()
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} executed")
        return result
    return wrapper

@log_function_call
def add(x, y):
    return x + y

result = add(3, 5)
print(result)  # Output: 8