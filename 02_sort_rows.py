# concept : 2d Lists
'''
Sort-Rows
  ** Sorting each row of 2d List **
  _ As you might have done sorting in a single array, Why can't we do the same for 2d list _
  ## Representation
  2 3 1
  5 3 4
  6 9 7
  ### After sorting each row
  1 2 3
  3 4 5
  6 7 9
  ## Input
  3
  1
  2
  3
  5
  4
  7
  9
  6
  ## Output
  1 2 3
  3 4 5
  6 7 9
  '''

import unittest


def sort_rows(lst):
  sorted_list = []
  for row in lst:
    current_row = row.copy()
    current_row.sort()
    sorted_list.append(current_row)

  return sorted_list


class Dict_to_list(unittest.TestCase):
  def test_01(self):
    input = [[10, 3, 2], [5, 6, 7]]
    output = [[2, 3, 10], [5, 6, 7]]

    self.assertEqual(sort_rows(input), output)

  def test_02(self):
    input = [[20, 30, 4], [15, 60, 87], [12, 3, 4], [78, 62, 41]]
    output = [[4, 20, 30], [15, 60, 87], [3, 4, 12], [41, 62, 78]]

    self.assertEqual(sort_rows(input), output)

  def test_03(self):
    input = [[3, 30, 3, 10], [5, 5, 4, 5], [1, 1, 3, 3, 1]]
    output = [[3, 3, 10, 30], [4, 5, 5, 5], [1, 1, 1, 3, 3]]

    self.assertEqual(sort_rows(input), output)


if __name__ == '__main__':
  unittest.main(verbosity=2)
