<h1 align='center'>Vitesse-Python</h1>

<p align='center'>
Mocking up web app with <b>Vitesse</b><sup><em>(speed)</em></sup><br>
</p>

<br>


<br>

<p align='center'>
<b>简体中文</b> | <a href="">English</a>
<!-- Contributors: Thanks for getting interested, however we DON'T accept new transitions to the README, thanks. -->
</p>

<br>

## Introduction

### 👀 `Vitesse-Python` 

- Vitesse-Python 帮助您构建 windows 平台客户端的应用，不再受pyqt的困扰。
- Vitesse-Python 的视图层采用 HTML+JS+CSS，业务层采用本地 Python。
- Vitesse-Python 采用了 Vite 的开发模式，支持热更新，开发体验更佳。
- Vitesse-Python 采用了 PyInstaller 打包，支持 windows 平台，打包体积更小。
- Vitesse-Python 采用了 pywebview 作为渲染引擎，支持 windows 平台，渲染速度更快。
- Vitesse-Python 采用了 Vue3、Vitesse 作为前端框架，代码编写更优雅从容。

### 📦 适用场景

- 对软件的用户界面有一定美感要求
- 需要用到 Python 中的人工智能等模块
- 考虑搭建本地应用，使用本机计算和存储资源
- 对软件功能要求比较高，需要自己开发

### 👨‍💻 适用人群

- 熟悉 Vue3 和 Python 编程的程序员。
- 熟悉 HTML、CSS、JS 的前端工程师。
- 熟悉 Python 的数据分析师。
- 熟悉 Python 的机器学习工程师。
- 熟悉 Python 的人工智能工程师。
- 熟悉 Python 的软件工程师。

## Features

- ⚡️ [Vue 3](https://github.com/vuejs/core), [Vite 3](https://github.com/vitejs/vite), [pnpm](https://pnpm.io/), [ESBuild](https://github.com/evanw/esbuild) - born with fastness

- 🗂 [File based routing](./src/pages)

- 📦 [Components auto importing](./src/components)

- 🍍 [State Management via Pinia](https://pinia.vuejs.org/)

- 📑 [Layout system](./src/layouts)

- 📲 [PWA](https://github.com/antfu/vite-plugin-pwa)

- 🎨 [UnoCSS](https://github.com/antfu/unocss) - the instant on-demand atomic CSS engine

- 😃 [Use icons from any icon sets with classes](https://github.com/antfu/unocss/tree/main/packages/preset-icons)

- 🌍 [I18n ready](./locales)

- 🔎 [Component Preview](https://github.com/johnsoncodehk/vite-plugin-vue-component-preview)

- 🗒 [Markdown Support](https://github.com/antfu/vite-plugin-vue-markdown)

- 🔥 Use the [new `<script setup>` syntax](https://github.com/vuejs/rfcs/pull/227)

- 🤙🏻 [Reactivity Transform](https://vuejs.org/guide/extras/reactivity-transform.html) enabled

- 📥 [APIs auto importing](https://github.com/antfu/unplugin-auto-import) - use Composition API and others directly

- 🖨 Static-site generation (SSG) via [vite-ssg](https://github.com/antfu/vite-ssg)

- 🦔 Critical CSS via [critters](https://github.com/GoogleChromeLabs/critters)

- 🦾 TypeScript, of course

- ☁️ Deploy on Netlify, zero-config

- 🎉 <strong>[Pywebview](https://pywebview.flowrl.com/) inside </strong>

<br>


## Try it now!

> Vitesse-Python requires Node >=14.18 & Python >=3.7

```bash

### GitHub Template

[Create a repo from this template on GitHub](https://github.com/MarleneJiang/vitesse-python).

### Clone to local

If you prefer to do it manually with the cleaner git history

```bash
git clone https://github.com/MarleneJiang/vitesse-python.git
cd vitesse-python
pnpm inits # If you don't have pnpm installed, run: npm install -g pnpm
```

## Usage

### 开发前端

```bash
pnpm dev
```

### 开发软件

```bash
pnpm dev:app
```

### 整体开发

```bash
pnpm start
```

### 预打包，带console，方便输出日志信息

```bash
pnpm pre
```

### 预打包，带console，生成文件夹，仅win系统

```bash
pnpm pre:folder
```

### 正式打包，仅win系统

```bash
pnpm build
```

### 正式打包，生成文件夹，仅win系统

```bash
pnpm build:folder
```

## 高级用法

### 客户端引擎介绍

`Vitesse-Python` 基于 [pywebview](https://pywebview.flowrl.com) 构建客户端。而 pywebview 构架构建客户端的原理是利用本地电脑自带的浏览器引擎驱动，模拟生成客户端。本质上还是网页，或者说是一个浏览器，但是感官上和本地客户端没有差别。

那么，基于 pywebview 构架构建客户端的成败或质量，就与本地电脑的浏览器引擎息息相关了。

##### windows 系统

在 windows 系统上，大体上分为两类客户端引擎：正常模式和兼容模式。`Vitesse-Python` 仅支持正常模式。

- 正常模式

正常模式下，按照 edgechromium ，edgehtml， mshtml 的客户端引擎依次检索。如果本地电脑 edge 浏览器支持这些引擎，则客户端可以正常启动。否则，请安装对应的 [EdgeWebView2Runtime](https://developer.microsoft.com/en-us/microsoft-edge/webview2/) 浏览器引擎。

- 兼容模式

如果本地电脑 edge 浏览器不支持这些引擎，同时也不想下载 [EdgeWebView2Runtime](https://developer.microsoft.com/en-us/microsoft-edge/webview2/) ，那么就可以使用兼容模式。兼容模式的原理就是利用 [CEFPython](https://github.com/cztomczak/cefpython)，嵌入 Chromium 的 Web 浏览器控件。也就是只要本地电脑安装了谷歌浏览器 V66 版及其以上版本，即可正常启动客户端。缺点就是生成的安装包体积会增加大约 60M 左右。


### 构建客户端 API

构建客户端的主程序是在 app 文件夹下的 main.py。 

main.py 里面主要是依靠 webview.create_window 和 webview.start 这两个 API 来构建客户端。其他的一些 API，可以直接查看 [pywebview 官网](https://pywebview.flowrl.com/guide/api.html) 了解详情。

#### webview.create_window

```
webview.create_window(title, url='', html='', js_api=None, width=800, height=600, \
                      x=None, y=None, resizable=True, fullscreen=False, \
                      min_size=(200, 100), hidden=False, frameless=False, \
                      minimized=False, on_top=False, confirm_close=False, \
                      background_color='#FFF')
```

创建一个新的 pywebview 窗口，并返回其实例。在开始 GUI 循环之前，窗口不会显示。

- **title** 窗口标题
- **url** 要加载的 URL。如果 URL 没有协议前缀，则将其解析为相对于应用程序入口点的路径。或者，可以传递 WSGI 服务器对象来启动本地 Web 服务器。
- **html** 要加载的 HTML 代码。如果同时指定了 URL 和 HTML，HTML 优先。
- **js_api** 将 python 对象暴露到当前 pywebview 窗口的 DOM 中。js_api 对象的方法可以通过调用 window.pywebview.api.<methodname>(<parameters>)从 Javascript 执行。请注意，调用 Javascript 函数会收到一个包含 python 函数的返回值。只有基本的 Python 对象（如 int、str、dict......）才能返回 Javascript。
- **width** 窗户宽度。默认值为 800px。
- **height** 窗户高度。默认值为 600px。
- **x** 窗口 x 坐标。默认值居中。
- **y** 窗口 y 坐标。默认值居中。
- **resizable** 是否可以调整窗口大小。默认值为 True
- **fullscreen** 从全屏模式开始。默认为 False
- **min_size** 指定最小窗口大小的（宽度、高度）元组。默认值为 200x100
- **hidden** 默认情况下创建一个隐藏的窗口。默认为 False
- **frameless** 创建一个无框窗口。默认值为 False。
- **minimized** 以最小化模式启动
- **on_top** 将窗口设置为始终位于其他窗口的顶部。默认值为 False。
- **confirm_close** 是否显示窗口关闭确认对话框。默认为 False
- **background_color** 加载 WebView 之前显示的窗口的背景颜色。指定为十六进制颜色。默认值为白色。
- **transparent** 创建一个透明的窗口。Windows 不支持。默认值为 False。请注意，此设置不会隐藏或使窗口铬透明。将窗口 chrome setframeless 隐藏为 True。

#### webview.start

```
webview.start(func=None, args=None, localization={}, gui=None, debug=False, http_server=False)
```

启动 GUI 循环并显示之前创建的窗口。此函数必须从主线程调用。

- **func** 启动 GUI 循环时调用的函数。
- **args** 函数参数。可以是单个值，也可以是元组值。
- **localization** 带有本地化字符串的词典。默认字符串及其键在 localization.py 中定义
- **gui** 强制使用特定的 GUI。允许的值是 cef、qt 或 gtk，具体取决于平台。
- **debug** 启用调试模式。
- **http_server** 启用内置 HTTP 服务器。如果启用，本地文件将使用随机端口上的本地 HTTP 服务器提供服务。对于每个窗口，都会生成一个单独的 HTTP 服务器。对于非本地 URL，此选项将被忽略。

### 域间通信

#### 从 Python 调用 Javascript

window.evaluate_js(code, callback=None)允许您使用同步返回的最后一个值执行任意 Javascript 代码。如果提供了回调函数，则解析 promise，并调用回调函数，结果作为参数。Javascript 类型转换为 Python 类型，例如 JS 对象到 Python 字典，数组到列表，未定义为 None。由于实现限制，字符串“null”将被计算为 None。另外，evaluate_js 返回的值限制为 900 个字符内。

#### 从 Javascript 调用 Python

从 Javascript 调用 Python 函数可以通过两种不同的方法完成。

- 通过将 Python 类的实例暴露给 create_window 的 js_api。该类的所有可调用方法都将以 pywebview.api.method_name 的形式公开到 JS 域中。方法名称不得以下划线开头。
- 通过将函数传递给窗口对象的 expose(func)这将以 pywebview.api.func_name 的形式将一个或多个函数公开到 JS 域。与 JS API 不同，expose 也允许在运行时公开函数。如果 JS API 和以这种方式公开的函数之间存在名称冲突，则后者优先。
