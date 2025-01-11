def perform_operation(num1, num2, operation):
  if  operation == "add":
    return num1 + num2
  elif operation == "substract":
    return num1 - num2
  elif operation == "multiply":
    return num1 * num2
  elif operation == "divide":
    if num2 == 0:
        return "Error. Division with zero not allowed"
    return num1 / num2
  else:
     return "Invalid operation"
     
if __name__ == "__main__":
    print(perform_operation(5, 0, "add"))

    