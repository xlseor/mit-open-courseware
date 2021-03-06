# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    #recursive implementation: returns all possible first letters,
    #and for each, makes a recursive call to the function to complete
    #the permutation of the rest of the letters, which it appends to the list.
    
    #initialize list
    n = len(sequence)
    main_list = []
    k=0
    if n == 1:
        return [sequence]
    while k < n:
        star = sequence[k]
        sub_seq = sequence[0:k]+sequence[k+1:n]
        perms_list = get_permutations(sub_seq)
        i = 0
        for item in perms_list:
            perms_list[i] = star+item
            i+=1
        main_list = main_list + perms_list
        k+=1
    return main_list   
        
if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    input1 = 'x'
    input2 = 'xy'
    input3 = 'xyz'

    print("Input: " + input1)
    print("Expected output: ['x']")
    print("Actual output: ", get_permutations(input1))
    print("")
    print("test 2:")
    print("")
    print("Input: " + input2)
    print("Expected output: ['xy, 'yx']")
    print("Actual output: ", get_permutations(input2))
    print("")
    print("test 3:")
    print("")
    print("Input: "+ input3)
    print("Expected output: ['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx']")
    print("Actual output: ", get_permutations(input3))
