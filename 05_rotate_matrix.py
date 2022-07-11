#  Concept : 2d Lists

'''
Suppose that you are given an image, which is not in a stright view then you have to rotate it to 90 degrees to a convenient side.
Considering that an image is a collection of pixels which looks like a 2d array or 2d list or Matrix, we apply this technique towards the Matrix with our own logic and rotate a Matrix.
If you know how to rotate a Matrix you can also write or use the same logic to rotate an image
 Example take the matrix below which you have to rotate left side 90 degree,
  ## Representation
  10 20 30
  40 50 60
  70 80 90
  ### After Rotation
  30 60 90
  20 50 80
  10 40 70
  ## Input
  3
  3
  10
  20
  30
  40
  50
  60
  70
  80
  90
  ## Output
  30 60 90
  20 50 80
  10 40 70
'''

import unittest


def rotate_matrix(lst, side):
  rotated_list = []
  len_i = len(lst)
  len_j = len(lst[0])
  if(side == "right"):
    for i in range(len_j):
      current_row = []
      for j in range(len_i-1, -1, -1):
        current_row.append(lst[j][i])
      rotated_list.append(current_row)

  else:
    for i in range(len_j-1, -1, -1):
      current_row = []
      for j in range(len_i):
        current_row.append(lst[j][i])
      rotated_list.append(current_row)
  return rotated_list


class Dict_to_list(unittest.TestCase):
  def test_01(self):
    input = [[2, 3, 4], [5, 6, 7]]
    output = [[5, 2], [6, 3], [7, 4]]

    self.assertEqual(rotate_matrix(input, "right"), output)

  def test_02(self):
    input = [[20, 30, 4], [15, 60, 87], [12, 3, 4], [41, 62, 78]]
    output = [[4, 87, 4, 78], [30, 60, 3, 62], [20, 15, 12, 41]]

    self.assertEqual(rotate_matrix(input, "left"), output)

  def test_03(self):
    input = [[20, 30, 4], [15, 60, 87], [12, 3, 4], [41, 62, 78]]
    output = [[41, 12, 15, 20], [62, 3, 60, 30], [78, 4, 87, 4]]

    self.assertEqual(rotate_matrix(input, "right"), output)


if __name__ == '__main__':
  unittest.main(verbosity=2)
