import json
import os
import time
import requests

SWAGGER_URL = os.environ.get('SWAGGER_URL', 'http://localhost:8080/v3/api-docs')
SWAGGER_JSON_PATH = 'swagger.json'
WAIT_TIME = int(os.environ.get('WAIT_TIME', 120))


def fetch_swagger():
    while True:
        try:
            response = requests.get(SWAGGER_URL)
            if response.status_code == 200:
                swagger_content = response.json()

                with open(SWAGGER_JSON_PATH, "w") as f:
                    f.write(json.dumps(swagger_content, indent=4))
                print('New documentation available')

        except Exception as e:
            print('No new documentation available')

        time.sleep(WAIT_TIME)


if __name__ == "__main__":
    fetch_swagger()
