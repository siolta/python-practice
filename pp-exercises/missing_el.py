import random
import timeit

# ordrd_lst = [i for i in range(1, random.randint(5, 10))]
# ordrd_lst.pop(random.choice(ordrd_lst))

# l_list = [1, 3, 4, 5, 6, 7, 8, 9, 10]
# m_list = [1, 2, 3, 4, 6, 7, 8, 9, 10]
# r_list = [1, 2, 3, 4, 5, 6, 7, 9, 10]

# print(f"List is: {ordrd_lst}")


class missingEl(object):

    def __init__(self):
        self.self = self

    def oOfNGetMissingNo(self, A):
        '''
        Find the missing element in array A using iteration, O(n) complexity
        '''
        el_index = 0

        for item in A:
            if el_index == item - 1:
                el_index += 1
            else:
                return item - 1

    def getMissingNo(self, A):
        '''
        Find the missing element in array A using sum, O(n) complexity
        '''
        array_len = len(A)
        total = (array_len + 1) * (array_len + 2) // 2
        sum_of_A = sum(A)
        return total - sum_of_A

    def getMissingNum(self, A):
        '''
        Find the missing element in array A using binary search, O(log n) complexity
        '''
        left = 0
        right = len(A) - 1
        middle = (left + right) // 2

        while right > left + 1:
            if (A[left] - left) != (A[middle] - middle):
                right = middle
            elif (A[right] - right) != (A[middle] - middle):
                left = middle

            middle = (left + right) // 2
        return A[middle] + 1

# finder = missingEl()

# l_Result = finder.getMissingNum(l_list)
# m_Result = finder.getMissingNum(m_list)
# r_Result = finder.getMissingNum(r_list)
# ordrd_Result = finder.getMissingNum(ordrd_lst)
# ordrd_M_Result = finder.getMissingNo(ordrd_lst)
# oOfNResult = finder.oOfNGetMissingNo(ordrd_lst)


# print(f"l_list result: {l_Result}")
# print(f"m_list result: {m_Result}")
# print(f"r_list result: {r_Result}")
# print(f"ordrd_list log N result: {ordrd_Result}")
# print(f"ordrd_list math result: {ordrd_M_Result}")
# print(f"ordrd_list oOfN result: {oOfNResult}")


def binary_time():
    SETUP_CODE = '''
from missing_el import missingEl
import random
ordrd_lst = [i for i in range(1, 100000)]
ordrd_lst.pop(75000)
finder = missingEl()
    '''

    TEST_CODE = '''
finder.getMissingNum(ordrd_lst)
    '''

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)

    # priniting minimum exec. time
    print('Binary search time: {}'.format(min(times)))


def linear_time_oN():
    SETUP_CODE = '''
from missing_el import missingEl
import random
ordrd_lst = [i for i in range(1, 100000)]
ordrd_lst.pop(75000)
finder = missingEl()'''

    TEST_CODE = '''
finder.oOfNGetMissingNo(ordrd_lst)
    '''
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)

    # priniting minimum exec. time
    print('Linear search time oN: {}'.format(min(times)))


def linear_time_math():
    SETUP_CODE = '''
from missing_el import missingEl
import random
ordrd_lst = [i for i in range(1, 100000)]
ordrd_lst.pop(75000)
finder = missingEl()'''

    TEST_CODE = '''
finder.getMissingNo(ordrd_lst)
    '''
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)

    # priniting minimum exec. time
    print('Linear search time math: {}'.format(min(times)))


# the concept behind this solution is that the elements appearing before the missing element
# will have ar[i] – i = 1 and those appearing after the missing element will have ar[i] – i = 2.

if __name__ == "__main__":
    binary_time()
    linear_time_oN()
    linear_time_math()
