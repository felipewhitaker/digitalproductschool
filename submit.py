import requests

if __name__ == "__main__":

    EC2_IP = "http://107.22.134.151:8000/predict"
    req = requests.post(EC2_IP, params={"year": 2021, "month": 1})
    if not req.json().get("prediction", False):
        raise ValueError("Prediction not found in response.")

    req = requests.post(
        "https://dps-challenge.netlify.app/.netlify/functions/api/challenge",
        json = dict(
            github = "https://github.com/felipewhitaker/digitalproductschool",
            email = "felipewhitaker+dps@gmail.com",
            url = EC2_IP,
            notes = (
                "Request must be made through `http` protocol, not `https`."
                "The server is running on a free tier EC2 instance, so it may "
                "take a few seconds to respond."
            )
        )
    )

    print(req.json()) # {'message': 'Congratulations! Achieved Mission 3'}