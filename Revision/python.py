'''

#1
def solveMefirst(a,b):
  return a + b;

num1 =  int(input())
num2 = int(input())
res = solveMefirst(num1,num2)
print(res)

#2
def simpleArraySum(arr):
  return sum(arr)


myArray = [1,2,3,4,5];
print(simpleArraySum(myArray));

#3
def campareTriplets(a,b):
  alice = 0
  bob = 0

  for i in range(3):
    if a[i] > b[i]:
      alice+=1
    elif a[i] < b[i]:
      bob+=1
  return alice, bob;    
  
array1 = 5, 6, 7
array2 = 3, 6, 10

print(campareTriplets(array1, array2));

#4
def aVeryBigSum(ar):
  return sum(ar)

a1 = 100000002
a2 = 100000003
a3 = a2, a1
result = aVeryBigSum(a3);
print(result);


#5

def diagonalDifferce(arr):
  leftdiag = rightdiag = 0
  for i in range(n):
    leftdiag = leftdiag + arr[i][i]
    rightdiag = rightdiag + arr[i][n - 1 - i]
  return abs(leftdiag - rightdiag);


n = int(input().strip())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().rstrip().split())))

print(diagonalDifferce(arr));

#6

def hashPattern(n):
  for i in range(1, n + 1):
    s = "#" * i; 
    print(s.rjust(n))
  

n = int(input())
result = hashPattern(n);
print(result)


# 7

def miniMaxSum(arr):
  s = 0
  minnum = 999999999999
  maxnum = 0

  n = len(arr)
  for i in range(n):
    s = s + arr[i]
    minnum = min(minnum, arr[i])
    maxnum = max(maxnum, arr[i])
  print(s-maxnum, s-minnum);

arr = [1,3,5,7,9];
print(miniMaxSum(arr))



#8

def birthdayCakeCandles(arr):
  
  n = len(arr)
  maxnum = 0
  count = 0
  for i in range(n):
    if(arr[i] > maxnum):
      maxnum = arr[i]
      count = 1
    elif arr[i] == maxnum:
      count+=1
  return count
  # return arr.count(max(arr)) #another method

print(birthdayCakeCandles([4,4,1,3]));

#9

def timeComversion(time):
  meridian = time[-2:]
  if meridian == 'AM' and time[:2] == '12':
    time = '00' + time[2:]
  if meridian == 'PM' and time[:2]!= '12' :
    time = str(12 + int(time[:2])) + time[2:]
  return time

result = '07:05:45PM'
print(timeComversion(result));



def fibonacci_recursive(n):
    if n <= 0:
        return "Please enter a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage
n = 10
print(f"The {n}th Fibonacci number is: {fibonacci_recursive(n)}")
'''



def febonacci(n):
  a = 0
  b = 1

  for i in range(i <= n):
    c = a[i] + b[i]
    a[i] = b[i]
    b[i] = c[i]

  return c

print(febonacci(9))
  
'''
'''