# def lesser_of_two_evens(a,b):
#     result = 0
#     if a%2 == 0 and b%2 == 0:
#         if a > b:
#             result ="Both are even and lesser is "+ str(b)
#         else:
#             result = "Both are even and lesser is "+ str(a) 
#     elif a%2 != 0 and b%2 != 0:   
#         if a > b:
#             result ="Both are odd and greater is "+ str(a) 
#         else:
#             result = "Both are odd and greater is "+ str(b)
#     return result
# fall = lesser_of_two_evens(5,7)
# print(fall)                            

### Hacker Rank
# if __name__ == '__main__':
#     n = int(input('number of entery:'))
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         print(scores)
#         student_marks[name] = scores
#     print(student_marks)    
#     query_name = input("name: ")
#     print(student_marks[query_name])
#     values = student_marks[query_name]
#     lenght = len(values)
#     print("length:"+ str(lenght))
#     # print("values: "+ str(values))
#     sums = 0
#     for i in values:
#         val = i
#         sums += val 
#         print(sums)
#     # print("Sum: "+str(sums)) 
#     result = sums/lenght
#     format_float = "{:.2f}".format(result)
#     print("Average: "+str(format_float))       

