import pymysql



def connDB(): #连接数据库函数
    conn=pymysql.connect(host='localhost',user='root',passwd='123',db='python',charset='utf8')
    cur=conn.cursor();
    return (conn,cur);

def exeUpdate(cur,sql):#更新语句，可执行update,insert语句
    sta=cur.execute(sql);
    return(sta);

def exeDelete(cur,IDs): #删除语句，可批量删除
    for eachID in IDs.split(' '):
        sta=cur.execute("delete from Person where name ='wanglin'");
    return (sta);

def exeQuery(cur,sql):#查询语句
    cur.execute(sql);
    # print(sql)
    return (cur);

def connClose(conn,cur):#关闭所有连接
    cur.close();
    conn.close();