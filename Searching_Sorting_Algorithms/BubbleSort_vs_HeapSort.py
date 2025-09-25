
import random
import timeit


def print_menu():
    print("menu----------------------------------")
    print("1-->generate a list of random numbers")
    print("2-->sort the list using bubble sort")
    print ("3-->sort the list using the heap sort")
    print("4-->exit the program")
    print("5-->best case")
    print("6-->avrage case")
    print ("7-->worst case")
    print("choose an option:")
    return input("-->")

def cases_menu():
    print("cases_menu------------------------------")
    print("1-->bubble sort")
    print("2-->heap sort")
    print("3-->exit menu")
    return input("-->")

def lists_menu():
    print("lists_menu------------------------------")
    print("1-->50 elements")
    print("2-->100 elements")
    print("3-->250 elements")
    print("4-->500 elements")
    print("5-->1000 elements")
    print("6-->exit menu")
    return input("-->")

def random_numbers(n):
    list = []
    for i in range (1,n+1):
        list.append(random.randint(0,100))
    return list

def ascending(list):
    list.sort()
    return list

def descending(list):
    list.sort(reverse=True)
    return list

def identical(list):
    l=len(list)
    for i in range (1,l):
        list[i]=list[1]
    return list

def different(list):
    l=len(list)
    for i in range (1,l):
        nr=list[i]
        k=i
        for j in range (1,l):
            if list[j]==nr and j!=i:
                list[j]=list[j]+1
    return list


def bubble_sort(list):
    n=len(list)
    for i in range(n):
        arranged =False
        for j in range(0,n-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
                arranged= True
        if arranged==False :
            break

def heapify(list2,size,root):
    largest=root
    l=2*root+1
    r=2*root+2
    if l<size and list2[largest]<list2[l]:
        largest=l
    if r<size and list2[largest]<list2[r]:
        largest=r
    if largest !=root:
        list2[root],list2[largest]=list2[largest],list2[root]
        heapify(list2,size,largest)



def heapMain(list):
    list2=list.copy()
    size=len(list2)
    for root in range (size//2-1,-1,-1):
        heapify(list2,size,root)

    for root in range (size-1,0,-1):
        list2[root],list2[0]=list2[0],list2[root]
        heapify(list2, root, 0)
    print("the sorted list: ",list2)









def start():
    ok=0
    while True :
        try:
            option = int(print_menu())
        except:
            print("invalid option")
            pass


        if option==1:
            print("length of the list: ")
            n=int(input())
            arr = random_numbers(n)
            print(arr)
            ok=1
            arr50=random_numbers(50)
            arr100=random_numbers(100)
            arr250=random_numbers(250)
            arr500=random_numbers(500)
            arr1000=random_numbers(1000)


        elif option==2:
            if ok==1:
                print("step number: ")
                s=int(input())
                bubble_sort(arr)
            else :print("the list doesn't exist.Choose first option 1")


        elif option==3:
            if ok==1:
                print("step number: ")
                s = int(input())
                heapMain(arr)
                print("the sorted list: ",arr)
            else:print("the list doesn't exist.Choose first option 1")


        elif option==4:
            break


        elif option==5:  #best case
            if ok==1:
                while True:
                    try:
                        option = int(cases_menu())
                    except:
                        print("invalid option")
                        pass

                    if option == 1:  #bubble sort
                        """the best case for this type of sorting is when the arrey is already sorted
                        such that the number of comparasion required is n-1 and there will be no swaps
                        The best case complexity is O(n)"""
                        while True:
                            try:
                                option = int(lists_menu())
                            except:
                                print("invalid option")
                                pass
                            if option == 1:    #50 elements
                                aux50 = arr50
                                ascending(aux50)
                                default_time = timeit.default_timer()
                                bubble_sort(aux50)
                                end_time = timeit.default_timer()
                                total_time = end_time-default_time
                                print("time elapsed for best case in bubble sort with 50 elements is: ",total_time)
                            elif option==2:    #100 elements
                                aux100 = arr100
                                ascending(aux100)
                                default_time = timeit.default_timer()
                                bubble_sort(aux100)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for best case in bubble sort with 100 elements is: ", total_time)
                            elif option==3:    #250 elements
                                aux250 = arr250
                                ascending(aux250)
                                default_time = timeit.default_timer()
                                bubble_sort(aux250)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for best case in bubble sort with 250 elements is: ", total_time)
                            elif option==4:    #500 elements
                                aux500 = arr500
                                ascending(aux500)
                                default_time = timeit.default_timer()
                                bubble_sort(aux500)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for best case in bubble sort with 500 elements is: ", total_time)
                            elif option==5:    #1000 elements
                                aux1000 = list(arr1000)
                                ascending(aux1000)
                                default_time = timeit.default_timer()
                                bubble_sort(aux1000)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for best case in bubble sort with 1000 elements is: ", total_time)
                            elif option == 6:
                                break
                            else:
                                print("bad command")


                    elif option ==2:  #heap sort
                        """The best case for heap sort would be if the elements in the array are all identical
                        such that there would be no need to bring any node down or bring the max valued nod up
                        For removing all nodes from the list would be necessar a n*O(1) number of moves
                         Time complexity O(n)"""
                        while True:
                            try:
                                option = int(lists_menu())
                            except:
                                print("invalid option")
                                pass
                            if option == 1:    #50 elements
                                aux50 = arr50
                                identical(aux50)
                                default_time = timeit.default_timer()
                                heapMain(aux50)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for best case in heap sort with 50 elements is: ", total_time)
                            elif option==2:    #100 elements
                                aux100 = arr100
                                identical(aux100)
                                default_time = timeit.default_timer()
                                heapMain(aux100)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for best case in heap sort with 100 elements is: ", total_time)
                            elif option==3:    #250 elements
                                aux250 = arr250
                                identical(aux250)
                                default_time = timeit.default_timer()
                                heapMain(aux250)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for best case in heap sort with 250 elements is: ", total_time)
                            elif option==4:    #500 elements
                                aux500 = arr500
                                identical(aux500)
                                default_time = timeit.default_timer()
                                heapMain(aux500)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for best case in heap sort with 500 elements is: ", total_time)
                            elif option==5:    #1000 elements
                                aux1000 = arr1000
                                identical(aux1000)
                                default_time = timeit.default_timer()
                                heapMain(aux1000)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for best case in heap sort with 1000 elements is: ", total_time)
                            elif option == 6:
                                break
                            else:
                                print("bad command")
                    elif option==3:
                        break
                    else:
                        print("bad command")
            else :
                print("choose option 1 first")


        elif option == 6:  # avrage case
            if ok==1:
                while True:
                    try:
                        option = int(cases_menu())
                    except:
                        print("invalid option")
                        pass

                    if option == 1:  # bubble sort
                        """The number of comparations is constantt in this type of sorting algorithm.
                                   as an example if the element on the position a should be on the position c in the 
                                   sorted array then the minimum number of swaps required will be (c-a). The maximum 
                                   number of swaps required will be n-1 if elements are on the edge and n/2 if they're 
                                   elements from the middle. Time complexity O(n^2)"""
                        while True:
                            try:
                                option = int(lists_menu())
                            except:
                                print("invalid option")
                                pass
                            if option == 1:  # 50 elements
                                 aux50 = arr50
                                 default_time = timeit.default_timer()
                                 bubble_sort(aux50)
                                 end_time = timeit.default_timer()
                                 total_time = end_time - default_time
                                 print("time elapsed for avrage case in bubble sort with 50 elements is: ", total_time)
                            elif option == 2:  # 100 elements
                                aux100 = arr100
                                default_time = timeit.default_timer()
                                bubble_sort(aux100)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for avrage case in bubble sort with 100 elements is: ", total_time)
                            elif option == 3:  # 250 elements
                                aux250 = arr250
                                default_time = timeit.default_timer()
                                bubble_sort(aux250)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for avrage case in bubble sort with 250 elements is: ", total_time)
                            elif option == 4:  # 500 elements
                                aux500 = arr500
                                default_time = timeit.default_timer()
                                bubble_sort(aux500)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for avrage case in bubble sort with 500 elements is: ", total_time)
                            elif option == 5:  # 1000 elements
                                aux1000 = arr1000
                                default_time = timeit.default_timer()
                                bubble_sort(aux1000)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for avrage case in bubble sort with 1000 elements is: ", total_time)
                            elif option == 6:
                                break
                            else:
                                print("bad command")
                    elif option == 2:  # heap sort
                        """We can create a heap in O(n)time and do insertions or removals in O(log(n)) time
                        Sience this function compares only 2 numbers at the time the total sum would look like this
                         log(n)/2+log(n-1)/2+log(n-2)/2+.....=log(n!)/2. The avrage runtime of heapify wold be O(n(log(n))).
                         Calling this function for every node in heapmain the runtime would be n*O(n(log(n)))"""
                        while True:
                            try:
                                option = int(lists_menu())
                            except:
                                print("invalid option")
                                pass
                            if option == 1:  # 50 elements
                                aux50 = arr50
                                default_time = timeit.default_timer()
                                heapMain(aux50)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for avrage case in heap sort with 50 elements is: ", total_time)
                            elif option == 2:  # 100 elements
                                aux100 = arr100
                                default_time = timeit.default_timer()
                                heapMain(aux100)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for avrage case in heap sort with 100 elements is: ", total_time)
                            elif option == 3:  # 250 elements
                                aux250 = arr250
                                default_time = timeit.default_timer()
                                heapMain(aux250)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for avrage case in heap sort with 250 elements is: ", total_time)
                            elif option == 4:  # 500 elements
                                aux500 = arr500
                                default_time = timeit.default_timer()
                                heapMain(aux500)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for avrage case in heap sort with 500 elements is: ", total_time)
                            elif option == 5:  # 1000 elements
                                aux1000 = arr1000
                                default_time = timeit.default_timer()
                                heapMain(aux1000)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for avrage case in heap sort with 1000 elements is: ", total_time)
                            elif option == 6:
                                break
                            else:
                                print("bad command")
                    elif option == 3:
                        break
                    else:
                        print("bad command")
            else :
                print("choose option 1 first")


        elif option == 7:  # worst case
            if ok==1:
                while True:
                    try:
                        option = int(cases_menu())
                    except:
                        print("invalid option")
                        pass

                    if option == 1: #bubble sort
                        """The worst case can be represented by an array where all the elements are arranged 
                        in a decreasing order. In a such case the number of swaps will be equal with the 
                         number of comparasions =n(n-1)/2. Time complexity=O(n^2)"""
                        while True:
                            try:
                                option = int(lists_menu())
                            except:
                                print("invalid option")
                                pass
                            if option == 1:  # 50 elements
                                aux50 = arr50
                                descending(aux50)
                                default_time = timeit.default_timer()
                                bubble_sort(aux50)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for worst case in bubble sort with 50 elements is: ", total_time)
                            elif option == 2:  # 100 elements
                                aux100 = arr100
                                descending(aux100)
                                default_time = timeit.default_timer()
                                bubble_sort(aux50)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for worst case in bubble sort with 100 elements is: ", total_time)
                            elif option == 3:  # 250 elements
                                aux250 = arr250
                                descending(aux250)
                                default_time = timeit.default_timer()
                                bubble_sort(aux250)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for worst case in bubble sort with 250 elements is: ", total_time)
                            elif option == 4:  # 500 elements
                                aux500 = arr500
                                descending(aux500)
                                default_time = timeit.default_timer()
                                bubble_sort(aux500)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for worst case in bubble sort with 500 elements is: ", total_time)
                            elif option == 5:  # 1000 elements
                                aux1000 = arr1000
                                descending(aux1000)
                                default_time = timeit.default_timer()
                                bubble_sort(aux1000)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for worst case in bubble sort with 1000 elements is: ", total_time)
                            elif option == 6:
                                break
                            else:
                                print("bad command")

                    if option == 2:  # heap sort
                        """The worst case in heap sort might happen when all the elements from the array are distinct,in that case heapify would be calld every time
                        an element is removed.The max height of the heap is log(n), the same as the number of swapsnneeded to remove every element
                        Doing it for each node, the total number of moves would be n*(log(n))
                        The runtime in the worst case is O(n(log(n)))"""
                        while True:
                            try:
                                option = int(lists_menu())
                            except:
                                print("invalid option")
                                pass
                            if option == 1:  # 50 elements
                                aux50 = arr50
                                different(aux50)
                                default_time = timeit.default_timer()
                                heapMain(aux50)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for worst case in heap sort with 50 elements is: ", total_time)
                            elif option == 2:  # 100 elements
                                aux100 = arr100
                                different(aux100)
                                default_time = timeit.default_timer()
                                heapMain(aux100)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for worst case in heap sort with 100 elements is: ", total_time)
                            elif option == 3:  # 250 elements
                                aux250 = arr250
                                different(aux250)
                                default_time = timeit.default_timer()
                                heapMain(aux250)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for worst case in heap sort with 250 elements is: ", total_time)
                            elif option == 4:  # 500 elements
                                aux500 = arr500
                                different(aux500)
                                default_time = timeit.default_timer()
                                heapMain(aux500)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for worst case in heap sort with 500 elements is: ", total_time)
                            elif option == 5:  # 1000 elements
                                aux1000 = arr1000
                                different(aux1000)
                                default_time = timeit.default_timer()
                                heapMain(aux1000)
                                end_time = timeit.default_timer()
                                total_time = end_time - default_time
                                print("time elapsed for worst case in heap sort with 1000 elements is: ", total_time)
                            elif option == 6:
                                break
                            else:
                                print("bad command")
                    elif option == 3 :
                        break
                    else:
                        print("bad command")
            else :
                print("choose option 1 first")

        else:
            print("bad command!")

start()
