def gradient_descent(derivative_func, initial_guess, multiplier = 0.01 , precision = 0.0001 , max_iter = 300):
    new_x = initial_guess
    
    #The following 2 lists are for graphing purposes
    x_list = [new_x] 
    slope_list = [derivative_func(new_x)]
    
    for i in range(max_iter):
        previous_x = new_x
        gradient = derivative_func(new_x)
        new_x = previous_x - gradient * multiplier
        
        x_list.append(new_x)
        slope_list.append(derivative_func(new_x))
        
        step_size = abs(new_x - previous_x)
        if step_size < precision:
            break
    
    return new_x, x_list, slope_list
