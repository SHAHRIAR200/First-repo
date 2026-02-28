import numpy as np

def convert(list) :
    # array = np.array([list1, list2, list3])
    # print(array)
    # transpose = np.transpose(array)
    # print(transpose)
    # print(transpose.flatten())
    matrix = np.array(list)
    transpose_matrix = matrix.transpose(  )
    print(transpose_matrix.flatten())
def main() :
    a, b = map(int, input().split())
    list = []
    for _ in range(a) :
        list.append(list(map(int, input().split())))

    convert(list)

main()