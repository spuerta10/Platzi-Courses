

def dynamic_fib(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = dynamic_fib(n-1, memo) + dynamic_fib(n-2,memo)
        memo[n] = result
        return result

if __name__ == "__main__":
    result = dynamic_fib(500)
    print(result)
    
    