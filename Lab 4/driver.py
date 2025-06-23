import requests
import json

session = requests.Session()

class cli:

    def start(self):

        running = True
        while running:
            self.interface()

    def interface(self):
        print("\nRoutes:")
        print("1. Display route information")
        print("2. Get age")
        print("3. Save a string")
        print("4. Display saved strings")
        print("5. Get current time")
        print("6. Get location info by IP")
        print("7. Add two numbers")
        print("8. Subtract two numbers")
        print("9. Generate a random word")
        print("10. Crash the app server")
        print("11. Headers demo")
        print("12. Session cookie")
        print("13. Exit")

        user_input = input("Select a route (#): ")

        match user_input:
            case '1':
                self.router("/")
            case '2':
                age = input("Enter your age: ")
                self.router(f"/age_query?age={age}")
            case '3':
                string = input("Enter a string to save: ")
                self.router(f"/save_string/{string}")
            case '4':
                self.router("/display_strings")
            case '5':
                self.router("/time")
            case '6':
                ip_address = input("Enter an IP address: ")
                self.router(f"/your_location/{ip_address}")
            case '7':
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                self.router(f"/plus/{a}/{b}")
            case '8':
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                self.router(f"/minus/{a}/{b}")
            case '9':
                self.router("/random_word")
            case '10':
                self.router("/byebye")
            case '11':
                theName = input("Enter your name: ")
                headers = {
                    "content-type": "application/json",
                    "X-Custom-Header": "CustomValue",
                    "name": theName
                    }
                url = "http://localhost:8080/headers"
                response = requests.get(url=url, headers=headers)
                print("\n ")
                print(response.json())
                print("\nResponse status code:", response.status_code)
                input("Press Enter to continue...")
                
            case '12':
                self.router("/session_cookie")
            case '13':
                print("Exiting...")
                exit()
            case _:
                print("Invalid choice, please try again.")

    def router(self, route):
        base_url = "http://localhost:8080"
        response = session.get(f"{base_url}/{route}")
        print("\n ")
        print(json.dumps(response.json(), indent=4))
        print("\nResponse status code:", response.status_code)
        input("Press Enter to continue...")

if __name__ == "__main__":  
    cli_instance = cli()
    cli_instance.start()