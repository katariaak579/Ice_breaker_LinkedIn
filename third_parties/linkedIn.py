import os
import requests


def scrape_linkedin_profile(linkedIn_profile_url: str):
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
    # response = requests.get(
    #     api_endpoint,params={"url":linkedIn_profile_url},headers=header_dic
    # )
    response = requests.get(
        "https://gist.githubusercontent.com/katariaak579/55ed3eec536de12b59f0d2b8ee042bee/raw/19a25e651106a25d9af2020f5750f38301009f45/bill-gates.json"
    )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
