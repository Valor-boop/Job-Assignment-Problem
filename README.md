# Job-Assignment-Problem
Solved the Job Assignment Problem using both brute force as well as branch and bound. 
The code contains 5 functions:

job_assignment(cost_matrix):
Find an optimal solution to the job assignment problem using branch and bound. 
Input: an nxn matrix where a row represents a person and a column represents the cost each
person takes to complete the jobs. 
Return: the minimal cost, an optimal solution, and the number of partial or full solutions
evaluated. 

get_csf(cost_matrix, partial_solution):
Input: an nxn cost matrix and a partial solution.
Return: the partial solution's Cost So Far (CSF). 
A partial solution is represented as a list of n elements, where an undecided element is 
denoted by a -1. For instance, a partial solution [2, -1, -1] represents assigning job 2 to 
person 0 and leaving the assignments of person 1 and person 2 undecided. 

get_gfc(cost_matrix, partial_solution):
Input: an nxn cost matrix and a partial solution.
Return: the partial solution's Guaranteed Future Cost (GFC). 

get_ffc(cost_matrix, partial_solution):
Input: an nxn cost matrix and a partial solution. 
Return: the partial solution's Feasible Futre Cost (FFC)

brute_force(cost_matrix):
This function finds an optimal solution for the job assignment problem using brute force. 
Input: an nxn cost matrix. 
Return: the minimal total cost, an optimal solution, and the number of full solutions
investigated. 
