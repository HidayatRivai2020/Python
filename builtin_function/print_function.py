print("=== print() Functions Examples ===")

# One Parameter
print("Hello")

# Multiple Parameters
print("Hello", "how are you?")

# Plus Separator
print("Hello", "with plus separator?", sep="+")

# End string
print("Hello", "show this : -->", end=" a new text \n")

# Print file
Newfile= open("./builtin_function/output/exam_score.txt", "w")

exam_name = "Degree"
exam_date = "2-Nov"
exam_score = 323

print(exam_name, exam_date, exam_score, file=Newfile , sep = ",")

Newfile.close()

# Print flush
print("Hello, World!", flush=True)