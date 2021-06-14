# -*- coding: utf-8 -*-
import heapq
import itertools
'''
The below function uses branch and bound in order
to find an optimal solution for the job assignment problem. 
The number of checked partial or full solutions, the optimal
solutions, and the final optimal cost are all returned. 
The functions get_csf, get_gfc, and get_ffc are called. 
'''
def job_assignment(cost_matrix):
    n = len(cost_matrix)
    global_upper_bound = 0
    
    used_columns = []
    for i in range(n): # Calculate initial global upper bound 
        min_element = float('inf')
        final_min = 0
        for j in range(n):
            if (j not in used_columns): # Check if at a valid column
                if (cost_matrix[i][j] < min_element): # Take min element 
                    min_element = cost_matrix[i][j]
                    final_min = cost_matrix[i][j]
                    savedColumn = j # Save index
        if (final_min != 0):
            used_columns.append(savedColumn) # Add used column 
            global_upper_bound += final_min
     
    P = [] # Create min heap
    counter = 5
    for i in range(n): # Initialize partial solution values
        partial_solution = [i]+[-1]*(n-1)
        gfc = get_gfc(cost_matrix,partial_solution)
        csf = get_csf(cost_matrix,partial_solution)
        lower_bound = gfc + csf # Get lower bound 
        partial_tuple = (lower_bound, partial_solution) # (lower_bound, partial)
        heapq.heappush(P, partial_tuple)
        
    while len(P) != 0 :
        partial_tuple = heapq.heappop(P) # Pop smallest value 
        partial_solution = partial_tuple[1] # Get partial solution 
        if (partial_solution[-1] != -1): # Full solution found 
            final_sum = get_csf(cost_matrix, partial_solution) # Get final cost 
            return final_sum, partial_solution, counter+1
        else:
            extended = []
            for i in list(range(n)): # Get possible extensions 
                if (i not in partial_solution):
                    extended.append(i)
            i = n - len(extended)
            
            for j in extended:
                counter += 1
                partial_solution[i] = j
                csf = get_csf(cost_matrix, partial_solution) # Get CSF
                gfc = get_gfc(cost_matrix, partial_solution) # Get GFC
                ffc = get_ffc(cost_matrix, partial_solution) # Get FFC 
                lower_bound = csf + gfc # Get lower bound for partial 
                upper_bound = csf + ffc # Get upper bound for partial
                if (lower_bound > global_upper_bound): # Eliminate partial
                    continue
                else:
                    temp_sol = partial_solution.copy()
                    partial_tuple = (lower_bound,temp_sol)
                    heapq.heappush(P, partial_tuple) # Add partial solution to heap
                    if (upper_bound < global_upper_bound): # Update upper bound 
                        global_upper_bound = upper_bound
                        
                        
'''
The following function takes a cost matrix and a 
partial solution and calcualtes the Cost So Far
for that partial solution.
'''
def get_csf(cost_matrix, partial_solution):
    csf = 0
    for i in range (len(cost_matrix)):
        if (partial_solution[i] != -1): # Ignore if -1 (not assigned)
            csf += cost_matrix[i][partial_solution[i]] # Get aassigned values
    return csf


'''
The following function takes a cost matrix and
a partial solution and calculates the Guaranteed
Future Cost for that partial solution.
'''
def get_gfc(cost_matrix, partial_solution):
    gfc = 0
    n = len(cost_matrix)
    free_rows = []
    free_columns = []
    
    for i in list(range(len(cost_matrix))): # Get free columns 
        if (i not in partial_solution):
            free_columns.append(i)

    for i in list(range(len(cost_matrix))): # Get free rows 
        if (partial_solution[i] == -1):
            free_rows.append(i)
            
    for i in range(n):  # Loop through rows  
        min_element = float('inf') # Initial min value 
        final_min = 0
        for j in range(n): # Loop through columns  
            if (i in free_rows and j in free_columns): # Check if at free col/row
                if (cost_matrix[i][j] < min_element): # Find min value 
                    min_element = cost_matrix[i][j]
                    final_min = cost_matrix[i][j]
        gfc += final_min
    return gfc 


'''
The following function takes a cost matrix and 
a partial solution and calculates the Feasible Future Cost 
for that partial solution.
'''
def get_ffc (cost_matrix, partial_solution):
    ffc = 0
    n = len(cost_matrix)
       
    free_rows = []
    free_columns = []
    
    for i in list(range(len(cost_matrix))): # Get free columns 
        if (i not in partial_solution):
            free_columns.append(i)

    for i in list(range(len(cost_matrix))): # Get free rows 
        if (partial_solution[i] == -1):
            free_rows.append(i)
            
    for i in range(n): # Loop through rows 
        min_element = float('inf')
        final_min = 0
        saved_column = 0
        saved_row = 0
        for j in range(n): # Loop through columns  
            if (i in free_rows and j in free_columns): # Check if at a valid row/column
                if (cost_matrix[i][j] < min_element): # Find min element 
                    min_element = cost_matrix[i][j]
                    final_min = cost_matrix[i][j]
                    saved_column = j # Save index
                    saved_row = i # Save index
        
        if (final_min != 0):
            free_rows.remove(saved_row) # Remove used row
            free_columns.remove(saved_column) # Remove used column 
            ffc += final_min
    return ffc 


'''
The below function returns an optimal solution for the job assignment
problem using a bruteforce algorithm. All permutations of the 
n x n matrix are calculated and then the minimum value is taken.
The number of checked solutions, the optimal solution and the optimal
value are all returned. Used the import itertools. 
'''
def brute_force(cost_matrix):
    permutes_list = itertools.permutations(list(range(len(cost_matrix)))) # All permutations of matrix
    final_sum = float('inf')
    counter = 0
    for possible in permutes_list: # Iterate through permutations 
        counter += 1
        temp_cost = 0
        for i in possible: # Get cost of each permutation 
            temp_cost += cost_matrix[i][possible[i]] # Get cost of permutation 
        if (temp_cost < final_sum): # Find min cost 
            final_sum = temp_cost # Cost
            optimal_sol = possible # Solution
    return final_sum, list(optimal_sol), counter
