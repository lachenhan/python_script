# Decorator
#不修改函数源代码,给函数增加新功能 -- 封闭开放性原则
##################################################################################
def check(fn):
    def inner():
        print("Please identify.")
        fn()
    return inner

def comment():
    print("Please leave your commands:")

## add identification before comments:
comment = check(comment)  #函数名存放的是函数所在的地址

## add as decorator
@check
def comment():
    print("Please leave your message")

comment()

# Execution time
import time
def count_exc_time(fn):
    def inner():
        start_time = time.time()
        fn()
        end_time = time.time()
        exec_time = end_time - start_time
        print(f"Execution time is {exec_time}")
    return inner


#list_num = count_exc_time(list_num)
@count_exc_time
def list_num():
    for i in range(100):
        print(i)

list_num()

#Decorator with parameters
def logging(fn):
    def inner(a,b):
        fn(a,b)
        print("Trigger function.")
    return inner
@logging
def sum(a,b):
    print(f"sum of {a} and {b} is {a+b}.")

sum(1,2)

#Decorator with any parameters
def logging(fn):
    def inner(*args):
        fn(args)
        print("Trigger function.")
    return inner

@logging
def sum_num(*args):
    print(args)

sum_num(1,2,5)