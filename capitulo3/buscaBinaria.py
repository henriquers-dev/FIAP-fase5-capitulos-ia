def binary_search(numbers: list[int], k: int) -> int:
    left, right = 0, len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == k:
            return mid
        elif numbers[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    return -1
