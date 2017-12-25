import unittest
import pprint
from datasource.TUserHandler import TUserHandler

class TestStringMethods(unittest.TestCase):
    def test_user_handler(self):
        handler = TUserHandler()
        seq = handler.getNextSequence("userid")
        self.assertTrue(seq >= 0)

        # postId = handler.insertUser('peek3', "tony.stark")
        # self.assertEqual(postId, -1)

    def test_selectAll(self):
        handler = TUserHandler()
        result = handler.selectAll()

        self.assertTrue(result.count() > 0)
        for row in result :
            print row


    def test_selectByCID(self):
        handler = TUserHandler()
        result = handler.selectByCID("peek2")
        pprint.pprint(result)

if __name__ == '__main__':
    unittest.main()