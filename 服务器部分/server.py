# coding=utf-8
import socket
import MySQLdb
#执行更新sql语句
def update(date, chartName):
   for n in range(len(date)):
      for m in range(len(date[n])):
         key = list(date[n].keys())
         value = list(date[n].values())
         # print (key)
         # print (value)
         keyValue = key[m] + '=' + str(value[m])
         if key[m] == 'time':
            keyValue = key[m] + '=' + '\'' + str(value[m]) + '\''
         update = "update " + chartName + " set " + keyValue 
         try:
            # 执行SQL语句
            cursor.execute(update)
            # 提交到数据库执行
            db.commit()
         except:
            # 发生错误时回滚
            db.rollback()
         print('Mysql run: ', update)
#连接数据库
db = MySQLdb.connect("localhost", "数据库用户名", "数据库密码", "数据库名", charset='utf8',unix_socket='/var/lib/mysql/mysql.sock')
#获取操作游标
cursor = db.cursor()


ip_port = ('', 端口号)
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind(ip_port)
sk.listen(5)
while 1:
    print('wait cnonnect....')
    conn, address = sk.accept()
    print(address)
    data=[]
    while 1:
        data_recv = conn.recv(1024)
        stop=str(data_recv,encoding='utf-8')
        if stop=='stop':
            conn.close()
            break
        data=eval(data_recv)

        print('data',data)
        update(data,'data')
    
        reply=bytes('server:over',encoding='utf-8')
        conn.send(reply)
        
db.close()

