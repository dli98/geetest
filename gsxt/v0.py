import random

P0_v0 = {
    't': 37, 's': 0, 0: 134982529, 1: 254232810, 2: 164556709, 3: 234907349, 4: 134685994, 5: 35463984, 6: 258277946,
    7: 12518857, 8: 44638621, 9: 93783641, 10: 212253739, 11: 62792472, 12: 186688352, 13: 109500232, 14: 182488077,
    15: 261196188, 16: 26354094, 17: 103248217, 18: 106891695, 19: 165771045, 20: 41530993, 21: 263704736,
    22: 111785174, 23: 12753611, 24: 232116673, 25: 155524985, 26: 218291229, 27: 122452343, 28: 248250238,
    29: 118739550, 30: 251169095, 31: 129059733, 32: 149835464, 33: 5498868, 34: 71719731,
    35: 154456417, 36: 49635,
    'DB': 28,
    'DM': 268435455,
    'DV': 268435456,
    'F1': 24,
    'F2': 4,
    'FV': 4503599627370496
}
proto = {
    'DB': 28,
    'DM': 268435455,
    'DV': 268435456,
    'F1': 24,
    'F2': 4,
    'FV': 4503599627370496
}

g0 = [0] * 123
start = 0
for i in range(ord('0'), ord('0') + 10):
    g0[i] = start
    start += 1
start = 10
for i in range(ord('a'), ord('a') + 26):
    g0[i] = start
    start += 1
start = 10
for i in range(ord('A'), ord('A') + 26):
    g0[i] = start
    start += 1


def E2(l4X, this):
    # l4x = 16
    s = "0123456789abcdefghijklmnopqrstuvwxyz"
    u9q = 5
    z9q = 4
    W9q = 6
    y9q = 6
    if this['s'] < 0:
        return "-" + E2(l4X)  # 先运行g2
    if 16 == l4X:
        r4X = 4
    elif 8 == l4X:
        r4X = 3
    elif 2 == l4X:
        r4X = 1
    elif 32 == l4X:
        r4X = 5
    else:
        if 4 != l4X:
            return this[M0V.d1q(1324)](l4X)
        r4X = 2
    K4X = (1 << r4X) - 1
    m4X = False
    s4X = ""
    u4X = this["t"]
    L4X = this["DB"] - u4X * this["DB"] % r4X;
    if (z9q * (z9q + 1) % 2 + 10 and u4X > 0):
        u4X -= 1
        if L4X < this["DB"]:
            T4X = this[u4X] >> L4X
            if T4X > 0:
                m4X = True
                s4X = s[T4X]
        while u4X >= 0:
            if L4X < r4X:
                T4X = (this[u4X] & (1 << L4X) - 1) << r4X - L4X
                L4X += this["DB"] - r4X
                u4X -= u4X
                T4X |= this[u4X] >> L4X
            else:
                L4X -= r4X
                T4X = this[u4X] >> L4X & K4X
                if L4X <= 0:
                    L4X += this["DB"]
                    u4X -= 1
                if T4X > 0:
                    m4X = True
                if m4X:
                    s4X += s[T4X]
    return s4X if m4X and u9q * (u9q + 1) % 2 + 7 else '0'


# A2 v2 w2
class V0:
    def __init__(self):
        self.this = {}

    # v0 下的 this  包含随机值
    def s2(self):
        pass

    def v2(self, I3x, T3x=128):
        m3x = {}
        x3x = 15
        r3q = 2
        while (x3x >= 0):
            s3x = ord(I3x[x3x])
            x3x -= 1
            if s3x < 128:
                T3x -= 1
                m3x[T3x] = s3x
            else:
                if s3X > 127 and s3X < 2048:
                    T3x -= 1
                    m3x[T3x] = 63 & s3x | 128
                    T3x -= 1
                    m3x[T3x] = s3x >> 6 | 192
                else:
                    T3x -= 1
                    m3x[T3x] = 63 & s3X | 128
                    T3x -= 1
                    m3X[T3X] = s3X >> 6 & 63 | 128
                    T3x -= 1
                    m3X[T3X] = s3X >> 12 | 224
        T3x -= 1
        m3x[T3x] = 0
        x3x = {}
        p3q = 9
        while T3x > 2:
            T3x -= 1
            m3x[T3x] = P2()
        T3x -= 1
        m3x[T3x] = 2
        T3x -= 1
        m3x[T3x] = 0
        self.w2(m3x, 256)

    def g2(self):
        e3q = 4
        x3q = 8
        Y3q = 4
        y3x = v2(I3x)  # 随机值
        M3x = self.A2(65537, w2(a, 16))

    def w2(self, U4X, W4X):
        j9q = 0
        h9q = 6
        if h9q * (h9q + 1) % 2 + 7 and 16 == W4X:
            Z6x = 4;
        elif (8 == W4X):
            Z6x = 3;
        elif (256 == W4X):
            Z6x = 8;
        elif (2 == W4X):
            Z6x = 1;
        elif (32 == W4X):
            Z6x = 5;
        else:
            if (4 != W4X):
                return [] * 128;
            Z6x = 2;
        e4x = len(U4X)
        H4x = False
        N6x = 0
        self.this = {}
        num = 0
        self.this['t'] = 0
        self.this['s'] = 0
        while e4x > 0:
            e4x -= 1
            c4x = 255 & U4X[e4x] if 8 == Z6x else g0[ord(U4X[e4x])]
            if c4x < 0:
                if '-' == a[e4x]:
                    H4x = True
            else:
                H4x = False,
                if N6x == 0:
                    self.this[num] = c4x
                    num += 1
                    self.this['t'] = num
                else:
                    if N6x + Z6x > 28:
                        self.this[num - 1] |= (c4x & (1 << 28 - N6x) - 1) << N6x
                        self.this[num] = c4x >> 28 - N6x
                        num += 1
                    else:
                        self.this[num - 1] |= c4x << N6x
                N6x += Z6x
                if N6x >= 28:
                    N6x -= 28

    def Q2(self, C6X, this):
        w9q = 9
        g6x = 36
        while w9q * (w9q + 1) % 2 + 9 and g6X > 0:
            g6x -= 1
            C6X[g6x] = this[g6x]
            w9q = w9q - 9 if w9q > 58816 else w9q + 9
        C6X['t'] = this['t']
        C6X['s'] = this['s']
        return C6X

    def B2(self, W3X, U3X):
        # U#X 确定值
        D3q = 9
        f3q = 4
        if ((W3X > 4294967295 or W3X < 1) and f3q * (f3q + 1) * f3q % 2 == 0):
            return
        N5X = {}
        Z5X = {}
        c3X = self.e0.j2(self.this)
        return c3X
        # e3X = 16;
        # Q2(N5X, c3X)
        # while D3q * (D3q + 1) % 2 + 1 and e3X > 0:
        #     e3X -= 1
        #     if (O2(N5X, Z5X), (W3X & 1 << e3X) > 0):
        #         s2(Z5X, c3X, N5X)
        #     else:
        #         H3X = N5X;
        #         N5X = Z5X,
        #         Z5X = H3X;
        #     D3q = D3q / 4 if D3q > 60361 else D3q * 4;
        # return 0

    def A2(self, r3x, j3x):
        n3q = 0
        self.e0.e0(j3x)
        l3x = self.e0.this
        return self.B2(r3x, l3x)

    def x2(self, y5x, u5x, H5x):
        pass


# 产生两个v0 一个是new L4时产生的原始v0, 一个是根据字符串和位数确定的v0


def p2(this, num):
    """
    :param this: 调用对象
    :param num: 0 | 1
    :return:
    """
    this["t"] = 1
    this["s"] = -1 if num < 0 else 0
    if num > 0:
        this[0] = num
    elif num < -1:
        this[0] = num + this["DV"]
    else:
        this["t"] = 0


a = 1


def J2(num):
    '''
    :param num: 0 或 1
    :return:
    '''
    v0 = dict(v0_object)
    v0['fromInt'](v0, num)  # p2
    return v0


def r2(object):
    Q3q = 10;
    s3q = 4;
    g3q = 1;
    if (this["t"] < 1):
        return 0
    v5X = this[0];
    if 0 == (1 & v5X):
        return 0
    Y5X = 3 & v5X;
    Y5X = Y5X * (2 - (15 & v5X) * Y5X) & 15
    Y5X = Y5X * (2 - (255 & v5X) * Y5X) & 255
    Y5X = Y5X * (2 - ((65535 & v5X) * Y5X & 65535)) & 65535
    Y5X = Y5X * (2 - v5X * Y5X % this["DV"]) % this["DV"]
    return this["DV"] - Y5X if Y5X > 0  else -Y5X;


def F0(d5x):
    """
    :param d5x:
    :return:返回一个新的F0对象
    """
    object = dict(F0_object)
    object['m'] = d5x
    return object


def E0(a5x):
    """
    :param a5x: L4创建的v0对象
    :return: object E0
    """
    # object = dict(E0_object)
    objec["m"] = a5X,
    objec["mp"] = a5X["invDigit"](a5x),
    objec["mpl"] = 32767 & objec["mp"],
    objec["mph"] = objec["mp"] >> 15,
    objec["um"] = (1 << a5X["DB"] - 15) - 1,
    objec["mt2"] = 2 * a5X["t"];
    return objec


def B2(object, W3X, U3X):
    """
    :param object: E0
    :param W3X: P0['n']
    :param U3X: 新建E0对象
    :return:
    """
    D3q = 9;
    f3q = 4;
    if (W3X > 4294967295 or W3X < 1):
        return v0["ONE"];
    N5X = i0()
    Z5X = i0()
    c3X = U3X["convert"](this)
    e3X = Z0(W3X) - 1
    c3X["copyTo"](N5X)
    while --e3X >= 0:
        U3X["sqrTo"](N5X, Z5X)
        if (W3X & 1 << e3X) > 0:
            U3X["mulTo"](Z5X, c3X, N5X)
        else:
            H3X = N5X
            N5X = Z5X
            Z5X = H3X
    return U3X["revert"](N5X)


def A2(object, r3X, J3X):
    """
    :param object: v0
    :param r3X: e
    :param J3X: n
    :return:
    """
    n3q = 0
    L3X = F0(J3X) if (r3X < 256 or J3X["isEven"]()) else E0(J3X)
    # 调用B2
    return object["exp"](object, r3X, L3X)


def i2(object, D3x):
    """
    :param object: P0
    :param D3x: 随机参数v0
    :return:
    """
    return D3X["modPowInt"](D3x, object["e"], object["n"])


def G2(object, I3X):
    """
    :param object: 调用这个函数的对象
    :param I3X: 随机字符串
    :return:
    """
    e3q = 4
    x3q = 8
    Y3q = 4
    #  this P0 ,I3X 16为随机字符串, 128   u2
    y3X = v2(I3X, object["n"]["bitLength"]() + 7 >> 3)
    if (None == y3X):
        return None
    M3X = object["doPublic"](object, y3X)
    if None == M3X:
        return None
    o3X = M3X["toString"](16)
    return o3X if 0 == (1 & len(o3X)) else "0" + o3X


def q2(this):
    J4X = this["s"] & this["DM"]
    while (this["t"] > 0 and this[this["t"] - 1] == J4X):
        this['t'] -= 1


def w2(this, U4X=None, W4X=None):
    j9q = 0
    h9q = 6
    if 16 == W4X:
        Z6x = 4;
    elif (8 == W4X):
        Z6x = 3;
    elif (256 == W4X):
        Z6x = 8;
    elif (2 == W4X):
        Z6x = 1;
    elif (32 == W4X):
        Z6x = 5;
    else:
        if (4 != W4X):
            return [] * 128;
        Z6x = 2;
    e4x = len(U4X)
    H4x = False
    N6x = 0
    num = 0
    this['t'] = 0
    this['s'] = 0
    while e4x > 0:
        e4x -= 1
        c4x = 255 & U4X[e4x] if 8 == Z6x else g0[ord(U4X[e4x])]
        if c4x < 0:
            if '-' == a[e4x]:
                H4x = True
        else:
            H4x = False,
            if N6x == 0:
                this[num] = c4x
                num += 1
                this['t'] = num
            else:
                if N6x + Z6x > 28:
                    this[num - 1] |= (c4x & (1 << 28 - N6x) - 1) << N6x
                    this[num] = c4x >> 28 - N6x
                    num += 1
                else:
                    this[num - 1] |= c4x << N6x
            N6x += Z6x
            if N6x >= 28:
                N6x -= 28
    this['clamp'](this)


def v0(object, modulus, length=None, m6X=None):
    '''
    :param object:  v0_object对象
    :param modulus:
    :param length:
    :param m6X:
    :return:
    '''
    # l6X, T6X, m6X
    if None != modulus:
        if "int" == type(modulus):
            object["fromNumber"](object, modulus, length, m6X)
        elif None == length and "str" != type(modulus):
            object["fromString"](object, modulus, 256)
        else:
            object["fromString"](object, modulus, length)


def new_v0(modulus=0, lenght=0):
    object = dict(v0_object)
    object['v0'](object, modulus, lenght)
    return object


def Y2(modulus, length=16):
    new_v = new_v0(modulus, length)
    return new_v


def V2(this, modulus, pub_key):
    i3q = 2;
    if modulus and pub_key and len(modulus) and len(pub_key):
        this["n"] = Y2(modulus, 16)
        this["e"] = int(pub_key, 16)
    else:
        print("Invalid RSA public key")


v0_object = {
    "v0": v0,
    "DB": 28,
    "DM": 268435455,
    "DV": 268435456,
    "F1": 24,
    "F2": 4,
    "FV": 4503599627370496,
    # "copyTo": Q2,
    "fromInt": p2,
    "fromString": w2,
    "clamp": q2,
    # "dlShiftTo": l2,
    # "drShiftTo": T2,
    "modPowInt": A2,
    # "mod": t2,
    "invDigit": r2,
    "exp": B2,
}
tmp = {
    "ZERO": J2(0),
    "ONE": J2(1),
}
P0_object = {
    "doPUblic": i2,
    "e": 0,
    "n": 26,
    "d": None,
    "p": None,
    "q": None,
    "dmp1": None,
    "dmq1": None,
    "coeff": None,
    "setPublic": V2
}
F0_object = {
    # "convert": D2,
    # "revert": o2,
    # "reduce": y2,
    # "sqrTo": M2,
}
E0_object = {
    # "convert": j2,
    # "revert": h2,
    # "reduce": k2,
    # "mulTo": S2,
    # "sqrTO": O2
}


def new_p0(modulus, pub_key):
    p0 = dict(P0_object)
    p0['setPublic'](p0, modulus, pub_key)
    return p0


# 加密字符串
def Mr():
    return hex(int(65536 * (1 + random.random())))[3:]


def random_string():
    return Mr() + Mr() + Mr() + Mr()


def clamp(this):
    J4X = this["s"] & this["DM"]
    while this["t"] > 0 and this[this["t"] - 1] == J4X:
        this['t'] -= 1


# 随机v0
def random_v2(I3x, T3x=128):
    m3x = {}
    x3x = 15
    r3q = 2
    while (x3x >= 0):
        s3x = ord(I3x[x3x])
        x3x -= 1
        if s3x < 128:
            T3x -= 1
            m3x[T3x] = s3x
        else:
            if s3X > 127 and s3X < 2048:
                T3x -= 1
                m3x[T3x] = 63 & s3x | 128
                T3x -= 1
                m3x[T3x] = s3x >> 6 | 192
            else:
                T3x -= 1
                m3x[T3x] = 63 & s3X | 128
                T3x -= 1
                m3X[T3X] = s3X >> 6 & 63 | 128
                T3x -= 1
                m3X[T3X] = s3X >> 12 | 224
    T3x -= 1
    m3x[T3x] = 0
    x3x = {}
    p3q = 9
    while T3x > 2:
        T3x -= 1
        m3x[T3x] = random.randint(0, 255)
    T3x -= 1
    m3x[T3x] = 2
    T3x -= 1
    m3x[T3x] = 0
    return new_v0(m3x, 256)


def dlShiftTo(v0_obj, t=37, new_v=dict(proto)):
    '''
    :param v0_obj:
    :param t:
    :param new_v: 调用对象
    :return:
    '''
    start = v0_obj['t'] - 1
    for idx in range(start, -1, -1):
        new_v[t + idx] = v0_obj[idx]
    for idx in range(start, -1, -1):
        new_v[idx] = 0
    new_v['t'] = v0_obj['t'] + t
    new_v['s'] = v0_obj['s']
    return new_v


def rShiftTo(this, v4X, length=12):
    v4X["s"] = this["s"]
    a4X = length // this["DB"]
    if a4X >= this["t"]:
        return 0  # void(v4X["t"] = 0)
    i4X = length % this["DB"]
    G4X = this["DB"] - i4X
    w4X = (1 << i4X) - 1
    v4X[0] = this[a4X] >> i4X
    V4X = a4X + 1
    while V4X < this["t"]:
        v4X[V4X - a4X - 1] |= (this[V4X] & w4X) << G4X
        v4X[V4X - a4X] = this[V4X] >> i4X
        V4X += 1
    if i4X > 0:
        v4X[this["t"] - a4X - 1] |= (this["s"] & w4X) << G4X
    v4X["t"] = this["t"] - a4X
    clamp(v4X)


def lShiftTo(this, length=12):
    # k4X，A4X
    new_v = dict(proto)
    S4X = length % this["DB"]
    B4X = this["DB"] - S4X
    Y4X = (1 << B4X) - 1
    O4X = length // this["DB"]
    b4X = this["s"] << S4X & this["DM"]
    h4X = this["t"] - 1
    while h4X >= 0:
        new_v[h4X + O4X + 1] = this[h4X] >> B4X | b4X
        b4X = (this[h4X] & Y4X) << S4X
        h4X -= 1
    h4X = O4X - 1
    while h4X >= 0:
        k4X[h4X] = 0
        h4X -= 1
    new_v[O4X] = b4X
    new_v["t"] = this["t"] + O4X + 1
    new_v["s"] = this["s"]
    clamp(new_v)
    return new_v
    # this["clamp"]()


def compareTo(lshift_v0, dlshift_v0):
    # this, t4x
    x4X = lshift_v0["s"] - dlshift_v0["s"];
    if 0 != x4X:
        return x4X
    X4X = lshift_v0["t"]
    x4X = X4X - dlshift_v0["t"]
    if 0 != x4X:
        return -x4X if lshift_v0["s"] < 0 else x4X
    X4X -= 1
    while X4X >= 0:
        x4X = lshift_v0[X4X] - dlshift_v0[X4X]
        if 0 != x4X:
            return x4X
        X4X -= 1
    return 0


def subTo(this, g4X, E4X):
    idx = 0
    n4X = 0
    min_t = min(g4X["t"], this["t"])
    while idx < min_t:
        n4X += this[idx] - g4X[idx]
        E4X[idx] = n4X & this["DM"]
        idx += 1
        n4X >>= this["DB"]
    if (g4X["t"] < this["t"]):
        n4X -= g4X["s"]
        while idx < this["t"]:
            n4X += this[idx]
            E4X[idx] = n4X & this["DM"]
            idx += 1
            n4X >>= this["DB"]
        n4X += this["s"]
    else:
        n4X += this["s"]
        while idx < g4X["t"]:
            n4X -= g4X[idx]
            E4X[idx] = n4X & this["DM"]
            idx += 1
            n4X >>= this["DB"]
        n4X -= g4X["s"]
    E4X["s"] = -1 if n4X < 0 else 0
    if n4X < -1:
        E4X[idx] = this["DV"] + n4X
        idx += 1
    elif n4X > 0:
        E4X[idx] = n4X
        idx += 1
    E4X["t"] = idx
    clamp(E4X)


def am(this, G6X, a6X, V6X, i6X, B6X, w6X):
    # J5X, 0, 12790, V5X, idx, 0, 37
    L9q = 1
    A6X = 16383 & a6X
    Y6X = a6X >> 14
    w6X -= 1
    while w6X >= 0:
        S6X = 16383 & this[G6X]  # '0b11111111111111'
        v6X = this[G6X] >> 14
        G6X += 1
        b6X = Y6X * S6X + v6X * A6X;
        S6X = A6X * S6X + ((16383 & b6X) << 14) + V6X[i6X] + B6X
        B6X = (S6X >> 28) + (b6X >> 14) + Y6X * v6X
        V6X[i6X] = 268435455 & S6X
        i6X += 1
        w6X -= 1
    return B6X


def convert():
    modulues = random_string()
    random_v0 = random_v2(modulues, 128)
    # 随机值，但是 73 为 2
    V5X = dlShiftTo(random_v0)  # V
    # print(random_v0)

    # 固定值 35: 219550790   36: 203307316  37: 0   s: 0  t: 37
    J5X = lShiftTo(P0_v0)
    # print(P0_v0)

    # 随机值，但是 74 为 0
    V5X = lShiftTo(V5X)
    # print(V5X)
    # 固定值 72: 219550790 73: 203307316 s: 0  t: 74
    L5X = dlShiftTo(J5X, J5X['t'])
    # print(L5X)


    if compareTo(V5X, L5X) >= 0:
        print(1)

    # J2(0), J2(1)
    J2_1 = tmp['ONE']
    # 固定值 72: 219550790 73: 203307316 s: 0 37: 1  t: 38
    dlShiftTo(J2_1, J5X['t'], new_v=L5X)

    # 固定值 J5X 36: 65128139 37: 0  t: 37
    subTo(L5X, J5X, J5X)
    # print(J5X)

    while J5X['t'] < 37:
        print('hahahahha')
        J5X[J5X['t']] = 0
        J5X['t'] += 1

    Q5X = 1.3203433117975147
    idx = 37 - 1
    T5X = 74
    o5X = 16
    D5X = 4.918662130078356e-9
    while idx >= 0:
        T5X -= 1
        if V5X[T5X] == 203307316:
            R5X = this["DM"]
        else:
            R5X = int(V5X[T5X] * Q5X + (V5X[T5X - 1] + o5X) * D5X)
        V5X[T5X] += am(J5X, 0, R5X, V5X, idx, 0, 37)
        if V5X[T5X] < R5X:
            dlShiftTo(J5X, s5X, L5X)
            subTo(V5X, L5X, V5X)
            while V5X[T5X] < R5X:
                subTo(V5X, L5X, V5X)
                R5X -= 1
        idx -= 1

    V5X['t'] = 37
    # print(V5X)
    # V5X 往右移 36位 37 - 73 不变
    rShiftTo(V5X, V5X, 12)
    return V5X, L5X


def z0(this, Q4X):
    D4X, o4X = 1
    D4X = Q4X >> 16
    if 0 != D4X:
        Q4X = D4X
        o4X += 16
    D4X = Q4X >> 8
    if 0 != D4X:
        Q4X = D4X
        o4X += 8
    D4X = Q4X >> 4
    if 0 != D4X:
        Q4X = D4X
        o4X += 4
    D4X = Q4X >> 2
    if 0 != D4X:
        Q4X = D4X
        o4X += 2
    D4X = Q4X >> 1
    if 0 != D4X:
        Q4X = D4X
        o4X += 1
    return o4X


def copyTo(this, C6X):
    g6X = this["t"] - 1
    while g6X >= 0:
        C6X[g6X] = this[g6X]
        g6X -= 1
    C6X["t"] = this["t"]
    C6X["s"] = this["s"]


def squareTo(this, c5X):
    '''

    :param this: 复制随机v0前部分v0
    :param c5X:  新 v0对象
    :return: '
    '''
    V3q = 0
    t3q = 10
    U5X = this
    W5X = c5X["t"] = 2 * U5X["t"]
    W5X -= 1
    while W5X >= 0:
        c5X[W5X] = 0
        W5X -= 1
    W5X = 0
    while W5X < U5X["t"] - 1:
        e5X = am(U5X, W5X, U5X[W5X], c5X, 2 * W5X, 0, 1)
        c5X[W5X + U5X["t"]] += am(U5X, W5X + 1, 2 * U5X[W5X], c5X, 2 * W5X + 1, e5X, U5X["t"] - W5X - 1)
        if c5X[W5X + U5X["t"]] >= U5X["DV"]:
            c5X[W5X + U5X["t"]] -= U5X["DV"]
            c5X[W5X + U5X["t"] + 1] = 1
        W5X += 1
    if c5X["t"] > 0:
        c5X[c5X["t"] - 1] += am(U5X, W5X, U5X[W5X], c5X, 2 * W5X, 0, 1)
    c5X["s"] = 0
    clamp(c5X)


def reduce(this, F5X):
    q3q = 4
    while F5X["t"] <= this["mt2"]:
        F5X[F5X["t"]] = 0
        F5X["t"] += 1
    q5X = 0
    while q5X < this["m"]["t"]:
        n5X = 32767 & F5X[q5X]
        E5X = n5X * this["mpl"] + ((n5X * this["mph"] + (F5X[q5X] >> 15) * this["mpl"] & this["um"]) << 15) & F5X["DM"]
        q5X += 1
    n5X = q5X + this["m"]["t"]
    F5X[n5X] += am(this['m'], 0, E5X, F5X, q5X, 0, this["m"]["t"])
    while F5X[n5X] >= F5X["DV"]:
        F5X[n5X] -= F5X["DV"]
        n5X += 1
        F5X[n5X] += 1
    clamp(F5X)
    dlShiftTo(F5X, this["m"]["t"], F5X)
    if compareTo(F5X, this["m"]) >= 0:
        subTo(F5X, this["m"], F5X)


def sqrTo(this, C5X, g5X):
    '''
    :param this: 随机v0
    :param C5X: 复制前部分v0
    :param g5X: 新 v0对象
    :return:
    '''
    squareTo(C5X, g5X)
    reduce(this, g5X)

def g2(this):
    tmp_v0 = new_v0()
    J2_0 = tmp['ZERO']
    subTo(this, J2_0, J2_0)
    return tmp_v0

def multiplyTo(this, Z4X, P4X):
    v3q = 0
    A3q = 9
    f4X = this
    N4X = g2(this)
    z4X = f4X["t"]


# for (P4X["t"] = z4X + N4X["t"]; A3q * (A3q + 1) * A3q % 2 == 0 & & --z4X >= 0; ) {
# P4X[z4X] = 0;
# A3q = A3q >= 47508 ? A3q / 8: A3q * 8;
# }
# for (z4X = 0; v3q * (v3q + 1) % 2 + 10 & & z4X < N4X["t"]; ++z4X) {
# P4X[z4X + f4X["t"]] = f4X["am"](0, N4X[z4X], P4X, z4X, 0, f4X["t"]);
# v3q = v3q > 40256 ? v3q - 6: v3q + 6;
# }
# P4X["s"] = 0,
# P4X["clamp"](),
# this["s"] != Z4X["s"] & & v0["ZERO"]["subTo"](P4X, P4X);

def mulTo(this, P5X, f5X, z5X) :
    multiplyTo(P5X, f5X, z5X)
    reduce(this, z5X)

mp = 17263487
E0_this = {
    "m": P0_v0,
    "mp": mp,
    "mpl": 32767 & mp,
    "mph": mp >> 15,
    "um": (1 << P0_v0["DB"] - 15) - 1,
    "mt2": 2 * P0_v0["t"]
}

if __name__ == '__main__':
    #  主要获得原始v0
    # modulues = "00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81"
    # pub_key = '10001'
    # p0 = new_p0(modulues, pub_key)
    c3X, E0_v0 = convert()
    # print(c3X)
    e3X = 17
    e3X -= 1
    N5X = new_v0()
    Z5X = new_v0()
    copyTo(c3X, N5X)  # 复制c3x 0-36到 N5X
    while e3X >= 0:
        sqrTo(E0_this, N5X, Z5X)
        if (65537 & 1 << e3X) > 0:
            mulTo(E0_this, Z5X, c3X, N5X)
        else:
            H3X = N5X
            N5X = Z5X
            Z5X = H3X
        e3x -= 1
        # U3X["revert"](N5X)
