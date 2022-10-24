class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
               # print("FizzBuzz")
                output.append("FizzBuzz")
            elif i % 3 == 0:
               # print("Fizz")
                output.append("Fizz")
            elif i % 5 == 0:
               # print("Buzz")
                output.append("Buzz")
            else :
                output.append(str(i))
               # print(i)
        return output
        