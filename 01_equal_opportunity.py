# concept : 2d list

# Equal-Opportunity-1

'''
  ** Equal Opportunity in each row of a list **
  _ Imagine for example in a class you have arranged a seating order in which both girls and boys are sitting together. Your task is to now check each row to find which row has equal number of girls and boys. Girls are represented by 0 and Boys are represented by 1 _
  ## Steps
  1. Write a code for accepting the input of 4 rows and 6 columns
  2. Go to each row and count the number of 0's and 1's
  3. If the 1's count and 0's count is equal then print the row there itself.
  ## Representation
1 1 0 0 1 0
0 1 1 1 1 1
0 0 1 1 0 0
0 0 0 1 1 1
### After finding the row number
0
3
## Input
[[1,1,0,0,1,0],[0,1,1,1,1,1],[0,0,1,1,0,0],[0,0,0,1,1,1]]
## Output
[0, 3]
NOTE : DO NOT USE count() method
'''

import unittest


def equal_opportunity(lst):
  equals = []
  for i in range(len(lst)):
    count_boy = 0
    count_girl = 0
    for j in range(len(lst[i])):
        if lst[i][j] == 0:
            count_boy += 1
        else:
            count_girl += 1
    if count_boy == count_girl:
        equals.append(i)
  return equals


class Dict_to_list(unittest.TestCase):
  def test_01(self):
    input = [[1, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1],
             [0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1]]
    output = [0, 3]

    self.assertEqual(equal_opportunity(input), output)

  def test_02(self):
    input = [[1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 1],
             [0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1]]
    output = [3]

    self.assertEqual(equal_opportunity(input), output)

  def test_03(self):
    input = [[1, 1], [0, 1], [0, 0], [1, 1]]
    output = [1]

    self.assertEqual(equal_opportunity(input), output)


if __name__ == '__main__':
  unittest.main(verbosity=2)
