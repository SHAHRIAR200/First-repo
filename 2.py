import numpy as np

def line_to_matrix(n) :
    array = np.array(n)
    print(np.reshape(array, (3,3)))
def main() :
    n = input().split()
    new_list = list(map(int, n))
    line_to_matrix(new_list)

main()