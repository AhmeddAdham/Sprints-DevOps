import sprints 
import unittest

class TestmyFunc(unittest.TestCase):
    #    def test1(self):
    #         data = [1,2,3,4,1.2,1.3]
    #         expected = (3, 1.3)
    #         actual = sprints.myFunc(data)
    #         self.assertEqual(actual, expected)     

    #     def test2(self):
    #         data=[1.1,5.2]
    #         expected=(0,5.2)
    #         actual=sprints
       
    def test1(self):

        data = [1,2,3,4,1.2,5.2]
        expected = (3, 5.2)
        actual = sprints.myFunc(data)
        self.assertEqual(actual, expected)


    def test2(self):

        data = [2,6,4.3,5.7]
        expected = (4,5.7)
        actual = sprints.myFunc(data)
        self.assertEqual(actual, expected)


    def test3(self):

        data = [2,4,6,8,3.7,5.2]
        expected = (5,5.2)
        actual = sprints.myFunc(data)
        self.assertEqual(actual, expected)








if __name__ == '__main__':
    unittest.main()