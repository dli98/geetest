import requests
from decrypt521 import get_gt_challenge

def get_data(searchword, challenge, validate):
    data = {
        "searchword": searchword,
        "geetest_challenge": challenge,
        "token": "83860651",
        "tab": "ent_tab",
        "geetest_seccode": validate + "|jordan",
        "geetest_validate": validate,
    }



