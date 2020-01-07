import json
import requests

# if you want to test local
# url = "http://localhost:9000"

# deployed
url = "http://nlp-subreddit-predictor.herokuapp.com/"

##

val = {'post_body': "Example of a reddit post body for testing"}



# you'll get a 200 response if the keys align
# and something bad if the keys don't align.
if __name__ == '__main__':
    r_success = requests.post(url, data=json.dumps(val))
    print(
        f"Request responded: {r_success}.\nResponse was\n{r_success.json()}")
