#### element-plus组件与vue3
1. element-plus是一个vue3的UI框架。[element-plus官网](https://element-plus.org/zh-CN/component "打开官方网站")
2. vue3是一款用于构建用户界面的 JavaScript 框架。[vue3 api文档](https://cn.vuejs.org/api/composition-api-dependency-injection.html)
[vue3 组件文档](https://cn.vuejs.org/guide/typescript/composition-api.html#typing-component-emits)

### vue使用实例

#### vue父子组件传值
常见的父组件向子组件传值，一般是通过钩子props进行。vue3规定该传值方向一般是单向的。如果你需要在子组件中向父组件传值，一般可以通过组件事件实现。

#### axios设置默认请求前缀

axios.defaults.baseURL = "<url>"

#### vue项目配置websocket代理
**注意**：如果你使用浏览器api的websocket，那么在创建客户端连接时需要指定你前端部署的服务器地址和相应开放端口，（即使你的node或nginx未配置websocket服务端）
axios如果未指定ip，发起连接时默认向自身服务请求。所有我们使用axios时可以不指定具体的ip地址（即不设置axios的defaultURL），代理会自动帮我们将连接定向到目标target指定服务地址
```
//vite.config.js文件中
  server: {
    host: "0.0.0.0",
    proxy: {
      "/api": {
        target: "http://172.17.0.2:8000",
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
      "/ws":{
        target: "ws://172.17.0.2:8000",
        changeOrigin: true,
        ws: true,
        rewrite: (path) => path.replace(/^\/ws/, ""),
      },
    },
  },
```

#### vue3 + vite 配置环境变量，区分生产和测试环境

1. 首先在项目最外层目录新建.env[mode]文件
在对应的环境文件中配置环境参数，需要加上VITE_前缀才能在后续读取

// 在.env.development/.env.production 文件中配置 `VITE_BASE_URL=https://hhh.com `

2. 在package.json文件的启动命令上加上--mode [mode]，vite指令默认测试环境，vite build默认构建生产环境

```
 "scripts": {
    "dev": "vite",
    "dev:prod": "vite --mode production",
    "build": "vite build --mode development",
    "build:prod": "vite build --mode production"
  }

```
3. 如果要在项目中获取在.env中配置的环境参数使用import.meta[参数名]

`const baseUrl = import.meta.env.VITE_BASE_URL // VITE_BASE_URL需要配置在当前运行的环境文件中`

4. vite默认不加载.env文件，会在执行完vite配置后才确定加载哪个，如果需要在vite.config.js中读取参数值，需要以下操作，通过
`const env = loadEnv(mode, process.cwd(), '')`获取.env信息

```
import { defineConfig, loadEnv } from 'vite'

export default defineConfig(({ command, mode }) => {
  // 根据当前工作目录中的 `mode` 加载 .env 文件
  // 设置第三个参数为 '' 来加载所有环境变量，而不管是否有 `VITE_` 前缀。
  const env = loadEnv(mode, process.cwd(), '')
  return {
    // vite 配置
    define: {
      __APP_ENV__: env.APP_ENV,
    },
  }
```
5. 配置快捷目录

如果试用的是vue3官方推荐的脚手架生成，则会自带该配置，后续可以通过@访问src文件夹
```
import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'

export default defineConfig({
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
```