import mysql.connector

class DbInfo:
    def __init__(self,config):
        self.config=config

    def get_data(self,sql,state):
        cnn= mysql.connector.connect(**self.config)

        if state==1:
            cursor=cnn.cursor()
            cursor.execute(sql)
            result=cursor.fetchall()
        elif state==2:
            cursor = cnn.cursor()
            cursor.execute(sql)
            cursor.execute('commit')
            result=[]
        cursor.close()
        cnn.close()
        return result



if __name__ == '__main__':
    from conf import project_path
    from comm.read_conf import ReadConfig
    config = eval(ReadConfig().read_config(project_path.datebae_conf_path, "DATABASE", 'config'))
    print(config)
    t=DbInfo(config)

    sql='SELECT a.* FROM `isport_yunketang_dev`.t_game_record a  WHERE a.team_id  ="6569"; '
    res=t.get_data(sql,1)
    print(res)

