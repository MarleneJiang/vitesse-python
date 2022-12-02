
class API:
    '''本地API，供前端JS调用'''
    window = None

    def getOwner(self):
        self.window.evaluate_js('getPythonData()')

        return '我是Python'
