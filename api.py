import requests

class PredictAPI:
    def __init__(self, base_url: str = 'http://0.0.0.0:80'):
        """
        Initializes the PredictAPI client with the base URL of the FastAPI server.

        Args:
            base_url (str): The base URL for the FastAPI server.
        """
        self.base_url = base_url

    def get_status(self):
        """
        Retrieves the status and version of the model from the home endpoint.

        Returns:
            dict: A dictionary containing the status and version of the model.
        """
        response = requests.get(f"{self.base_url}/")
        return response.json()

    def predict(self, input_int: int = -1):
        """
        Sends a POST request to the predict endpoint with an integer input.

        Args:
            input_int (int): The integer to be sent for prediction.
        Returns:
            dict: A dictionary containing the prediction result.
        """
        data = {"input_int": input_int}
        response = requests.post(f"{self.base_url}/predict", json = data)
        return response.json()