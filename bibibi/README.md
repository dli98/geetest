# geetest-v2
滑动验证码 纯python实现


w参数破解：<font color=red>AES(JSON.stringify(Z9S)) + RSA()</font>
    

发送方创建一个AES私钥，并对这个私钥通过RSA进行加密。  
## 文件说明
trace.py 轨迹  
run.py 主程序  
decrypt.py 解密模块


## **RSA**：
- n : "00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81"
- e : "10001"
- pkcs1 pad



## 轨迹数组[[x, y, t]...]
- x 
- y
- t 拖动滑块时间

## JSON字符串
- userresponse: function(distance， challege)
- aa: function(轨迹数组arr，s) 
- passtime: 轨迹数组[-1][-1]
- imgload : 图片加载时间，随机值
- ep : 版本号
- rp : MD5(gt, challenge, passtime)


## AES:
- 随机创建128bit的密钥
- JSon字符串
- 初始iv 0000000000000000
- pkcs7 pad


## 运行结果
![运行结果](bibibi/result.png)  
轨迹forbidden，可自行修改trace.py文件。
