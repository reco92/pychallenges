

def combinations(start, sources):
    for i in sources:
        new = start
        new.append(i)
        print (new)
        new_sources = sources()
        return combinations(new, new_sources) 

def get_posibilities():
    print(1)

# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

def problem1(lista, k):
    for index in range(len(lista)):
        if index == (len(lista)-1):
            return False
        index2 = index + 1
        while index2 < len(lista):
            if (lista[index] + lista[index2]) == k:
                return True
            index2 += 1
    
    return False

# def problem1b(lista, k):

#     for item in lista:
#         if item < k:
def solution(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            print (i)
            sum += i
    return sum
  
def song_decoder(song):
    song = song.replace('WUB', ' ')
    song = song.strip()
    lsong = list(song)
    index = 0
    if len(song) <= 2:
        return song
        
    while index < len(lsong) - 2:
        if (lsong[index] == ' ' or  lsong[index] == '')  and  lsong[index+1] == ' ':
             lsong[index+1] = ''
        index += 1
        
    return "".join(lsong)

# Test.assert_equals(song_decoder("AWUBBWUBC"), "A B C","WUB should be replaced by 1 space")
# Test.assert_equals(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C","multiples WUB should be replaced by only 1 space")
# Test.assert_equals(song_decoder("WUBAWUBBWUBCWUB"), "A B C","heading or trailing spaces should be removed")

def song_decoder2(song):
    return " ".join(song.replace('WUB', ' ').split())


# Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

# Integers can appear more than once in the list. You may assume all numbers in the list are positive.

# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

def sublist_sums_value(arr, val):
    sublist = [ item for item in arr  if item <= val]
    if len(sublist):
        sublist.sort()
        sublist.reverse()
        for idx, item in enumerate(sublist):
            combinations = [[item]]
            idx_eval = idx + 1
            while idx_eval < len(sublist):
                news = list()
                for comb in combinations:
                    total = sum(comb)
                    if (total + sublist[idx_eval]) == val:
                        comb.append(sublist[idx_eval]) 
                        return comb
                    elif (total + sublist[idx_eval]) < val:
                        lcopy = comb.copy()
                        lcopy.append( sublist[idx_eval])
                        news.append(lcopy)
                combinations += news
                idx_eval += 1
    return None

# Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.

def flights_origin_destination(arr, start):
    flights = dict()
    itinerary = list()
    for item in arr:
        if item[0] in flights:
            flights[item[0]].append(item[1])
        else:
            flights[item[0]] = [item[1]]
    for key, value in flights.items():
        value.sort()
        # flights[key] = value
        #ist not necesary because value is a pointer to the original value the change made there affects the original

    while start:
        itinerary.append(start)
        dests = flights.get(start, [])
        if dests:
            start = dests.pop(0)
        else:
            start = None

    if len(itinerary) == (len(arr)+1):
        return itinerary
    
    return None

# Implement a stack that has the following methods:

# push(val), which pushes an element onto the stack
# pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
# max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

class NodeStack:

    def __init__(self, value=None):
        self.value = value
        self.next_node = None

class Stack:
    
    def __init__(self):
        self.root = None
        self.length = 0

    def push(self, value):
        self.length += 1
        if self.root:
            new_root = NodeStack(value)
            new_root.next_node = self.root
            self.root = new_root
        else:
            self.root = NodeStack(value)

    def pop(self):
        if self.root:
            self.length -= 1
            value = self.root.value
            self.root = self.root.next_node
            return value
        else:
            return None

    def max(self):
        if self.root:
            value = self.root.value
            root = self.root
            while root:
                if root.value > value:
                    value = root.value
                root = root.next_node
        else:
            return None
        
        return value
        
    def print(self):
        if self.root:
            root = self.root
            while root:
                print (root.value)
                root = root.next_node

# merge sort

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    middle = int(len(arr)/2)
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[ middle:])
    c = list()

    pl = 0
    pr = 0

    while pl < len(left) and pr < len(right):
        if left[pl] > right[pr]:
            c.append(right[pr])
            pr+=1
        else:
            c.append(left[pl])
            pl+=1
        
    c = c + left[pl:]
    c = c + right[pr:]

    return c


def max_profit(arr):
    max_profit = 0
    buy = 0
    sell = 0

    for idx, val in enumerate(arr):
        next_val = idx+1
        while next_val < len(arr):
            if arr[next_val] - val > max_profit:
                buy = val
                sell = arr[next_val]
                max_profit = arr[next_val] - val
            next_val+=1
    return max_profit
            



def main():
    # lista = [10, 15, 3, 7]
    # print ( problem1(lista, 20))
    # print (solution(10))
    # print (set('abcdeaaaa'))
    # tmp = 'aabbccaaddeeaa'
    # print (tmp.find('99'))
    # print (tmp.replace('aa', '-'))
    # print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
    # print(sublist_sums_value([12, 1, 61, 5, 9, 2], 24))
    # print(flights_origin_destination( [('A', 'C'), ('A', 'B'), ('B', 'C'), ('C', 'A')], 'A'))

    # ss = Stack()
    # ss.push(1)
    # ss.push(2)
    # ss.push(3)
    # ss.print()
    # print(ss.max())

    # print(merge_sort([2, 4, 1, 3 ,5]) )
    print(max_profit([9, 11, 8, 5, 7, 10]))


if __name__ == "__main__":
    main()
