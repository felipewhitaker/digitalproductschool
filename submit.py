import requests

if __name__ == "__main__":

    EC2_DYNAMIC_IP = "http://3.222.96.133:8000/"

    req = requests.post(
        "https://dps-challenge.netlify.app/.netlify/functions/api/challenge",
        json = dict(
            github = "https://github.com/felipewhitaker/digitalproductschool",
            email = "felipewhitaker+dps@gmail.com",
            url = EC2_DYNAMIC_IP,
            notes = (
                "Request must be made through `http` protocol, not `https`."
                "Moreover, the application was deployed over a EC2 instance with"
                "a dynamic IP address. Therefore, the IP address may change."
            )
        )
    )

    print(req.json()) # {'message': 'Congratulations! Achieved Mission 3'}