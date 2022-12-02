import platform


class Config:
    '''配置文件'''

    appName = 'Vitesse-Python'  # 应用名称
    appVersion = "1.0.0"  # 应用版本号

    appSystem = platform.system()    # 本机系统类型
