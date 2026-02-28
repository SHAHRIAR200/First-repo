def conversion(old_list):
    new_list = list(map(int, old_list))
    print(new_list)
    return new_list

def main():
    items = input().split()
    conversion(items)

def build_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row_items = input().split()
        row = list(map(int, row_items))
        if len(row) != cols:
            raise ValueError(f"Row {i+1} must have {cols} values")
        matrix.append(row)
    return matrix

def matrix_main():
    r, c = map(int, input("Enter rows and cols: ").split())
    print(f"Enter {r} rows, each with {c} numbers:")
    mat = build_matrix(r, c)
    print("Matrix:")
    for row in mat:
        print(row)

if __name__ == "__main__":
    mode = input("Type 'm' for matrix or 'c' for convert: ").strip().lower()
    if mode == 'm':
        matrix_main()
    else:
        main()