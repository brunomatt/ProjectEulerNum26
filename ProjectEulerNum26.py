# A unit fraction contains 1 in the numerator.
# The decimal representation of the unit fractions with denominators 2 to 10 are given:
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
import time
import math
start = time.time()

cycle_length = []
answers = []

def long_division(num,denom): #numerator is dividend and denominator is divisor num = 1 denom = 7
    digits = []
    remainder = num
    power = len(str(denom))
    while remainder > 0 and len(digits) < 2020: # PLAY WITH THIS ONCE ANSWER IS KNOWN
        if (remainder * 10) % denom == (remainder * 10): #checks for a zero placeholder
            digits.append(0)
            if (remainder * 100) % denom == (remainder * 100):
                digits.append(0)
        digit = (remainder * pow(10,power))//denom
        new_remainder = (remainder * pow(10,power)) % denom
        for i in str(digit):
            digits.append(int(i))
        remainder = new_remainder
    return digits, denom

def cycle_check(int_list,denom):
    for k in range(10,1000):
        if int_list[0:k] == int_list[k:2*k]:
            cycle_length.append(k)
            answers.append(denom)
            break

for j in range(2,1001):
    cycle_check(long_division(1,j)[0] , long_division(1,j)[1])

answer = answers[cycle_length.index(max(cycle_length))]
print(answer)

stop = time.time()
print('Time: ', math.ceil(stop-start), 'seconds')