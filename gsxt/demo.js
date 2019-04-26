var window = {};
var L4 = function() {
    //返回指定位置的字符
    function e2(F6X) {
        return H2["charAt"](F6X);
    }
    function h2(object, w5X) {
        var G5X = i0();
        return w5X["copyTo"](G5X),
        object["reduce"](G5X),
        G5X;
    }
    function R2(object, Z4X, P4X) {
        var v3q = 0;
        var A3q = 9;
        var f4X = object["abs"]()
          , N4X = Z4X["abs"]()
          , z4X = f4X["t"];
        for (P4X["t"] = z4X + N4X["t"]; A3q * (A3q + 1) * A3q % 2 == 0 && --z4X >= 0; ) {
            P4X[z4X] = 0;
            A3q = A3q >= 47508 ? A3q / 8 : A3q * 8;
        }
        for (z4X = 0; v3q * (v3q + 1) % 2 + 10 && z4X < N4X["t"]; ++z4X) {
            P4X[z4X + f4X["t"]] = f4X["am"](0, N4X[z4X], P4X, z4X, 0, f4X["t"]);
            v3q = v3q > 40256 ? v3q - 6 : v3q + 6;
        }
        P4X["s"] = 0,
        P4X["clamp"](),
        object["s"] != Z4X["s"] && v0["ZERO"]["subTo"](P4X, P4X);
    }
    var E3q = 3;
    function o2(h5X) {
        return h5X;
    }
    var w3q = 6;
    function O2(object, C5X, g5X) {
        C5X["squareTo"](g5X),
        object["reduce"](g5X);
    }
    function l2(object, I4X, M4X) {
        var r9q = 10;
        var S9q = 1;
        var y4X;
        for (y4X = object["t"] - 1; y4X >= 0; --y4X) {
            M4X[y4X + I4X] = object[y4X];
        }
        for (y4X = I4X - 1; y4X >= 0 && r9q * (r9q + 1) * r9q % 2 == 0; --y4X) {
            M4X[y4X] = 0;
            r9q = r9q >= 59102 ? r9q - 6 : r9q + 6;
        }
        M4X["t"] = object["t"] + I4X,
        M4X["s"] = object["s"];
    }
    var T3q = 8;
    function E0(object, a5X) {
        object["m"] = a5X,
        object["mp"] = a5X["invDigit"](),
        object["mpl"] = 32767 & object["mp"],
        object["mph"] = object["mp"] >> 15,
        object["um"] = (1 << a5X["DB"] - 15) - 1,
        object["mt2"] = 2 * a5X["t"];
    }
    var L3q = 10;
    function y2(object, k5X) {
        k5X["divRemTo"](object["m"], null, k5X);
    }
    function T2(object, d4X, j4X) {
        var k9q = 5;
        for (var p4X = d4X; p4X < object["t"] && k9q * (k9q + 1) % 2 + 9; ++p4X) {
            j4X[p4X - d4X] = object[p4X];
            k9q = k9q > 77578 ? k9q / 2 : k9q * 2;
        }
        j4X["t"] = Math["max"](object["t"] - d4X, 0),
        j4X["s"] = object["s"];
    }
    function s2(object, F4X, v4X) {
        var G9q = 9;
        var J9q = 10;
        v4X["s"] = object["s"];
        var a4X = Math["floor"](F4X / object["DB"]);
        if (a4X >= object["t"])
            return void (v4X["t"] = 0);
        var i4X = F4X % object["DB"]
          , G4X = object["DB"] - i4X
          , w4X = (1 << i4X) - 1;
        v4X[0] = object[a4X] >> i4X;
        for (var V4X = a4X + 1; V4X < object["t"]; ++V4X) {
            v4X[V4X - a4X - 1] |= (object[V4X] & w4X) << G4X,
            v4X[V4X - a4X] = object[V4X] >> i4X;
        }
        i4X > 0 && (v4X[object["t"] - a4X - 1] |= (object["s"] & w4X) << G4X),
        v4X["t"] = object["t"] - a4X,
        v4X["clamp"]();
    }
    function Z2(object, e6X) {
        var p9q = 9;
        var R9q = 7;
        var U6X, c6X, H6X;
        // 0-255的数组， e6x w0 256随机数组
        for (U6X = 0; U6X < 256 ; ++U6X) {
            object["S"][U6X] = U6X;
        }
        for (c6X = 0,
        U6X = 0; U6X < 256; ++U6X) {
            // 保证&255 c6x在255以内
            c6X = c6X + object["S"][U6X] + e6X[U6X % e6X["length"]] & 255,
            H6X = object["S"][U6X], // U6X 和H6X 交换位置
            object["S"][U6X] = object["S"][c6X],
            object["S"][c6X] = H6X;
        }
        object["i"] = 0,
        object["j"] = 0;
    }
    function z2(object, u6X) {
        // u6x =[0]
        var L6X;
        for (L6X = 0; L6X < u6X["length"]; ++L6X) {
            u6X[L6X] = P2();
        }
    }
    // 调用w2, ase publish key, 16
    function v0(object, l6X, T6X, m6X) {
        var x9q = 0;
        null != l6X && ("number" == typeof l6X ? object["fromNumber"](l6X, T6X, m6X) : null == T6X && "string" != typeof l6X ? object["fromString"](l6X, 256) : object["fromString"](l6X, T6X));
    }
    function d2(object, k6X, d6X, j6X, h6X, o6X, O6X) {
        var l9q = 4;
        for (var M6X = 32767 & d6X, I6X = d6X >> 15; l9q * (l9q + 1) % 2 + 8 && --O6X >= 0; ) {
            var D6X = 32767 & object[k6X]
              , p6X = object[k6X++] >> 15
              , y6X = I6X * D6X + p6X * M6X;
            D6X = M6X * D6X + ((32767 & y6X) << 15) + j6X[h6X] + (1073741823 & o6X),
            o6X = (D6X >>> 30) + (y6X >>> 15) + I6X * p6X + (o6X >>> 30),
            j6X[h6X++] = 1073741823 & D6X;
            l9q = l9q > 42537 ? l9q / 3 : l9q * 3;
        }
        return o6X;
    }
    function D2(object,j5X) {
        var m3q = 10;
        return (j5X["s"] < 0 || j5X["compareTo"](object["m"]) >= 0) && m3q * (m3q + 1) * m3q % 2 == 0 ? j5X["mod"](object["m"]) : j5X;
    }
    function S2(object, P5X, f5X, z5X) {
        P5X["multiplyTo"](f5X, z5X),
        object["reduce"](z5X);
    }
    function L2(object, q6X, E6X) {
        // g0 123位的数组，0 48-58：1-10，A 65-90：10-35  a 97-123：10-35
        var n6X = g0[q6X["charCodeAt"](E6X)];
        return null == n6X ? -1 : n6X;
    }
    // w参数 16
    function E2(object, l4X) {
        var u9q = 5;
        var z9q = 4;
        var W9q = 6;
        var y9q = 6;
        if (y9q * (y9q + 1) * y9q % 2 == 0 && object["s"] < 0)
            return "-" + object["negate"]()["toString"](l4X);
        var r4X;
        if (16 == l4X)
            r4X = 4;
        else if (8 == l4X)
            r4X = 3;
        else if (2 == l4X)
            r4X = 1;
        else if (32 == l4X)
            r4X = 5;
        else {
            if (4 != l4X)
                return object["toRadix"](l4X);
            r4X = 2;
        }
        var T4X, K4X = (1 << r4X) - 1, m4X = !1, s4X = "", u4X = object["t"], L4X = object["DB"] - u4X * object["DB"] % r4X;
        if (z9q * (z9q + 1) % 2 + 10 && u4X-- > 0)
            for (L4X < object["DB"] && (T4X = object[u4X] >> L4X) > 0 && (m4X = !0,
            s4X = e2(T4X)); u4X >= 0; )
                L4X < r4X ? (T4X = (object[u4X] & (1 << L4X) - 1) << r4X - L4X,
                T4X |= object[--u4X] >> (L4X += object["DB"] - r4X)) : (T4X = object[u4X] >> (L4X -= r4X) & K4X,
                L4X <= 0 && (L4X += object["DB"],
                --u4X)),
                T4X > 0 && (m4X = !0),
                m4X && (s4X += e2(T4X));
        return m4X && u9q * (u9q + 1) % 2 + 7 ? s4X : "0";
    }
    var l3q = 3;
    W2["prototype"]["init"] = Z2,
    W2["prototype"]["next"] = N2;
    // 返回属性 v0 调用V2
    function P0(object) {
        object["n"] = null,
        object["e"] = 0,
        object["d"] = null,
        object["p"] = null,
        object["q"] = null,
        object["dmp1"] = null,
        object["dmq1"] = null,
        object["coeff"] = null;
        object["setPublic"]("00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81", "10001");
    }
    function M2(object, S5X, b5X, O5X) {
        S5X["multiplyTo"](b5X, O5X),
        object["reduce"](O5X);
    }
    var z0, w0, V0, U2 = 256;
    function x2(object, c5X) {
        var V3q = 0;
        var t3q = 10;
        for (var U5X = object["abs"](), W5X = c5X["t"] = 2 * U5X["t"]; t3q * (t3q + 1) * t3q % 2 == 0 && --W5X >= 0; ) {
            c5X[W5X] = 0;
            t3q = t3q > 88868 ? t3q / 8 : t3q * 8;
        }
        for (W5X = 0; W5X < U5X["t"] - 1 && V3q * (V3q + 1) * V3q % 2 == 0; ++W5X) {
            var e5X = U5X["am"](W5X, U5X[W5X], c5X, 2 * W5X, 0, 1);
            (c5X[W5X + U5X["t"]] += U5X["am"](W5X + 1, 2 * U5X[W5X], c5X, 2 * W5X + 1, e5X, U5X["t"] - W5X - 1)) >= U5X["DV"] && (c5X[W5X + U5X["t"]] -= U5X["DV"],
            c5X[W5X + U5X["t"] + 1] = 1);
            V3q = V3q > 64483 ? V3q - 5 : V3q + 5;
        }
        c5X["t"] > 0 && (c5X[c5X["t"] - 1] += U5X["am"](W5X, U5X[W5X], c5X, 2 * W5X, 0, 1)),
        c5X["s"] = 0,
        c5X["clamp"]();
    }
    function g2(object) {
        var R4X = i0();
        return v0["ZERO"]["subTo"](object, R4X),
        R4X;
    }
    // 256为随机数 wo V0 256 U2
    if (null == w0 && l3q * (l3q + 1) % 2 + 9) {
        w0 = [],
        V0 = 0;
        var f0;
        if (e6["crypto"] && e6["crypto"]["getRandomValues"]) {
            var N0 = new Uint32Array(256);
            for (e6["crypto"]["getRandomValues"](N0),
            f0 = 0; f0 < N0["length"]; ++f0)
                w0[V0++] = 255 & N0[f0];
        }
        var q0 = 0
          , C0 = function(p3X) {
            if ((q0 = q0 || 0) >= 256 || V0 >= U2)
                return void (e6["removeEventListener"] ? (q0 = 0,
                e6["removeEventListener"]("mousemove", C0, !1)) : e6["detachEvent"] && (q0 = 0,
                e6["detachEvent"]("onmousemove", C0)));
            try {
                var d3X = p3X["x"] + p3X["y"];
                w0[V0++] = 255 & d3X,
                q0 += 1;
            } catch (j3X) {}
        };
        e6["addEventListener"] ? e6["addEventListener"]("mousemove", C0, !1) : e6["attachEvent"] && e6["attachEvent"]("onmousemove", C0);
    }
    function p2(object, z6X) {
        object["t"] = 1,
        object["s"] = z6X < 0 ? -1 : 0,
        z6X > 0  ? object[0] = z6X : z6X < -1 ? object[0] = z6X + object["DV"] : object["t"] = 0;
    }
    function Q2(object, C6X) {
        var w9q = 9;
        for (var g6X = object["t"] - 1; w9q * (w9q + 1) % 2 + 9 && g6X >= 0; --g6X) {
            C6X[g6X] = object[g6X];
            w9q = w9q > 58816 ? w9q - 9 : w9q + 9;
        }
        C6X["t"] = object["t"],
        C6X["s"] = object["s"];
    }
    c2["prototype"]["nextBytes"] = z2;
    function J2(object, f6X) {
        var P6X = i0();
        // 调用P2
        return P6X["fromInt"](P6X,f6X),
        P6X;
    }
    function K2(object, g4X, E4X) {
        // L5X 调用  J5X J5X
        var H3q = 3;
        var c3q = 7;
        var C3q = 1;
        var P3q = 1;
        var Z9q = 2;
        for (var q4X = 0, n4X = 0, C4X = Math["min"](g4X["t"], object["t"]); q4X < C4X; ) {
            n4X += object[q4X] - g4X[q4X],
            E4X[q4X++] = n4X & object["DM"],
            n4X >>= object["DB"];
        }
        if (g4X["t"] < object["t"]) {
            for (n4X -= g4X["s"]; q4X < object["t"]; )
                n4X += object[q4X],
                E4X[q4X++] = n4X & object["DM"],
                n4X >>= object["DB"];
            n4X += object["s"];
        } else if (P3q * (P3q + 1) % 2 + 2) {
            for (n4X += object["s"]; q4X < g4X["t"]; )
                n4X -= g4X[q4X],
                E4X[q4X++] = n4X & object["DM"],
                n4X >>= object["DB"];
            n4X -= g4X["s"];
        }
        E4X["s"] = n4X < 0 ? -1 : 0,
        n4X < -1? E4X[q4X++] = object["DV"] + n4X : n4X > 0 && (E4X[q4X++] = n4X),
        E4X["t"] = q4X,
        E4X["clamp"]();
    }
    // new 一个对象 W2
    function f2() {
        return new W2();
    }
    var G0;
    "Microsoft Internet Explorer" == l6["appName"] && L3q * (L3q + 1) % 2 + 5 ? (v0["prototype"]["am"] = d2,
    G0 = 30) : "Netscape" != l6["appName"] ? (v0["prototype"]["am"] = n2,
    G0 = 26) : (v0["prototype"]["am"] = a2,
    G0 = 28),
    v0["prototype"]["DB"] = G0,
    v0["prototype"]["DM"] = (1 << G0) - 1,
    v0["prototype"]["DV"] = 1 << G0;
    // v0 null v0
    function X2(object, y5X, u5X, H5X) {
        var o3q = 5;
        // 返回y5x  l5x 就是y5x
        var l5X = y5X["abs"]();
        if (o3q * (o3q + 1) * o3q % 2 == 0 && !(l5X["t"] <= 0)) {
            // object == K5x == H5X
            var K5X = object["abs"]();
            if (K5X["t"] < l5X["t"])
                return null != u5X && u5X["fromInt"](0),
                void (null != H5X && object["copyTo"](H5X));
            null == H5X && (H5X = i0());
            // 新建v0对象
            var J5X = i0()
              , t5X = 0
              , M5X = 0
              , m5X = object["DB"] - Z0(l5X[l5X["t"] - 1]);
            // m5x > 0 调用 m2(12, J5X)
            m5X > 0 ? (l5X["lShiftTo"](m5X, J5X),
            K5X["lShiftTo"](m5X, H5X)) : (l5X["copyTo"](J5X),
            K5X["copyTo"](H5X));
            var r5X = J5X["t"]
              , x5X = J5X[r5X - 1];
            if (0 != x5X) {
                var X5X = x5X * (1 << object["F1"]) + (r5X > 1 ? J5X[r5X - 2] >> object["F2"] : 0)
                  , Q5X = object["FV"] / X5X
                  , D5X = (1 << object["F1"]) / X5X
                  , o5X = 1 << object["F2"]
                  , T5X = H5X["t"]
                  , s5X = T5X - r5X
                  , L5X = null == u5X ? i0() : u5X;
                for (J5X["dlShiftTo"](s5X, L5X),
                H5X["compareTo"](L5X) >= 0 && (H5X[H5X["t"]++] = 1,
                H5X["subTo"](L5X, H5X)),
                v0["ONE"]["dlShiftTo"](r5X, L5X),
                L5X["subTo"](J5X, J5X); J5X["t"] < r5X; )
                    J5X[J5X["t"]++] = 0;
                for (; --s5X >= 0; ) {
                    var R5X = H5X[--T5X] == x5X ? object["DM"] : Math["floor"](H5X[T5X] * Q5X + (H5X[T5X - 1] + o5X) * D5X);
                    if ((H5X[T5X] += J5X["am"](0, R5X, H5X, s5X, 0, r5X)) < R5X)
                        for (J5X["dlShiftTo"](s5X, L5X),
                        H5X["subTo"](L5X, H5X); H5X[T5X] < --R5X; )
                            H5X["subTo"](L5X, H5X);
                }
                null != u5X && (H5X["drShiftTo"](r5X, u5X),
                t5X != M5X && v0["ZERO"]["subTo"](u5X, u5X)),
                H5X["t"] = r5X,
                H5X["clamp"](),
                m5X > 0 && H5X["rShiftTo"](m5X, H5X),
                t5X < 0 && v0["ZERO"]["subTo"](H5X, H5X);
            }
        }
    }
    // 随机数组w0清零
    function P2() {
        // U2 为 256
        var i9q = 1;
        if (null == z0) {
            // f2 新建W2 三个参数 原生属性Z2, N2
            for (z0 = f2(); V0 < U2; ) {
                var r6X = Math["floor"](65536 * Math["random"]());
                w0[V0++] = 255 & r6X;
            }
            for (z0["init"](w0),  //Z2(w0)  W2对象S数组 256个随机数
            V0 = 0; V0 < w0["length"]; ++V0)
                w0[V0] = 0;
            V0 = 0;
        }
        return z0["next"](); //调用 N2() 返回随机数
    }
    function q2(object) {
        for (var J4X = object["s"] & object["DM"]; (object["t"] > 0 && object[object["t"] - 1] == J4X); ) {
            --object["t"];
        }
    }
    function N2(object) {
        var J6X;
        return object["i"] = object["i"] + 1 & 255,
        object["j"] = object["j"] + object["S"][object["i"]] & 255,
        J6X = object["S"][object["i"]], //
        object["S"][object["i"]] = object["S"][object["j"]],
        object["S"][object["j"]] = J6X,
        object["S"][J6X + object["S"][object["i"]] & 255];
    }
    function W6X(object, t4X) {
        var K9q = 8;
        var b9q = 2;
        var M9q = 8;
        var x4X = object["s"] - t4X["s"];
        if (M9q * (M9q + 1) % 2 + 9 && 0 != x4X)
            return x4X;
        var X4X = object["t"];
        if (0 != (x4X = X4X - t4X["t"]))
            return object["s"] < 0 ? -x4X : x4X;
        for (; --X4X >= 0; ) {
            if (0 != (x4X = object[X4X] - t4X[X4X]))
                return x4X;
        }
        return 0;
    }
    // ******加密函数***** 16随机字符串和 128， 返回v0
    function v2(object, R3X, T3X) {
        var p3q = 9;
        var R3q = 2;
        var O3q = 10;
        if (T3X < R3X["length"] + 11)
            return console["error"]("Message too long for RSA"),
            null;
        // 把R3X字符串转为对应数字存入m3x数组中 数组总长度为T3X
        for (var m3X = [], x3X = R3X["length"] - 1; (x3X >= 0 && T3X > 0); ) {
            var s3X = R3X["charCodeAt"](x3X--);
            s3X < 128 ? m3X[--T3X] = s3X : s3X > 127 && s3X < 2048 ? (m3X[--T3X] = 63 & s3X | 128,
            m3X[--T3X] = s3X >> 6 | 192) : (m3X[--T3X] = 63 & s3X | 128,
            m3X[--T3X] = s3X >> 6 & 63 | 128,
            m3X[--T3X] = s3X >> 12 | 224);
        }
        m3X[--T3X] = 0;
        // new一个新对象c2 ,c2中nextbytes为z2
        //
        for (var X3X = new c2(), K3X = []; T3X > 2; ) {
            for (K3X[0] = 0; 0 == K3X[0]; )
                X3X["nextBytes"](K3X); // z2(K3x)
            m3X[--T3X] = K3X[0];
        }
        return m3X[--T3X] = 2,
        m3X[--T3X] = 0,
        new v0(m3X);
    }
    // 三个参数 i=0, j= 0, S=[]
    function W2(object) {
        object["i"] = 0,
        object["j"] = 0,
        object["S"] = [];
    }
    v0["prototype"]["FV"] = Math["pow"](2, 52),
    v0["prototype"]["F1"] = 52 - G0,
    v0["prototype"]["F2"] = 2 * G0 - 52;
    function Z0(Q4X) {
        var D4X, o4X = 1;
        return 0 != (D4X = Q4X >>> 16) && (Q4X = D4X,
        o4X += 16),
        0 != (D4X = Q4X >> 8) && (Q4X = D4X,
        o4X += 8),
        0 != (D4X = Q4X >> 4) && (Q4X = D4X,
        o4X += 4),
        0 != (D4X = Q4X >> 2) && (Q4X = D4X,
        o4X += 2),
        0 != (D4X = Q4X >> 1) && (Q4X = D4X,
        o4X += 1),
        o4X;
    }
    function i2(object,D3X) {
        return D3X["modPowInt"](object["e"], object["n"]);
    }
    function u2(object) {
        // object 是P0
        var X9q = 0;
        return object["t"] <= 0 && X9q * (X9q + 1) % 2 + 6 ? 0 : object["DB"] * (object["t"] - 1) + Z0(object[object["t"] - 1] ^ object["s"] & object["DM"]);
    }
    function i0() {
        return new v0(null);
    }
    function A2(object,r3X, J3X) {
        var n3q = 0;
        var L3X;
        return L3X = (r3X < 256 || J3X["isEven"]()) ? new F0(J3X) : new E0(J3X),
        object["exp"](r3X, L3X);
    }
    var n0, a0, H2 = "0123456789abcdefghijklmnopqrstuvwxyz", g0 = [];
    // go
    for (n0 = "0"["charCodeAt"](0),
    a0 = 0; T3q * (T3q + 1) * T3q % 2 == 0 && a0 <= 9; ++a0) {
        g0[n0++] = a0;
        T3q = T3q >= 66202 ? T3q / 4 : T3q * 4;
    }
    function n2(object,X6X, t6X, R6X, x6X, s6X, Q6X) {
        var e9q = 0;
        for (; --Q6X >= 0 && e9q * (e9q + 1) * e9q % 2 == 0; ) {
            var K6X = t6X * object[X6X++] + R6X[x6X] + s6X;
            s6X = Math["floor"](K6X / 67108864),
            R6X[x6X++] = 67108863 & K6X;
            e9q = e9q >= 57007 ? e9q - 1 : e9q + 1;
        }
        return s6X;
    }
    function I2(object,A5X, B5X) {
        A5X["squareTo"](B5X),
        object["reduce"](B5X);
    }
    for (n0 = "a"["charCodeAt"](0),
    a0 = 10; a0 < 36 && w3q * (w3q + 1) % 2 + 10; ++a0) {
        g0[n0++] = a0;
        w3q = w3q >= 27149 ? w3q / 3 : w3q * 3;
    }
    function F0(object,d5X) {
        object["m"] = d5X;
    }
    // 加密关键参数 n和e, 调用Y2,
    function V2(object,t3X, Q3X) {
        var i3q = 2;
        (null != t3X && null != Q3X && t3X["length"] > 0 && Q3X["length"] > 0) ? (object["n"] = Y2(t3X, 16), object["e"] = parseInt(Q3X, 16)) : console["error"]("Invalid RSA public key");
    }
    for (n0 = "A"["charCodeAt"](0),
    a0 = 10; E3q * (E3q + 1) * E3q % 2 == 0 && a0 < 36; ++a0) {
        g0[n0++] = a0;
        E3q = E3q > 64681 ? E3q / 4 : E3q * 4;
    }
    // 关键参数v0
    function w2(object,U4X, W4X) {
        var j9q = 0;
        var h9q = 6;
        var Z6X;
        if (16 == W4X)
            Z6X = 4;
        else if (8 == W4X)
            Z6X = 3;
        else if (256 == W4X)
            Z6X = 8;
        else if (2 == W4X)
            Z6X = 1;
        else if (32 == W4X)
            Z6X = 5;
        else {
            if (4 != W4X)
                return void object["fromRadix"](U4X, W4X);
            Z6X = 2;
        }
        object["t"] = 0,
        object["s"] = 0;
        // 4位， 调用L2
        for (var e4X = U4X["length"], H4X = !1, N6X = 0; --e4X >= 0; ) {
            var c4X = 8 == Z6X ? 255 & U4X[e4X] : L2(U4X, e4X);
            c4X < 0 ? "-" == U4X["charAt"](e4X) && (H4X = !0) : (H4X = !1,
            0 == N6X ? object[object["t"]++] = c4X : N6X + Z6X > object["DB"] ? (object[object["t"] - 1] |= (c4X & (1 << object["DB"] - N6X) - 1) << N6X,
            object[object["t"]++] = c4X >> object["DB"] - N6X) : object[object["t"] - 1] |= c4X << N6X,
            (N6X += Z6X) >= object["DB"] && (N6X -= object["DB"]));
        }
        8 == Z6X && 0 != (128 & U4X[0]) && (object["s"] = -1,
        N6X > 0 && (object[object["t"] - 1] |= (1 << object["DB"] - N6X) - 1 << N6X)),
        object["clamp"](), //q2
        H4X && v0["ZERO"]["subTo"](object, object);
    }
    // 返回this 函数
    function C2(object) {
        return  object["s"] < 0 ? object["negate"]() : object;
    }
    function b2(object) {
        var I3q = 8;
        return 0 == (object["t"] > 0  ? 1 & object[0] : object["s"]);
    }
    function k2(object,F5X) {
        var q3q = 4;
        var a3q = 4;
        for (; a3q * (a3q + 1) * a3q % 2 == 0 && F5X["t"] <= object["mt2"]; ) {
            F5X[F5X["t"]++] = 0;
            a3q = a3q > 64487 ? a3q / 8 : a3q * 8;
        }
        for (var q5X = 0; q5X < object["m"]["t"] && q3q * (q3q + 1) % 2 + 8; ++q5X) {
            var n5X = 32767 & F5X[q5X]
              , E5X = n5X * object["mpl"] + ((n5X * object["mph"] + (F5X[q5X] >> 15) * object["mpl"] & object["um"]) << 15) & F5X["DM"];
            for (n5X = q5X + object["m"]["t"],
            F5X[n5X] += object["m"]["am"](0, E5X, F5X, q5X, 0, object["m"]["t"]); F5X[n5X] >= F5X["DV"]; )
                F5X[n5X] -= F5X["DV"],
                F5X[++n5X]++;
            q3q = q3q > 43484 ? q3q - 9 : q3q + 9;
        }
        F5X["clamp"](),
        F5X["drShiftTo"](object["m"]["t"], F5X),
        F5X["compareTo"](object["m"]) >= 0 && F5X["subTo"](object["m"], F5X);
    }
    function a2(object,G6X, a6X, V6X, i6X, B6X, w6X) {
        var L9q = 1;
        for (var A6X = 16383 & a6X, Y6X = a6X >> 14; --w6X >= 0; ) {
            var S6X = 16383 & object[G6X]
              , v6X = object[G6X++] >> 14
              , b6X = Y6X * S6X + v6X * A6X;
            S6X = A6X * S6X + ((16383 & b6X) << 14) + V6X[i6X] + B6X,
            B6X = (S6X >> 28) + (b6X >> 14) + Y6X * v6X,
            V6X[i6X++] = 268435455 & S6X;
        }
        return B6X;
    }
    function r2(object) {
        var Q3q = 10;
        var s3q = 4;
        var g3q = 1;
        if (object["t"] < 1)
            return 0;
        var v5X = object[0];
        if (0 == (1 & v5X))
            return 0;
        var Y5X = 3 & v5X;
        return Y5X = Y5X * (2 - (15 & v5X) * Y5X) & 15,
        Y5X = Y5X * (2 - (255 & v5X) * Y5X) & 255,
        Y5X = Y5X * (2 - ((65535 & v5X) * Y5X & 65535)) & 65535,
        Y5X = Y5X * (2 - v5X * Y5X % object["DV"]) % object["DV"],
        Y5X > 0  ? object["DV"] - Y5X : -Y5X;
    }
    function G2(object, I3X) {
        var e3q = 4;
        var x3q = 8;
        var Y3q = 4;
        // object P0 ,I3X 16为随机字符串, 128   u2
        var y3X = v2(object, I3X, object["n"]["bitLength"]() + 7 >> 3);
        if (null == y3X && Y3q * (Y3q + 1) % 2 + 10)
            return null;
        var M3X = object["doPublic"](y3X);
        if (x3q * (x3q + 1) * x3q % 2 == 0 && null == M3X)
            return null;
        var o3X = M3X["toString"](16);
        return e3q * (e3q + 1) * e3q % 2 == 0 && 0 == (1 & o3X["length"]) ? o3X : "0" + o3X;
    }
    function j2(object,i5X) {
        var V5X = i0();
        return i5X["abs"]()["dlShiftTo"](object["m"]["t"], V5X),
        V5X["divRemTo"](object["m"], null, V5X),
        i5X["s"] < 0 && V5X["compareTo"](v0["ZERO"]) > 0 && object["m"]["subTo"](V5X, V5X),
        V5X;
    }
    function t2(object,p5X) {
        var I5X = i0();
        return object["abs"]()["divRemTo"](p5X, null, I5X),
        object["s"] < 0 && I5X["compareTo"](v0["ZERO"]) > 0 && p5X["subTo"](I5X, I5X),
        I5X;
    }
    // 12 ,新建v0对象
    function m2(object,A4X, k4X) {
        var F9q = 0;
        var d9q = 4;
        var h4X, S4X = A4X % object["DB"], B4X = object["DB"] - S4X, Y4X = (1 << B4X) - 1, O4X = Math["floor"](A4X / object["DB"]), b4X = object["s"] << S4X & object["DM"];
        for (h4X = object["t"] - 1; h4X >= 0; --h4X) {
            k4X[h4X + O4X + 1] = object[h4X] >> B4X | b4X,
            b4X = (object[h4X] & Y4X) << S4X;
        }
        for (h4X = O4X - 1; h4X >= 0; --h4X) {
            k4X[h4X] = 0;
        }
        k4X[O4X] = b4X,
        k4X["t"] = object["t"] + O4X + 1,
        k4X["s"] = object["s"],
        k4X["clamp"]();
    }
    function B2(object,W3X, U3X) {
        var D3q = 9;
        var f3q = 4;
        if ((W3X > 4294967295 || W3X < 1) && f3q * (f3q + 1) * f3q % 2 == 0)
            return v0["ONE"];
        var N5X = i0()
          , Z5X = i0()
          , c3X = U3X["convert"](object)
          , e3X = Z0(W3X) - 1;
        for (c3X["copyTo"](N5X); D3q * (D3q + 1) % 2 + 1 && --e3X >= 0; ) {
            if (U3X["sqrTo"](N5X, Z5X),
            (W3X & 1 << e3X) > 0)
                U3X["mulTo"](Z5X, c3X, N5X);
            else {
                var H3X = N5X;
                N5X = Z5X,
                Z5X = H3X;
            }
            D3q = D3q > 60361 ? D3q / 4 : D3q * 4;
        }
        return U3X["revert"](N5X);
    }
    function c2() {}
    // new一个v0对象， RSA, 16
    function Y2(u3X, l3X) {
        return new v0(u3X,l3X);
    }
    return F0["prototype"]["convert"] = D2,
    F0["prototype"]["revert"] = o2,
    F0["prototype"]["reduce"] = y2,
    F0["prototype"]["mulTo"] = M2,
    F0["prototype"]["sqrTo"] = I2,
    E0["prototype"]["convert"] = j2,
    E0["prototype"]["revert"] = h2,
    E0["prototype"]["reduce"] = k2,
    E0["prototype"]["mulTo"] = S2,
    E0["prototype"]["sqrTo"] = O2,
    v0["prototype"]["copyTo"] = Q2,
    v0["prototype"]["fromInt"] = p2,
    v0["prototype"]["fromString"] = w2,
    v0["prototype"]["clamp"] = q2,
    v0["prototype"]["dlShiftTo"] = l2,
    v0["prototype"]["drShiftTo"] = T2,
    v0["prototype"]["lShiftTo"] = m2,
    v0["prototype"]["rShiftTo"] = s2,
    v0["prototype"]["subTo"] = K2,
    v0["prototype"]["multiplyTo"] = R2,
    v0["prototype"]["squareTo"] = x2,
    v0["prototype"]["divRemTo"] = X2,
    v0["prototype"]["invDigit"] = r2,
    v0["prototype"]["isEven"] = b2,
    v0["prototype"]["exp"] = B2,
    v0["prototype"]["toString"] = E2,
    v0["prototype"]["negate"] = g2,
    v0["prototype"]["abs"] = C2,
    v0["prototype"]["compareTo"] = W6X,
    v0["prototype"]["bitLength"] = u2,
    v0["prototype"]["mod"] = t2,
    v0["prototype"]["modPowInt"] = A2,
    v0["ZERO"] = J2(window, 0),
    v0["ONE"] = J2(window, 1),
    P0["prototype"]["doPublic"] = i2,
    P0["prototype"]["setPublic"] = V2,
    P0["prototype"]["encrypt"] = G2,
    P0;
}();