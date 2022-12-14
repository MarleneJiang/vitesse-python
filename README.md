<h1 align='center'>Vitesse-Python</h1>

<p align='center'>
Mocking up web app with <b>Vitesse</b><sup><em>(speed)</em></sup><br>
</p>

<br>


<br>

<p align='center'>
<b>ç®ä½ä¸­æ</b> | <a href="">English</a>
<!-- Contributors: Thanks for getting interested, however we DON'T accept new transitions to the README, thanks. -->
</p>

<br>

## Introduction

### ð `Vitesse-Python` 

- Vitesse-Python å¸®å©æ¨æå»º windows å¹³å°å®¢æ·ç«¯çåºç¨ï¼ä¸ååpyqtçå°æ°ã
- Vitesse-Python çè§å¾å±éç¨ HTML+JS+CSSï¼ä¸å¡å±éç¨æ¬å° Pythonã
- Vitesse-Python éç¨äº Vite çå¼åæ¨¡å¼ï¼æ¯æç­æ´æ°ï¼å¼åä½éªæ´ä½³ã
- Vitesse-Python éç¨äº PyInstaller æåï¼æ¯æ windows å¹³å°ï¼æåä½ç§¯æ´å°ã
- Vitesse-Python éç¨äº pywebview ä½ä¸ºæ¸²æå¼æï¼æ¯æ windows å¹³å°ï¼æ¸²æéåº¦æ´å¿«ã
- Vitesse-Python éç¨äº Vue3ãVitesse ä½ä¸ºåç«¯æ¡æ¶ï¼ä»£ç ç¼åæ´ä¼éä»å®¹ã

### ð¦ éç¨åºæ¯

- å¯¹è½¯ä»¶çç¨æ·çé¢æä¸å®ç¾æè¦æ±
- éè¦ç¨å° Python ä¸­çäººå·¥æºè½ç­æ¨¡å
- èèæ­å»ºæ¬å°åºç¨ï¼ä½¿ç¨æ¬æºè®¡ç®åå­å¨èµæº
- å¯¹è½¯ä»¶åè½è¦æ±æ¯è¾é«ï¼éè¦èªå·±å¼å

### ð¨âð» éç¨äººç¾¤

- çæ Vue3 å Python ç¼ç¨çç¨åºåã
- çæ HTMLãCSSãJS çåç«¯å·¥ç¨å¸ã
- çæ Python çæ°æ®åæå¸ã
- çæ Python çæºå¨å­¦ä¹ å·¥ç¨å¸ã
- çæ Python çäººå·¥æºè½å·¥ç¨å¸ã
- çæ Python çè½¯ä»¶å·¥ç¨å¸ã

## Features

- â¡ï¸ [Vue 3](https://github.com/vuejs/core), [Vite 3](https://github.com/vitejs/vite), [pnpm](https://pnpm.io/), [ESBuild](https://github.com/evanw/esbuild) - born with fastness

- ð [File based routing](./src/pages)

- ð¦ [Components auto importing](./src/components)

- ð [State Management via Pinia](https://pinia.vuejs.org/)

- ð [Layout system](./src/layouts)

- ð² [PWA](https://github.com/antfu/vite-plugin-pwa)

- ð¨ [UnoCSS](https://github.com/antfu/unocss) - the instant on-demand atomic CSS engine

- ð [Use icons from any icon sets with classes](https://github.com/antfu/unocss/tree/main/packages/preset-icons)

- ð [I18n ready](./locales)

- ð [Component Preview](https://github.com/johnsoncodehk/vite-plugin-vue-component-preview)

- ð [Markdown Support](https://github.com/antfu/vite-plugin-vue-markdown)

- ð¥ Use the [new `<script setup>` syntax](https://github.com/vuejs/rfcs/pull/227)

- ð¤ð» [Reactivity Transform](https://vuejs.org/guide/extras/reactivity-transform.html) enabled

- ð¥ [APIs auto importing](https://github.com/antfu/unplugin-auto-import) - use Composition API and others directly

- ð¨ Static-site generation (SSG) via [vite-ssg](https://github.com/antfu/vite-ssg)

- ð¦ Critical CSS via [critters](https://github.com/GoogleChromeLabs/critters)

- ð¦¾ TypeScript, of course

- âï¸ Deploy on Netlify, zero-config

- ð <strong>[Pywebview](https://pywebview.flowrl.com/) inside </strong>

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

### å¼ååç«¯

```bash
pnpm dev
```

### å¼åè½¯ä»¶

```bash
pnpm dev:app
```

### æ´ä½å¼å

```bash
pnpm start
```

### é¢æåï¼å¸¦consoleï¼æ¹ä¾¿è¾åºæ¥å¿ä¿¡æ¯

```bash
pnpm pre
```

### é¢æåï¼å¸¦consoleï¼çææä»¶å¤¹ï¼ä»winç³»ç»

```bash
pnpm pre:folder
```

### æ­£å¼æåï¼ä»winç³»ç»

```bash
pnpm build
```

### æ­£å¼æåï¼çææä»¶å¤¹ï¼ä»winç³»ç»

```bash
pnpm build:folder
```

## é«çº§ç¨æ³

### å®¢æ·ç«¯å¼æä»ç»

`Vitesse-Python` åºäº [pywebview](https://pywebview.flowrl.com) æå»ºå®¢æ·ç«¯ãè pywebview ææ¶æå»ºå®¢æ·ç«¯çåçæ¯å©ç¨æ¬å°çµèèªå¸¦çæµè§å¨å¼æé©±å¨ï¼æ¨¡æçæå®¢æ·ç«¯ãæ¬è´¨ä¸è¿æ¯ç½é¡µï¼æèè¯´æ¯ä¸ä¸ªæµè§å¨ï¼ä½æ¯æå®ä¸åæ¬å°å®¢æ·ç«¯æ²¡æå·®å«ã

é£ä¹ï¼åºäº pywebview ææ¶æå»ºå®¢æ·ç«¯çæè´¥æè´¨éï¼å°±ä¸æ¬å°çµèçæµè§å¨å¼ææ¯æ¯ç¸å³äºã

##### windows ç³»ç»

å¨ windows ç³»ç»ä¸ï¼å¤§ä½ä¸åä¸ºä¸¤ç±»å®¢æ·ç«¯å¼æï¼æ­£å¸¸æ¨¡å¼åå¼å®¹æ¨¡å¼ã`Vitesse-Python` ä»æ¯ææ­£å¸¸æ¨¡å¼ã

- æ­£å¸¸æ¨¡å¼

æ­£å¸¸æ¨¡å¼ä¸ï¼æç§ edgechromium ï¼edgehtmlï¼ mshtml çå®¢æ·ç«¯å¼æä¾æ¬¡æ£ç´¢ãå¦ææ¬å°çµè edge æµè§å¨æ¯æè¿äºå¼æï¼åå®¢æ·ç«¯å¯ä»¥æ­£å¸¸å¯å¨ãå¦åï¼è¯·å®è£å¯¹åºç [EdgeWebView2Runtime](https://developer.microsoft.com/en-us/microsoft-edge/webview2/) æµè§å¨å¼æã

- å¼å®¹æ¨¡å¼

å¦ææ¬å°çµè edge æµè§å¨ä¸æ¯æè¿äºå¼æï¼åæ¶ä¹ä¸æ³ä¸è½½ [EdgeWebView2Runtime](https://developer.microsoft.com/en-us/microsoft-edge/webview2/) ï¼é£ä¹å°±å¯ä»¥ä½¿ç¨å¼å®¹æ¨¡å¼ãå¼å®¹æ¨¡å¼çåçå°±æ¯å©ç¨ [CEFPython](https://github.com/cztomczak/cefpython)ï¼åµå¥ Chromium ç Web æµè§å¨æ§ä»¶ãä¹å°±æ¯åªè¦æ¬å°çµèå®è£äºè°·æ­æµè§å¨ V66 çåå¶ä»¥ä¸çæ¬ï¼å³å¯æ­£å¸¸å¯å¨å®¢æ·ç«¯ãç¼ºç¹å°±æ¯çæçå®è£åä½ç§¯ä¼å¢å å¤§çº¦ 60M å·¦å³ã


### æå»ºå®¢æ·ç«¯ API

æå»ºå®¢æ·ç«¯çä¸»ç¨åºæ¯å¨ app æä»¶å¤¹ä¸ç main.pyã 

main.py éé¢ä¸»è¦æ¯ä¾é  webview.create_window å webview.start è¿ä¸¤ä¸ª API æ¥æå»ºå®¢æ·ç«¯ãå¶ä»çä¸äº APIï¼å¯ä»¥ç´æ¥æ¥ç [pywebview å®ç½](https://pywebview.flowrl.com/guide/api.html) äºè§£è¯¦æã

#### webview.create_window

```
webview.create_window(title, url='', html='', js_api=None, width=800, height=600, \
                      x=None, y=None, resizable=True, fullscreen=False, \
                      min_size=(200, 100), hidden=False, frameless=False, \
                      minimized=False, on_top=False, confirm_close=False, \
                      background_color='#FFF')
```

åå»ºä¸ä¸ªæ°ç pywebview çªå£ï¼å¹¶è¿åå¶å®ä¾ãå¨å¼å§ GUI å¾ªç¯ä¹åï¼çªå£ä¸ä¼æ¾ç¤ºã

- **title** çªå£æ é¢
- **url** è¦å è½½ç URLãå¦æ URL æ²¡æåè®®åç¼ï¼åå°å¶è§£æä¸ºç¸å¯¹äºåºç¨ç¨åºå¥å£ç¹çè·¯å¾ãæèï¼å¯ä»¥ä¼ é WSGI æå¡å¨å¯¹è±¡æ¥å¯å¨æ¬å° Web æå¡å¨ã
- **html** è¦å è½½ç HTML ä»£ç ãå¦æåæ¶æå®äº URL å HTMLï¼HTML ä¼åã
- **js_api** å° python å¯¹è±¡æ´é²å°å½å pywebview çªå£ç DOM ä¸­ãjs_api å¯¹è±¡çæ¹æ³å¯ä»¥éè¿è°ç¨ window.pywebview.api.<methodname>(<parameters>)ä» Javascript æ§è¡ãè¯·æ³¨æï¼è°ç¨ Javascript å½æ°ä¼æ¶å°ä¸ä¸ªåå« python å½æ°çè¿åå¼ãåªæåºæ¬ç Python å¯¹è±¡ï¼å¦ intãstrãdict......ï¼æè½è¿å Javascriptã
- **width** çªæ·å®½åº¦ãé»è®¤å¼ä¸º 800pxã
- **height** çªæ·é«åº¦ãé»è®¤å¼ä¸º 600pxã
- **x** çªå£ x åæ ãé»è®¤å¼å±ä¸­ã
- **y** çªå£ y åæ ãé»è®¤å¼å±ä¸­ã
- **resizable** æ¯å¦å¯ä»¥è°æ´çªå£å¤§å°ãé»è®¤å¼ä¸º True
- **fullscreen** ä»å¨å±æ¨¡å¼å¼å§ãé»è®¤ä¸º False
- **min_size** æå®æå°çªå£å¤§å°çï¼å®½åº¦ãé«åº¦ï¼åç»ãé»è®¤å¼ä¸º 200x100
- **hidden** é»è®¤æåµä¸åå»ºä¸ä¸ªéèççªå£ãé»è®¤ä¸º False
- **frameless** åå»ºä¸ä¸ªæ æ¡çªå£ãé»è®¤å¼ä¸º Falseã
- **minimized** ä»¥æå°åæ¨¡å¼å¯å¨
- **on_top** å°çªå£è®¾ç½®ä¸ºå§ç»ä½äºå¶ä»çªå£çé¡¶é¨ãé»è®¤å¼ä¸º Falseã
- **confirm_close** æ¯å¦æ¾ç¤ºçªå£å³é­ç¡®è®¤å¯¹è¯æ¡ãé»è®¤ä¸º False
- **background_color** å è½½ WebView ä¹åæ¾ç¤ºççªå£çèæ¯é¢è²ãæå®ä¸ºåå­è¿å¶é¢è²ãé»è®¤å¼ä¸ºç½è²ã
- **transparent** åå»ºä¸ä¸ªéæççªå£ãWindows ä¸æ¯æãé»è®¤å¼ä¸º Falseãè¯·æ³¨æï¼æ­¤è®¾ç½®ä¸ä¼éèæä½¿çªå£é¬éæãå°çªå£ chrome setframeless éèä¸º Trueã

#### webview.start

```
webview.start(func=None, args=None, localization={}, gui=None, debug=False, http_server=False)
```

å¯å¨ GUI å¾ªç¯å¹¶æ¾ç¤ºä¹ååå»ºççªå£ãæ­¤å½æ°å¿é¡»ä»ä¸»çº¿ç¨è°ç¨ã

- **func** å¯å¨ GUI å¾ªç¯æ¶è°ç¨çå½æ°ã
- **args** å½æ°åæ°ãå¯ä»¥æ¯åä¸ªå¼ï¼ä¹å¯ä»¥æ¯åç»å¼ã
- **localization** å¸¦ææ¬å°åå­ç¬¦ä¸²çè¯å¸ãé»è®¤å­ç¬¦ä¸²åå¶é®å¨ localization.py ä¸­å®ä¹
- **gui** å¼ºå¶ä½¿ç¨ç¹å®ç GUIãåè®¸çå¼æ¯ cefãqt æ gtkï¼å·ä½åå³äºå¹³å°ã
- **debug** å¯ç¨è°è¯æ¨¡å¼ã
- **http_server** å¯ç¨åç½® HTTP æå¡å¨ãå¦æå¯ç¨ï¼æ¬å°æä»¶å°ä½¿ç¨éæºç«¯å£ä¸çæ¬å° HTTP æå¡å¨æä¾æå¡ãå¯¹äºæ¯ä¸ªçªå£ï¼é½ä¼çæä¸ä¸ªåç¬ç HTTP æå¡å¨ãå¯¹äºéæ¬å° URLï¼æ­¤éé¡¹å°è¢«å¿½ç¥ã

### åé´éä¿¡

#### ä» Python è°ç¨ Javascript

window.evaluate_js(code, callback=None)åè®¸æ¨ä½¿ç¨åæ­¥è¿åçæåä¸ä¸ªå¼æ§è¡ä»»æ Javascript ä»£ç ãå¦ææä¾äºåè°å½æ°ï¼åè§£æ promiseï¼å¹¶è°ç¨åè°å½æ°ï¼ç»æä½ä¸ºåæ°ãJavascript ç±»åè½¬æ¢ä¸º Python ç±»åï¼ä¾å¦ JS å¯¹è±¡å° Python å­å¸ï¼æ°ç»å°åè¡¨ï¼æªå®ä¹ä¸º Noneãç±äºå®ç°éå¶ï¼å­ç¬¦ä¸²ânullâå°è¢«è®¡ç®ä¸º Noneãå¦å¤ï¼evaluate_js è¿åçå¼éå¶ä¸º 900 ä¸ªå­ç¬¦åã

#### ä» Javascript è°ç¨ Python

ä» Javascript è°ç¨ Python å½æ°å¯ä»¥éè¿ä¸¤ç§ä¸åçæ¹æ³å®æã

- éè¿å° Python ç±»çå®ä¾æ´é²ç» create_window ç js_apiãè¯¥ç±»çææå¯è°ç¨æ¹æ³é½å°ä»¥ pywebview.api.method_name çå½¢å¼å¬å¼å° JS åä¸­ãæ¹æ³åç§°ä¸å¾ä»¥ä¸åçº¿å¼å¤´ã
- éè¿å°å½æ°ä¼ éç»çªå£å¯¹è±¡ç expose(func)è¿å°ä»¥ pywebview.api.func_name çå½¢å¼å°ä¸ä¸ªæå¤ä¸ªå½æ°å¬å¼å° JS åãä¸ JS API ä¸åï¼expose ä¹åè®¸å¨è¿è¡æ¶å¬å¼å½æ°ãå¦æ JS API åä»¥è¿ç§æ¹å¼å¬å¼çå½æ°ä¹é´å­å¨åç§°å²çªï¼ååèä¼åã

## THX

- [vue-pywebview-pyinstaller](https://github.com/pangao1990/vue-pywebview-pyinstaller)