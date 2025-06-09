import requests
import json
import unittest

class routesTest(unittest.TestCase):

    # ROOT/INDEX
    def test_getRoot(self):
        url = "http://localhost:8080/"
        response = requests.get(url)

        print("Response status code:", response.status_code)
        print("Response Body:", response.json())
        self.assertEqual(response.status_code, 200)

    # AGE ROUTE
    def test_route_getAgeRoute(self):
        url = "http://localhost:8080/age_query?age=22"
        response = requests.get(url)

        print("Response status code:", response.status_code)
        print("Response Body:", response.json())
        self.assertEqual(response.status_code, 200)
    
    # AGE ROUTE - NEGATIVE
    def test_route_getAgeRoute_negative(self):
        url = "http://localhost:8080/age_query?age=Lucas"
        response = requests.get(url)

        print("Response status code:", response.status_code)
        print("Response Body:", response.json())
        self.assertEqual(response.status_code, 422)

    # SAVE STRING
    def test_route_getSaveString(self):
        url = "http://localhost:8080/save_string/HelloWorld"
        response = requests.get(url)

        print("Response status code:", response.status_code)
        print("Response Body:", response.json())
        self.assertEqual(response.status_code, 200)

    # DISPLAY STRING
    def test_route_getDisplayStrings(self):   
        url = "http://localhost:8080/display_strings"
        response = requests.get(url)

        print("Response status code:", response.status_code)
        print("Response Body:", response.json())
        self.assertEqual(response.status_code, 200)

    # CURRENT TIME
    def test_route_getCurrentTime(self):
        url = "http://localhost:8080/time"
        response = requests.get(url)

        print("Response status code:", response.status_code)
        print("Response Body:", response.json())
        self.assertEqual(response.status_code, 200)

    # LOCATION INFO
    def test_route_getLocationInfo(self):
        url = "http://localhost:8080/your_location/69.43.66.33/"
        response = requests.get(url)

        print("Response status code:", response.status_code)
        print("Response Body:", response.json())
        self.assertEqual(response.status_code, 200)
    
    # ADDITION
    def test_route_getAddition(self):
        url = "http://localhost:8080/plus/5/10"
        response = requests.get(url)

        print("Response status code:", response.status_code)
        print("Response Body:", response.json())

        self.assertEqual(response.status_code, 200)
    
    # ADDITION - FUNCTIONALITY
    def test_route_functionality_getAddition(self):
        url = "http://localhost:8080/plus/5/10"
        response = requests.get(url)

        print("Response status code:", response.status_code)
        print("Response Body:", response.json())
        self.assertEqual(response.json(), {"Result": 15})

    # ADDITION - NEGATIVE
    def test_route_getAddition_negative(self):
        url = "http://localhost:8080/plus/5/Lucas"
        response = requests.get(url)

        print("Response status code:", response.status_code)
        print("Response Body:", response.json())
        self.assertEqual(response.status_code, 422)

    # SUBTRACTION
    def test_route_getSubtraction(self):
        url = "http://localhost:8080/minus/10/5"
        response = requests.get(url)

        print("Response status code:", response.status_code)
        print("Response Body:", response.json())
        self.assertEqual(response.status_code, 200)

    # RANDOM WORD
    def test_route_getRandomWord(self):
        url = "http://localhost:8080/random_word"
        response = requests.get(url)

        print("Response status code:", response.status_code)
        print("Response Body:", response.json())
        self.assertEqual(response.status_code, 200)

    # CRASH THE APP - Requires manual testing

    # HEADERS DEMO
    def test_route_getHeadersDemo(self):
        url = "http://localhost:8080/hello_headers"
        response = requests.get(url)

        print("Response status code:", response.status_code)
        print("Response Body:", response.json())
        self.assertEqual(response.status_code, 200)

    # COOKIE DEMO
    def test_route_getCookieDemo(self):
        url = "http://localhost:8080/read_cookie"
        response = requests.get(url)

        print("Response status code:", response.status_code)
        print("Response Body:", response.json())
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()