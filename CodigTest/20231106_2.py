def solution(numbers):
    sorted_list = sorted(numbers, reverse=True)
    first = max(sorted_list)
    second = sorted_list[1]
    answer = first*second
    
    return answer
