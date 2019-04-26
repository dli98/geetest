this = {}


def E2(l4X, this):
    # l4x = 16
    s = "0123456789abcdefghijklmnopqrstuvwxyz"
    u9q = 5
    z9q = 4
    W9q = 6
    y9q = 6
    if y9q * (y9q + 1) * y9q % 2 == 0 and this['s'] < 0:
        return "-" + E2(l4X)  # 先运行g2
    if 16 == l4X and W9q * (W9q + 1) * W9q % 2 == 0:
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


this['DB'] = 28
this['DM'] = 268435455
this['DV'] = 268435456
this['F1'] = 24
this['F2'] = 4
this['FV'] = 4503599627370496


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
    object = dict(E0_object)
    objec["m"] = a5X,
    objec["mp"] = a5X["invDigit"](a5x),
    objec["mpl"] = 32767 & objec["mp"],
    objec["mph"] = objec["mp"] >> 15,
    objec["um"] = (1 << a5X["DB"] - 15) - 1,
    objec["mt2"] = 2 * a5X["t"];
    return object


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


def new_v0():
    object = dict(v0_object)
    return object

def v0(object, modulus, length=None, m6X=None):
    '''
    :param object:  v0_object对象
    :param modulus:
    :param length:
    :param m6X:
    :return:
    '''
    # l6X, T6X, m6X
    if None != modulus :
        if "int" == type(modulus):
            object["fromNumber"](modulus, length, m6X)
        elif None == length and "str" != type(modulus) :
            object["fromString"](modulus, 256)
        else:
            object["fromString"](modulus, length)


def Y2(modulus, length=16):
    new_v = new_v0()
    new_v['v0'](new_v, modulus, 16)

def V2(modulus, pub_key):
    i3q = 2;
    if modulus and pub_key and len(modulus) and len(pub_key):
        this["n"] = Y2(modulus, 16)
        this["e"] = int(pub_key, 16)
    else:
        print("Invalid RSA public key")

v0_object = {
    "v0": v0,
    "DB": "28",
    "DM": 268435455,
    "DV": 268435456,
    "F1": 24,
    "F2": 4,
    "FV": 4503599627370496,
    # "copyTo": Q2,
    "fromInt": p2,
    # "fromString": w2,
    # "clamp": q2,
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
P0 = {
    "doPUblic": i2,
    "e": 0,
    "n": 26,
    "d": None,
    "p": None,
    "q" : None,
    "dmp1":None,
    "dmq1":None,
    "coeff": None,
    "setPublic": V2(
    "00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81",
    "10001")
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

if __name__ == '__main__':
    J2(1)
    p0 = dict(P0)

