#### node是什么？
Node.js 是基于 V8 JavaScript 引擎 构建的 JavaScript 运行时。
[node中文api官网](https://nodejs.cn/api/documentation.html)

#### npm镜像设置
`npm config set registry https://regisity.npm.taobao.org/`

npm 官方原始镜像网址是：https://registry.npmjs.org/ 
淘宝 NPM 镜像：http://registry.npmmirror.com 
阿里云 NPM 镜像：https://npm.aliyun.com 
腾讯云 NPM 镜像：https://mirrors.cloud.tencent.com/npm/ 
华为云 NPM 镜像：https://mirrors.huaweicloud.com/repository/npm/ 
网易 NPM 镜像：https://mirrors.163.com/npm/ 
中国科学技术大学开源镜像站：http://mirrors.ustc.edu.cn/ 
清华大学开源镜像站：https://mirrors.tuna.tsinghua.edu.cn/ 


#### yrm镜像包管理
yrm是一个管理npm/pnpm/yarn等包管理器的镜像源工具，你可以通过yrm很方便的更改下载镜像源。
使用`npm install -g yrm`全局安装。

```
(base) C:\Users\EDY\Desktop\program\blog>yrm ls    

  npm ---- https://registry.npmjs.org/
  cnpm --- http://r.cnpmjs.org/
* taobao - https://registry.npm.taobao.org/
  nj ----- https://registry.nodejitsu.com/
  rednpm - http://registry.mirror.cqupt.edu.cn/
  npmMirror  https://skimdb.npmjs.com/registry/
  edunpm - http://registry.enpmjs.org/
  yarn --- https://registry.yarnpkg.com
  aliyun - https://maven.aliyun.com/nexus/content/groups/public/
```

#### node运行时require与vue项目import
在es6之前js一直没有自己的模块语法，为了解决这种尴尬就有了require.js的出现。在es6发布之后js又引入了import的概念

区别：require 是赋值过程并且是运行时才执行， import 是解构过程并且是编译时执行。require可以理解为一个全局方法，所以它甚至可以进行下面这样的骚操作，是一个方法就意味着可以在任何地方执行。而import必须写在文件的顶部。

**require核心概念**：在导出的文件中定义module.export,导出的对象的类型不予限定（可以是任何类型，字符串，变量，对象，方法），在引入的文件中调用require()方法引入对象即可。

代码示例：
```
//a.js中
module.export = {
    a: function(){
     console.log(666)
  }
}

//b.js中
var obj = require('../a.js')
obj.a()  //666
注: 本质上是将要导出的对象赋值给module这个的对象的export属性，在其他文件中通过require这个方法访问该属性
```

**import核心概念**：导出的对象必须与模块中的值一一对应，换一种说法就是导出的对象与整个模块进行**解构赋值**。

代码示例：
```
//a.js中
export default{    //（最常使用的方法,加入default关键字代表在import时可以使用任意变量名并且不需要花括号{}）
     a: function(){
         console.log(666)
   }
}
 
export function(){  //导出函数
 
}
 
export {newA as a ,b,c}  //  解构赋值语法(as关键字在这里表示将newA作为a的数据接口暴露给外部，外部不能直接访问a)
 
//b.js中
import  a  from  '...'  //import常用语法（需要export中带有default关键字）可以任意指定import的名称
 
import {...} from '...'  // 基本方式，导入的对象需要与export对象进行解构赋值。
 
import a as biubiubiu from '...'  //使用as关键字，这里表示将a代表biubiubiu引入（当变量名称有冲突时可以使用这种方式解决冲突）
 
import {a as biubiubiu,b,c}  //as关键字的其他使用方法
```

#### node的websocket
node运行时没有自带的ws库，需要借助第三方模块WebSocket-Node或ws

1. 使用npm命令安装`npm install websocket`
[WebSocket-Node网站](https://github.com/theturtle32/WebSocket-Node)

2. 使用npm命令安装`npm install ws`
[ws网站](https://github.com/websockets/ws)


#### websocket与socket.io
websocket与socket.io容易混淆。虽然socket.io和WebSocket都支持实时通信，但是它们并不能混用。

Socket.io不是Websocket，它只是将Websocket和轮询 （Polling）机制以及其它的实时通信方式封装成了通用的接口，并且在服务端实现了这些实时机制的相应代码。也就是说，**Websocket仅仅是 Socket.io实现实时通信的一个子集**。因此Websocket客户端连接不上Socket.io服务端，当然Socket.io客户端也连接不上Websocket服务端。