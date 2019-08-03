# geetest-v2
滑动验证码 纯python实现 如果对你有用给个star哦🌟


w参数破解：💗AES(JSON.stringify(Z9S)) + RSA()💗

    

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
![运行结果](/bibibi/result.png)  
本代码库提供的轨迹可能forbidden，不是全部有效。

### 第一种方法可自行修改trace.py文件的轨迹生成函数。  
轨迹是一个[[x, y,t],[x2, y2, t2]...]的数组。自己构造轨迹函数时需要注意以下几点
- 第一组数组[-x, -y, 0] 前两个值为负值，大概在-15到-25之间
- 第二组数组[0, 0, 0]
- 每一组的最后一个元素是t，是递增的。
- x是拖动距离（0~distance），随机值，但是最后一个数组元素[x, y, t] x为缺口距离distance，t为通过时间passtime
- y是拖动过程中鼠标上下波动。在[-3, 3]之间

### 第二种方法 手动滑动滑块，把你手动滑动的滑块数据记录下来取代文件中的数据。
- [	点击这里](https://github.com/Kevin-Cherish/geetest/issues/3)

## 联系我
- 欢迎反馈！
- My Email : cherish_kevin@163.com  

## 注意：
- 本项目仅用于学习和交流
> 欢迎任何人参与和完善：一个人可以走的很快，但是一群人却可以走的更远
