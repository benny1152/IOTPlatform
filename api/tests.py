from pymongo import MongoClient
from test.model_user import UserTests
from test.model_house import HouseTests
from test.model_room import RoomTests
import unittest

mongo = MongoClient('localhost', 27017)
db = mongo.database

def main():
    #suite = unittest.TestSuite()
    #suite.addTest(UserTests(db.users_tests))
    #suite = unittest.defaultTestLoader.loadTestsFromTestCase(UserTests(db.users_test))
    #unittest.TextTestRunner().run(suite)
    UserTests.collection = db.user_test
    HouseTests.collection = db.house_test
    RoomTests.collection = db.room_test
    unittest.main()

if __name__ == "__main__":
    main()