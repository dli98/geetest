from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii, json, os
import random
import hashlib
import rsa


class Encrypyed():
    def __init__(self):
        self.modulus = "00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81"
        self.pub_key = '10001'

    def encrypted_request(self, initData, userresponse, passtime, aa):
        # md5 加密
        hash = hashlib.md5()
        hash.update(bytes(initData['gt'], encoding='utf-8'))
        hash.update(bytes(initData['challenge'][0:32], encoding='utf-8'))
        hash.update(bytes(str(passtime), encoding='utf-8'))
        text = {
            "userresponse": userresponse,
            "passtime": passtime,
            "imgload": random.randint(100, 800),
            "aa": aa,
            "ep": {"v": "6.0.9"},
            'rp': hash.hexdigest()
        }
        text = json.dumps(text, separators=(',', ':'))
        sec_key = self.create_secret_key(8)
        # rsa 不对称性对 aes的密钥进行加密
        enc_sec_key = self.rsa_encrpt(sec_key, self.pub_key, self.modulus)

        # aes 对称加密  进行轨迹加密
        iv = b"0000000000000000"
        enc_text = self.aes_encrypt(text, sec_key.decode('utf-8'), iv)

        # base64 编码
        enc_text = self.b64encode(enc_text)

        data = {
            'gt': initData['gt'],
            'challenge': initData['challenge'],
            'w': enc_text + enc_sec_key,
            # 'callback': 'geetest_' + str(int(time.time() * 1000)),
        }
        return data

    def aes_encrypt(self, text, secKey, iv, style='pkcs7'):
        """
        :param text: 文本
        :param secKey: 密钥
        :param iv: 初始iv  bytes
        :param style: 返回函数类型
        :return:
        """
        encryptor = AES.new(secKey.encode('utf-8'), AES.MODE_CBC, iv)
        pad_pkcs7 = pad(text.encode('utf-8'), AES.block_size, style=style)
        ciphertext = encryptor.encrypt(pad_pkcs7)
        return ciphertext

    def rsa_encrpt(self, text, pubKey, modulus):
        '''
        对text 进行rsa加密   # reverseText^pubKey%modulus
        '''
        PublicKey = rsa.PublicKey(int(modulus, 16), int(pubKey, 16))  # rsa库公钥形式
        rs = rsa.encrypt(text, PublicKey)
        return rs.hex()

    def create_secret_key(self, size):
        # 作用是返回的二进制数据的十六进制表示。每一个字节的数据转换成相应的2位十六进制表示
        return binascii.hexlify(os.urandom(size))

    def b64encode(self, s):

        def separate_24_to_6(n, base):
            res = 0
            for i in range(24, -1, -1):
                if base >> i & 1 == 1:
                    res = (res << 1) + (n >> i & 1)
            return res

        base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()"
        r = ""
        p = ""
        c = len(s) % 3
        if c > 0:
            for _ in range(c, 3):
                p += '.'
                s += b'\0'

        for c in range(0, len(s), 3):

            # we add newlines after every 76 output characters, according to the MIME specs
            # if c > 0 and (c / 3 * 4) % 76 == 0:
            #     r += "\r\n"

            # these three 8-bit (ASCII) characters become one 24-bit number
            n = (s[c] << 16) + (s[c + 1] << 8) + (s[c + 2])

            # this 24-bit number gets separated into four 6-bit numbers
            # n = [n >> 18 & 63, n >> 12 & 63, n >> 6 & 63, n & 63]

            n = [separate_24_to_6(n, base) for base in [7274496, 9483264, 19220, 235]]

            r += base64chars[n[0]] + base64chars[n[1]] + base64chars[n[2]] + base64chars[n[3]]

        # add the actual padding string, after removing the zero pad
        return r[0: len(r) - len(p)] + p


if __name__ == '__main__':
    ep = Encrypyed()
    array = b"\xba\x93ufv\x97\xffjw\x89l\xc9\x87/\xfcv#\xf6\xc7 \xb7\x0c\xf8\x02\xdb\xe7\\6k\xf3\xf5\xf8\xea\xfb\xed\xe22\xc8\x13\xa2\xe7\x05I\xa7\xbcM\xf0qC\x19/:4\x91\xb2\xfa\xb7\xc1-\xb3\xcc[\x1e_\x18\xd8\xff\xe0\\G`Hsf\xb3\x86#\xc4b'n\x95\xf0\x0b\x0e\x87\x95\xb85\x08=t\x83\xc6Mh4\xbc\xac\xf3\xc6uo!*\xda\x19\x1eDR\xberr\xdfK\xad\xb1\xb7C\r\xb5\xb1\x0cC\x90\xf3W\x90\x14\x95\xe7\xc4B\xfa\xf3\xd6\xf3\x98\xdc\xd6u\x13\x80\xa5lu\x89\xf6E4\xba\xe4f\xa22\x91\x97/\xf4>x\xb3\xf5\x7fn\x83]7\x1e\xaf\xb1\x0cKU\xa18\xa0q\x9cbT\x985\xa8\xba\xab\x06zY.\x1f\x8f\xe3\xdb+L\xd0\xeb\xc3@c\xcd\x96\xebU\x02\x9c\xa5y\xa2\x96\xc3\x03\x01\xdd}\xc4\x08\xa42\xafZ)J\x11\x04\x17\x1b|\xe3\x12\xf5\xeeg\x91:\xa4\xa2\xb0U\xd0\xab5\xc4>\x99b&\xe0 \x1d\xad\xf9\x9b:\x9aX\xfa&\x04$B\xe8\x04\xfa(u@\xb7Q\x98\xd9\x9e\x99\x87C\n\x84\xf4T\x9e\x82(L|\xbaB\xda\xd1\xfa\xb5y\xab\x15\x07^\xe79\xb8#\xdfl,\xc9NYG\x9c\xaf\x84\xcf\xc3\x04m\xf2k\n\x8e\x16\xdd\x1e\xfe7\xa7W\x10\x80\x1a\xfb\xf4\x06\xadRf\xbe3R\\\xcc\x13\xed%\xff\x8b\x16\xb1a\x07\xfaJ\xe7\xd6"
    print(ep.b64encode(array))
