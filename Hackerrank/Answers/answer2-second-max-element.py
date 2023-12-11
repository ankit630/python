if __name__ == '__main__':
    n = int(input())
    # Create array list with element as int
    arr = list(map(int, input().split()))
    
    # find the max number in list
    max_element = max(arr)

   # initalize a empty list
    updated_list = []
  
   # Iteriate over element in list and append all the element in list except max element to create new list
    for element in arr:
        if element != max_element:
            updated_list.append(element)

  # fix the max element in the list again that would find the 2nd max element in the list
    print(max(updated_list))
