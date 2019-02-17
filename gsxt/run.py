import requests
from 

def get_data(searchword, challenge, validate):
    data = {
        "searchword": searchword,
        "geetest_challenge": challenge,
        "token": "83860651",
        "tab": "ent_tab",
        "geetest_seccode": validate + "|jordan",
        "geetest_validate": validate,
    }


if __name__ == '__main__':
    # get_data("百度")