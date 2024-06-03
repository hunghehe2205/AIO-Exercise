import math
import random


#Exercise 1
def calculate_F1_score(tp, fp, fn):
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    print(f"Precision is {precision}")
    print(f"Recall is {recall}")
    print(f"F1_Score is {f1_score}")
   
    
def exercise1(tp, fp, fn):
    if not isinstance(tp,int):
        print("TP must be int")
        return
    elif tp <= 0:
        print("TP must > 0")
        return
    if not isinstance(fp, int):
        print("FP must be int")
        return
    if fp <= 0:
        print("FP must > 0")
        return
    if not isinstance(fn, int):
        print("FN must be int")
        return
    if fn <= 0:
        print("FN must > 0")
        return
    calculate_F1_score(tp, fp, fn)


#Exercise 2
# Activation Function

def sigmoid_function(x):
    res = 1 / (1 + math.exp(-x))
    return res


def relu_function(x):
    if x <= 0:
        return 0
    else:
        return x
    

def elu_function(x):
    if  x <= 0:
        res = 0.01 * (math.exp(x) - 1)
        return res
    else:
        return x
    

def is_number(n):
    try :
        float(n)
    except ValueError :
        return False
    return True


def exercise2():
    x = input("Please input x: ")
    if not is_number(x) :
        print("X must be a float")
    else:
        x = float(x)
        function = input("Input activation Function ( sigmoid | relu | elu )")  
        if function == "sigmoid" :
            print(f"Sigmoid: f({x}) = {sigmoid_function(x)}")
        elif function == "relu" :
            print(f"ReLU: f({x}) = {relu_function(x)}")
        elif function == "elu" :
            print(f"Elu: f({x}) = {elu_function(x)}")
        else:
            print(f"{function} is not supported")


#Exercise3


def mae_function(target, predict):
    mae_list = [abs(x - y) for x,y in zip(target, predict)]
    return mae_list


def mse_function(target, predict):
    mse_list = [(x -y) ** 2 for x,y in zip(target, predict)]
    return mse_list


def rmse_function(target, predict):
    return mse_function(target,predict)


def exercise3():
    num_samples = input("Input number of samples ( integer number ) which are generated")
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return
    else:
        target = []
        predict = []
        num_samples = int(num_samples)
        for _ in range(num_samples):
                   target.append(random.uniform(0,10))
                   predict.append(random.uniform(0,10))
        loss_function = input("Input loss name: ")
        res = []
        if loss_function == "MSE":
            res = mse_function(target,predict)
        elif loss_function == "MAE":
            res = mae_function(target,predict)
        else:
            res = mae_function(target,predict)
        for i in range(0,num_samples):
            print(f"loss name: {loss_function}, sample: {i}, pred: {predict[i]}, target: {target[i]}, loss: {res[i]}")
        print(f"final {loss_function}: {sum(res) / len(res)}")
                
        
#Exercise 4 
def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
    
def approx_sin(x,n):
    res = 0
    for i in range(0,n):
        val = (-1)**i * (x**(2*i + 1)) / factorial(2*i+1)
        res = res + val
    return res


def approx_cos(x,n):
    res = 0
    for i in range(0,n):
        val = ((-1)**i) * (x**(2*i)) / factorial(2*i)
        res = res + val
    return res

def approx_sinh(x,n):
    res = 0
    for i in range(0,n):
        val = x**(2*n+1) / factorial(2*n+1)
        res = res + val
    return res


def approx_cosh(x,n):
    res = 0
    for i in range(0,n):
        val = x**(2*n) / factorial(2*n)
        res = res + val
    return res


#Exercise 5

def md_nre_single_sample(y, y_hat, n, p):
    y_root = y ** (1/n)
    y_hat_root = y_hat ** (1/n)
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss

     
if __name__ == "__main__":
    print(approx_cos(3.14,10))
    
