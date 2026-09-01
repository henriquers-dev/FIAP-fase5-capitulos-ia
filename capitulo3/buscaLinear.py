def linear_search(numbers: list[int], k: int) -> int:
    for idx, num in enumerate(numbers):
        if num == k:
            return idx
    return -1

print(linear_search([1, 4, 2, 5, 3, 4, 8], 3))  # Saída: 4
