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


this = {
    0: 222967939,
    1: 118908145,
    2: 188415329,
    3: 75069744,
    4: 264717231,
    5: 28197152,
    6: 151234699,
    7: 123072569,
    8: 257940046,
    9: 136149239,
    10: 69153984,
    11: 160478855,
    12: 113700534,
    13: 197818708,
    14: 252746462,
    15: 240101000,
    16: 131174635,
    17: 142190454,
    18: 149892651,
    19: 45315654,
    20: 12583352,
    21: 62228899,
    22: 239759230,
    23: 116435782,
    24: 26517773,
    25: 106233527,
    26: 256801748,
    27: 195663433,
    28: 28425246,
    29: 145098894,
    30: 169407876,
    31: 232542245,
    32: 212533116,
    33: 98495345,
    34: 243409245,
    35: 36623821,
    36: 25860,
    37: 222967939,
    38: 118908145,
    39: 188415329,
    40: 75069744,
    41: 264717231,
    42: 28197152,
    43: 151234699,
    44: 123072569,
    45: 257940046,
    46: 136149239,
    47: 69153984,
    48: 160478855,
    49: 113700534,
    50: 197818708,
    51: 252746462,
    52: 240101000,
    53: 131174635,
    54: 142190454,
    55: 149892651,
    56: 45315654,
    57: 12583352,
    58: 62228899,
    59: 239759230,
    60: 116435782,
    61: 26517773,
    62: 106233527,
    63: 256801748,
    64: 195663433,
    65: 28425246,
    66: 145098894,
    67: 169407876,
    68: 232542245,
    69: 212533116,
    70: 98495345,
    71: 243409245,
    72: 36623821,
    73: 25860,
    74: 0,
    's': 0,
    't': 37,
}

this['DB'] = 28
this['DM'] = 268435455
this['DV'] = 268435456
this['F1'] = 24
this['F2'] = 4
this['FV'] = 4503599627370496

E2(16, this)


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
        while r3q * (r3q + 1) * r3q % 2 == 0 and (x3x >= 0):
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
            r3q = r3q / 6 if r3q > 41510 else r3q * 6
        T3x -= 1
        m3x[T3x] = 0
        x3x = {}
        p3q = 9
        while p3q * (p3q + 1) * p3q % 2 == 0 and T3x > 2:
            T3x -= 1
            m3x[T3x] = P2()
            p3q = p3q - 2 if p3q > 51568 else p3q + 2
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
        while e4x > 0 and j9q * (j9q + 1) % 2 + 2:
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
            j9q = j9q / 10 if j9q >= 24874 else j9q * 10

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
