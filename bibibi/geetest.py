import requests
import json
import time
import trace
import random
import os
from img_locate import ImgProcess
from decrypt import Encrypyed
import re

def cal_userresponse(a, b):
    d = []
    c = b[32:]
    for e in range(len(c)):
        f = ord(str(c[e]))
        tmp = f - 87 if f > 57 else f - 48
        d.append(tmp)

    c = 36 * d[0] + d[1]
    g = int(round(a)) + c
    b = b[:32]

    i = [[], [], [], [], []]
    j = {}
    k = 0
    e = 0
    for e in range(len(b)):
        h = b[e]
        if h in j:
            pass
        else:
            j[h] = 1
            i[k].append(h)
            k += 1
            k = 0 if (k == 5) else k

    n = g
    o = 4
    p = ""
    q = [1, 2, 5, 10, 50]
    while n > 0:
        if n - q[o] >= 0:
            m = int(random.random() * len(i[o]))
            p += str(i[o][m])
            n -= q[o]
        else:
            del (i[o])
            del (q[o])
            o -= 1
    return p
# 由challenge+track ==> 解析得到  userresponse 和 a
def get_userresponse_a(challenge, track_list, distance):
    # 路径需要自己拟合

    l = distance

    skip_list = fun_c(track_list)
    # for item in skip_list[1:]:
    #     print('item %.2f' % (item[0] / item[2]))

    a = fun_f(track_list)

    userresponse = cal_userresponse(l, challenge)

    return userresponse, a

# 计算每次间隔   相当于c函数
def fun_c(a):
    g = []
    e = []
    f = 0
    for h in range(len(a) - 1):
        b = int(round(a[h + 1][0] - a[h][0]))
        c = int(round(a[h + 1][1] - a[h][1]))
        d = int(round(a[h + 1][2] - a[h][2]))
        g.append([b, c, d])

        if b == c == d == 0:
            pass
        else:
            if b == c == 0:
                f += d
            else:
                e.append([b, c, d + f])
                f = 0
    if f != 0:
        e.append([b, c, f])
    return e


def fun_e(item):  # 相当于e函数
    b = [[1, 0], [2, 0], [1, -1], [1, 1], [0, 1], [0, -1], [3, 0], [2, -1], [2, 1]]
    c = 'stuvwxyz~'
    for i, t in enumerate(b):
        if t == item[:2]:
            return c[i]
    return 0


def fun_d(a):
    b = '()*,-./0123456789:?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqr'
    c = len(b)
    d = ''
    e = abs(a)
    f = int(e / c)
    if f >= c:
        f = c - 1
    if f > 0:
        d = b[f]
    e %= c
    g = ''
    if a < 0:
        g += '!'
    if d:
        g += '$'
    return g + d + b[e]


def fun_f(track_list):
    skip_list = fun_c(track_list)
    g, h, i = [], [], []
    for j in range(len(skip_list)):
        b = fun_e(skip_list[j])
        if b:
            h.append(b)
        else:
            g.append(fun_d(skip_list[j][0]))
            h.append(fun_d(skip_list[j][1]))
        i.append(fun_d(skip_list[j][2]))
    return ''.join(g) + '!!' + ''.join(h) + '!!' + ''.join(i)


def crack(gt, challenge, referer):
    headers = {
        "Referer": referer,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/53"
                      "7.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
    }

    # 获取初始化数据
    uri = "gt=" + gt + \
          "&challenge=" + challenge + \
          "&width=100%&product=float&offline=false&protocol=https://&voice=/static/js/voice.1.1.3.js" \
          "&type=slide&pencil=/static/js/pencil.1.0.1.js&path=/static/js/geetest.6.0.9.js&callback=geetest"
    response = requests.get(
        "https://api.geetest.com/get.php?" + uri,
        headers=headers,
    )
    initData = json.loads(response.text.replace("geetest(", "")[:-1])
    # 下载图片
    fullbg = str(time.time()) + str(random.random())
    bg = str(time.time()) + str(random.random())
    open("Image/" + fullbg + ".jpg", "wb").write(
        requests.get("https://static.geetest.com/" + initData["fullbg"]).content)
    open("Image/" + bg + ".jpg", "wb").write(requests.get("https://static.geetest.com/" + initData["bg"]).content)

    # 图片处理
    # 代码改自 OSinoooO/bilibili_geetest
    img_process = ImgProcess()
    img1 = img_process.get_merge_image('Image/' + fullbg + '.jpg')
    img2 = img_process.get_merge_image('Image/' + bg + '.jpg')
    os.remove("Image/" + fullbg + ".jpg")
    os.remove("Image/" + bg + ".jpg")
    distance = int(img_process.get_gap(img1, img2) - 7)

    # 采用垃圾算法获取轨迹 建议重写
    track = trace.get_trace_fast(distance)
    # track = input("%i track " % distance)
    print(distance)
    print("Track", track)
    userresponse, aa = get_userresponse_a(initData['challenge'], track, distance)
    passtime = 0
    for _ in range(len(track)):
        passtime += track[_][2]
    print(userresponse, aa, passtime)
    time.sleep(1)
    ep = Encrypyed()
    params = ep.encrypted_request(initData, userresponse,passtime, aa)
    response = requests.get(
        "https://api.geetest.com/ajax.php",
        headers=headers,
        params=params
    )
    text = re.sub("geetest_\d*\(", "", response.text)
    return json.loads(text[:-1])