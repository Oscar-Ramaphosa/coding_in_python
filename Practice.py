
def Numbers(arr, j):
    # To store the count
    count = 0

    # Sort the original array
    arr.sort()
    i = 0
    while i < (j - 1):

        #if statement for a valid pair is found
        if (arr[i] == arr[i + 1]):
            count += 1
            # Skip the elements of the current pair
            i = i + 2

        # an else if for current elements doesn't make a valid pair with any other element
        else:
            i += 1
    return ("There are " + str(count) + " good pairs.") #the number of pairs found
arr= [10,20,10,40,50,45,30,70,5,20,45]
n = len(arr)
print(Numbers(arr, n)) #print out all the numbers