# Concept : Strings

# Manipulate string

'''
Given a string S and a character C (as string of length 1), return a string with the characters surrounding any occurrence of C reversed.
For example, if S is "Hello beautiful world" and C is a space, return "Hellb oeautifuw lorld".
Skip any positions where C occurs twice in a row.
'''
import unittest


def manipulate_string(S, C):
  ansst = ""
  length = len(S)
  previous = 0
  temp_s = list(S)
  while (S.find(C, previous) != -1):
    index = S.find(C, previous)
    temp_s[index-1], temp_s[index+1] = temp_s[index+1], temp_s[index-1]
    previous = index+1
  for r in temp_s:
    ansst += r
  return ansst


class Dict_to_list(unittest.TestCase):
  def test_01(self):
    self.assertEqual(manipulate_string(
        'Hello beautiful world', ' '), 'Hellb oeautifuw lorld')

  def test_02(self):
    self.assertEqual(manipulate_string('Hello-World', '-'), 'HellW-oorld')

  def test_03(self):
    self.assertEqual(manipulate_string('Gf oish!', ' '), 'Go fish!')


if __name__ == '__main__':
  unittest.main(verbosity=2)
