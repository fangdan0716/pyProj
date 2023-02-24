import logging
from conf import project_path
class MyLog():
    def my_log(sel,msg,mss_level,log_name='aoto_case',level='DEBUG',file_path=project_path.log_path):
    #日志收集器
        logger=logging.getLogger(log_name)
        logger.setLevel(level)#日志收集器级别

    #输出渠道
        fh=logging.FileHandler(file_path,encoding='utf-8')
        sh =logging.StreamHandler()
    #设置日志级别
        fh.setLevel(level)  #msg级别
        sh.setLevel(level)
    #设置日志输出格式
        formater=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s -日志信息 -%(message)s')
        fh.setFormatter(formater)
        sh.setFormatter(formater)

    #对接日志收集器以及输出渠道
        logger.addHandler(sh)
        logger.addHandler(fh)
        if level=="DEBUG":
            logger.debug(msg)
        elif level=="INFO":
            logger.info(msg)
        elif level=="WARNING":
            logger.warning(msg)
        elif level=="INFO":
            logger.info(msg)
        elif level=="CRITICAL":
            logger.critical(msg)
    #移除输出渠道
        logger.removeHandler(sh)
        logger.removeHandler(fh)

    def info(self,msg):
        self.my_log(msg,'INFO')

    def debug(self,msg):
        self.my_log(msg,'DEBUG')
    def error(self,msg):
        self.my_log(msg,'ERROR')
    def critical(self,msg):
        self.my_log(msg,'CRITICAL')

    def warning(self,msg):
        self.my_log(msg,'WARNING')



if __name__ == '__main__':
    MyLog().info('kill')