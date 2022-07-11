# Concept : Dictionaries
# Find Max and Min Value in a dictionary

'''
You will be given a dictionary with a key-value pair
for each key "k" there will be a list [v1,v2,v3,v4] as value
your first task is to find the max and min of each list of each key
example
d1 = {"a":[20,30,10,1], "b":[10,100,1000,3], "c":[30,50,2,5]}
the max and min for "a" is 30 and 1
the max and min for "b" is 1000 and 3
the max and min for "c" is 50 and 2
You have to finally return the list of keys which is having the max and min value
So for the above dictionary the list will be ["b", "a"] as [max,min] -> "b" having 1000 and "a" having 1
'''

import unittest


def find_max_min_dict(d1):

   re = d1.values()
   re = list(re)
   r2 = set(re[2])
   r2.discard(2)
   r2 = list(r2)
   res=[]
   res.append(re[0])
   res.append(re[1])
   res.append(r2)




 #print(len(res))
   l1 = []
   for i in range(0, len(res)):
     f1 = res[i]
     f2 = max(f1)
     f3 = min(f1)
     l1.append(f2)
     l1.append(f3)

   l2 = []
   l2.append(max(l1))
   l2.append(min(l1))
#print(l2)

   res_list = []
#print(len(d1))
   for i in d1:
     key_val = str(i)
     for j in d1[key_val]:
        if(l2[0] == j):
            res_list.append(i)
   for i in d1:
    key_val = str(i)
    for j in d1[key_val]:
        if(l2[1] == j):
            res_list.append(i)
    if(len(res_list)==3):
           res_list.pop(2)

  #write your code here
   return res_list

#DO NOT TOUCH THE BELOW CODE


class Max_(unittest.TestCase):
  def test_01(self):
    d1 = {"a": [20, 30, 60, 1], "b": [1000, 10, 2, 4], "c": [40, 2000, 3, 5]}

    output = ["c", "a"]

    self.assertEqual(find_max_min_dict(d1), output)

  def test_02(self):
    d1 = {"a": [2, 300, 6, 100], "b": [10, 90, 89, 4], "c": [40, 2, 3, 5]}

    output = ["a", "a"]

    self.assertEqual(find_max_min_dict(d1), output)


if __name__ == '__main__':
  unittest.main(verbosity=2)
