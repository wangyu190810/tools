# -*-coding:utf-8-*-
# email:190810401@qq.com
__author__ = 'wangyu'

from  sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,text

from base import conn



def insert_data(data):
    sql =text("insert into queue_message (url,status_code) "
              "VALUES (:url,:status_code)")
    sql = sql.bindparams(url=data.get("url"),
                         status_code=data.get("status_code"))
    conn.execute(sql)
    conn.commit()

def get_chouti_index():
    chouti_list = []
    

    def getKey(item):
        return item.get("ups")
    for row in get_chouti_data():
        data = dict()
        data['id'] = row['chouti_id']
        comments = row['comments']
        data['comments'] = sorted(comments,key= getKey,reverse=True)
        content = row['content']
        
        data['content'] = dict(
            title = content['title'],
            url = content['url'],
            createtime = content['createtime'],
            subject = content['subject']
        )

        chouti_list.append(data)
    return chouti_list


def get_chouti_data(offset=0,limit=10):
    sql = text("SELECT * FROM chouti ORDER BY chouti_id DESC LIMIT  :limit OFFSET :offset")
    sql = sql.bindparams(limit=limit,
                         offset=offset)
    data = conn.execute(sql)
    resp = data.fetchall()
    return resp

def main():
    get_chouti_data()



if __name__ == '__main__':
    main()




