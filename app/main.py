import os
import sys

import webview
import argparse
from api.api import API
from config.config import Config

# 前端页面目录
if sys.flags.dev_mode:
    MAIN_DIR = os.path.join("..", "dist")  # 开发环境
    DEBUG = True
else:
    MAIN_DIR = os.path.join(".", "web")  # 生产环境
    DEBUG = False


def WebViewApp(port,dev=False):
    api = API()    # 本地接口
    cfg = Config()    # 配置文件
    if(dev):
        window = webview.create_window(cfg.appName, 'http://localhost:'+str(port)+'/',js_api=api)
        webview.start(debug=True, http_server=True)    # 启动窗口
    else:
        template = os.path.join(MAIN_DIR, "index.html")    # 设置页面，可以指向远程或本地
        window = webview.create_window(title=cfg.appName, url=template, js_api=api)    # 创建窗口
        api.window=window    # 本地接口
        webview.start(debug=DEBUG, http_server=True)    # 启动窗口


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--dev',
        type=str,
        default='False',
        help="开发模式")
    parser.add_argument(
        '--port',
        type=str,
        default='3333',
        help="端口号")
    args = parser.parse_args()

    WebViewApp(args.port,args.dev=='True')
