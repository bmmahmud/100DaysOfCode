### Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        print(scores)
        student_marks[name] = scores
        
    query_name = input()
    values = student_marks[query_name]
    lenght = len(values)
    sums = 0
    for i in values:
        val = i
        sums += val 
    result = sums/lenght
    format_float = "{:.2f}".format(result)
    print(format_float)       