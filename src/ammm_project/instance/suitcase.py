import random

# Function to generate an empty suitcase of given length and width
def generate_suitcase(length, width):
    suitcase = [[0] * width for _ in range(length)]
    return suitcase

def fill_suitcase(suitcase, product_sizes):
    length = len(suitcase)
    width = len(suitcase[0])
    squares = []
    
    # Sort product sizes in descending order
    product_sizes.sort(reverse=True)
    
    for size in product_sizes:
        for i in range(length):
            for j in range(width):
                if i + size <= length and j + size <= width:
                    if all(suitcase[x][y] == 0 for x in range(i, i + size) for y in range(j, j + size)):
                        square_id = chr(len(squares) + 65)
                        for x in range(i, i + size):
                            for y in range(j, j + size):
                                suitcase[x][y] = square_id
                        squares.append((square_id, size))
                        break
            else:
                continue
            break
    
    num_squares = len(squares)
    total_area = length * width
    square_sizes = [size for _, size in squares]
    square_ids = [id for id, _ in squares]

    return {
        "x": length,
        "y": width,
        "n": num_squares,
        "tot_area": total_area,
        "dxdy": square_sizes,
        "id": square_ids,
    }
