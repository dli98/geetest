import requests
import time
import execjs


def get_w():
    node = execjs.get()
    with open('demo.js', 'r', encoding='utf-8') as f:
        decrypt_js = f.read()
    ctx = execjs.compile(decrypt_js)
    # print(ctx)
    data = ctx.call('decrypt')
    print(data)


# 获得bg和fullbg的地址
def get_bg_fullbg(gt, challenge):
    url = 'http://api.geetest.com/get.php'
    headers = {
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Host": "api.geetest.com",
        "Accept": "*/*",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        "Connection": "keep-alive",
        'Referer': 'http://www.gsxt.gov.cn/index.html'
    }
    t = time.time()
    data = {
        'is_next': 'true',
        'type': 'slide3',
        'gt': gt,
        'challenge': challenge,
        'lang': 'zh-cn',
        'https': 'false',
        'protocol': 'http://',
        'offline': 'false',
        'product': 'embed',
        'api_server': 'api.geetest.com',
        'isPC': 'true',
        'width': '100%',
        'callback': 'geetest_' + str(int(t * 1000)),
    }

    res = requests.get(url, params=data, headers=headers)
    print(res.url)
    print(res.text)
    # website = 'http://static.geetest.com/'
    # 
    # json_data = re.findall(r'\((.*?)\)', res)[0]
    # json_data = json_data.replace('false', '"0"').replace('true', '"0"')
    # json_data = eval(json_data)
    # 
    # challenge = json_data['challenge']
    # bg = website + json_data['bg']
    # fullbg = website + json_data['fullbg']
    # 
    # return challenge, bg, fullbg


if __name__ == '__main__':
    get_w()
    # from decrypt521 import get_gt_challenge
    #
    # gt, challenge = get_gt_challenge()
    # get_bg_fullbg(gt, challenge)
