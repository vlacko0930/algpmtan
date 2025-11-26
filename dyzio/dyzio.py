import sys

sys.setrecursionlimit(30000)

def solve_recursive(iterator, current_depth, cuts_before_me):
    try:
        char = next(iterator)
    except StopIteration:
        return 0, 0, 0

    if char == '0':
        return (current_depth, cuts_before_me, 0)

    else:
        l_depth, l_win, l_consumed = solve_recursive(
            iterator, 
            current_depth + 1, 
            cuts_before_me + 1
        )
        
        r_depth, r_win, r_consumed = solve_recursive(
            iterator, 
            current_depth + 1, 
            cuts_before_me + 1 + l_consumed
        )
        
        my_total_consumed = 1 + l_consumed + r_consumed
        
        if r_depth > l_depth:
            return (r_depth, r_win, my_total_consumed)
        else:
            return (l_depth, l_win, my_total_consumed)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    data_iter = iter(input_data)
    
    try:
        while True:
            _ = next(data_iter)
            
            s = next(data_iter)
            
            _, result, _ = solve_recursive(iter(s), 0, 0)
            
            print(result)
            
    except StopIteration:
        pass

if __name__ == "__main__":
    main()