# IPsec(Internet Protocol Security, 网际协议安全)

IPsec是为IP网络提供安全性的协议和服务的集合, 常用于 VPN(Virtual Private Network，虚拟专用网)中.

由于IP报文本身没有集成任何安全特性, IP数据包在公用网络如Internet中传输可能会面临被伪造、窃取或篡改的风险。通信双方通过IPsec建立一条IPsec隧道，IP数据包通过IPsec隧道进行加密传输，有效保证了数据在不安全的网络环境如Internet中传输的安全性。

## 工作原理

IPsec的工作原理大致可以分为4个阶段:

1. 识别"感兴趣流"(及需要通过 `IPsec` 隧道的数据帧): 网络设备接收到报文后, 通常会将报文的五元组等信息和`IPsec策略`进行匹配来判断报文是否要通过`IPsec隧道`传输, 需要通过`IPsec隧道`传输的流量通常被称为"感兴趣流"
2. `协商安全联盟(Security Association，以下简称SA)`: SA是通信双方对某些协商要素的约定，比如双方使用的安全协议、数据传输采用的封装模式、协议采用的加密和验证算法、用于数据传输的密钥等，通信双方之间只有建立了SA，才能进行安全的数据传输。
> 识别出感兴趣流后，本端网络设备会向对端网络设备发起`SA协商`。在这一阶段，通信双方之间通过`IKE协议`先协商建立`IKE SA(用于身份验证和密钥信息交换)`，然后在`IKE SA`的基础上协商建立`IPsec SA(用于数据安全传输)`。
3. 数据传输: `IPsec SA`建立成功后，双方就可以通过`IPsec隧道`传输数据了。
> IPsec为了保证数据传输的安全性, 在这一阶段需要通过`AH/ESP协议`对数据进行加密和验证。加密机制保证了数据的机密性, 防止数据在传输过程中被窃取; 验证机制保证了数据的真实可靠, 防止数据在传输过程中被仿冒和篡改。(加密和验证均采用对称密钥)
4. 隧道拆除: 通常情况下，通信双方之间的会话老化(连接断开)即代表通信双方数据交换已经完成，因此为了节省系统资源，通信双方之间的隧道在空闲时间达到一定值后会自动删除。

## 使用协议

`IKE(Internet Key Exchange, 因特网密钥交换)`/`AH(Authentication Header, 认证头)`/`ESP(Encapsulating Security Payload, 封装安全载荷)`

- `LKE`: 基于UDP的应用层协议，它主要用于SA协商和密钥管理。
> `IKE协议`属于一种混合型协议，它综合了`ISAKMP(Internet Security Association and Key Management Protocol)`、`Oakley协议`和`SKEME协议`这三个协议。其中，`ISAKMP`定义了`IKE SA`的建立过程，`Oakley和SKEME协议`的核心是`DH(Diffie-Hellman)`算法，主要用于在Internet上安全地分发密钥、验证身份，以保证数据传输的安全性。`IKE SA`和`IPsec SA`需要的加密密钥和验证密钥都是通过DH算法生成的，它还支持密钥动态刷新
- `AH`: AH协议用来对IP报文进行数据源认证和完整性校验, 即用来保证传输的IP报文的来源可信和数据不被篡改, 但它并不提供加密功能。
> AH协议在每个数据包的标准IP报文头后面添加一个AH报文头，AH协议对报文的完整性校验的范围是整个IP报文。
- `ESP`: ESP协议除了对IP报文进行数据源认证和完整性校验以外，还能对数据进行加密。
> ESP协议在每一个数据包的标准IP报头后方添加一个ESP报文头，并在数据包后方追加一个ESP尾(ESP Trailer和ESP Auth data)。ESP协议在传输模式下的数据完整性校验范围不包括IP头，因此它不能保证IP报文头不被篡改。

## 使用端口
`IPsec`中`IKE协议`采用`UDP 500`端口发起和响应协商，因此为了使`IKE协商报文`顺利通过网关设备，通常要在网关设备上配置安全策略放开`UDP 500`端口。另外，在`IPsec NAT`穿越场景下，还需要放开`UDP 4500`端口。
