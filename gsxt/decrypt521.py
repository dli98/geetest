import requests
import time
import re
import execjs


def get_gt_challenge():
    t = time.time()
    # 第一次访问获取动态加密的JS
    url = 'http://www.gsxt.gov.cn/SearchItemCaptcha?t=' + str(int(t * 1000))
    # print(url)
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'www.gsxt.gov.cn',
        'Referer': 'http://www.gsxt.gov.cn/index.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    r = requests.get(url, headers=headers)
    __jsluid = r.headers["Set-Cookie"].split(';')[0]
    txt_521 = ''.join(re.findall('<script>(.*?)</script>', r.text))
    # print(__jsluid)
    # 对拿来的js代码进行修改并且运行

    node = execjs.get()
    txt_521 = txt_521.replace('{eval', '{return')
    content = execjs.compile(txt_521)
    first_decryption = content.call('f')  # 一级解密结果
    # print(first_decryption)
    func_name = re.match('var (.*?)=', first_decryption).group(1)

    s = 'var a' + first_decryption.split('document.cookie')[1].split("Path=/;'")[0] + "Path=/;';return a;"
    s = re.sub(r'document.create.*?firstChild.href', '"{}"'.format(url), s)
    # print(s)
    resHtml = "function getClearance(){"'var window = {};' + s + "};"
    ctx = execjs.compile(resHtml)
    # 二级解密结果
    __jsl_clearance = ctx.call('getClearance').split(';')[0]
    # print(__jsl_clearance)

    # 需要注意的是 User-Agent 一定要和第一次访问设置的一模一样，不然照样返回521
    headers['Cookie'] = __jsluid + ';' + __jsl_clearance + ';'
    try:
        r = requests.get(url, headers=headers).json()
        print(r)
        if 'challenge' in r and 'gt' in r:
            return r['gt'], r['challenge']
        else:
            return '', ''
    except Exception as e:
        print(e)
        return '', ''


if __name__ == '__main__':
    gt, challenge = get_gt_challenge()
    print(gt, challenge)
