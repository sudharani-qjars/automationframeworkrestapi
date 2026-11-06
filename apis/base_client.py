"""
base_client.py

Simple HTTP client for API automation.
"""
import allure
import requests
import json

class BaseClient:
    """
    Base HTTP Client
    """

    def __init__(self, base_url: str):
        """
        Initialize the client.

        Args:
            base_url (str): Base URL of the API.
        """
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def get(self, endpoint: str, params=None, headers=None):
        """
        Send GET request.
        """
        response = self.session.get(
            url=f"{self.base_url}{endpoint}",
            params=params,
            headers=headers
        )
        allure.attach(
            f"{self.base_url}{endpoint}",
            "Request URL",
            allure.attachment_type.TEXT
        )

        allure.attach(
            json.dumps(response.json(), indent=4),
            "Response",
            allure.attachment_type.JSON
        )
        return response

    def post(self, endpoint: str, json=None, data=None, headers=None):
        """
        Send POST request.
        """
        response = self.session.post(
            url=f"{self.base_url}{endpoint}",
            json=json,
            data=data,
            headers=headers
        )
        allure.attach(
            f"{self.base_url}{endpoint}",
            "Request URL",
            allure.attachment_type.TEXT
        )

        allure.attach(
            json.dumps(response.json(), indent=4),
            "Response",
            allure.attachment_type.JSON
        )
        return response

    def put(self, endpoint: str, json=None, headers=None):
        """
        Send PUT request.
        """
        response = self.session.put(
            url=f"{self.base_url}{endpoint}",
            json=json,
            headers=headers
        )
        allure.attach(
            f"{self.base_url}{endpoint}",
            "Request URL",
            allure.attachment_type.TEXT
        )

        allure.attach(
            json.dumps(response.json(), indent=4),
            "Response",
            allure.attachment_type.JSON
        )
        return response


    def patch(self, endpoint: str, json=None, headers=None):
        """
        Send PATCH request.
        """
        response = self.session.patch(
            url=f"{self.base_url}{endpoint}",
            json=json,
            headers=headers
        )
        allure.attach(
            f"{self.base_url}{endpoint}",
            "Request URL",
            allure.attachment_type.TEXT
        )

        allure.attach(
            json.dumps(response.json(), indent=4),
            "Response",
            allure.attachment_type.JSON
        )
        return response

    def delete(self, endpoint: str, headers=None):
        """
        Send DELETE request.
        """
        response = self.session.delete(
            url=f"{self.base_url}{endpoint}",
            headers=headers
        )
        allure.attach(
            f"{self.base_url}{endpoint}",
            "Request URL",
            allure.attachment_type.TEXT
        )

        allure.attach(
            json.dumps(response.json(), indent=4),
            "Response",
            allure.attachment_type.JSON
        )
        return response

    def close(self):
        """
        Close the HTTP session.
        """
        self.session.close()