import os
import sys

import requests
from dotenv import load_dotenv


def main():

    load_dotenv()

    platform = sys.argv[1]
    user_id = sys.argv[2]
    url = f"https://public-api.tracker.gg/v2/apex/standard/profile/{platform}/{user_id}"

    trn_api_key = os.environ["TRN_API_KEY"]
    headers = {"TRN-Api-Key": trn_api_key}

    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        return

    data = res.json()
    segments = data.get("data").get("segments")

    for segment in segments:
        if segment.get("type") == "overview":
            rank_name = segment.get("stats").get("rankScore").get("metadata").get("rankName")
            rank_point = segment.get("stats").get("rankScore").get("displayValue")
            break
    
    print(rank_name)
    print(rank_point)



if __name__ == "__main__":
    main()
