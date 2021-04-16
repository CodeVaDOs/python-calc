import os
from dotenv import load_dotenv
from sql.connector import get_connection

load_dotenv()

connection = get_connection(
    os.environ.get('dbHost'),
    os.environ.get('dbUser'),
    os.environ.get('dbPass'),
    os.environ.get('dbName')
)

select_subscribe_by_chat_id = ("SELECT chat_id, is_subscribed FROM subscribes s WHERE s.chat_id = ( %s )")
update_subscribe = ("UPDATE subscribes s SET s.is_Subscribed=( %s ) WHERE s.chat_id = ( %s )")
insert_subscribe = ("INSERT INTO subscribes (chat_id, is_subscribed) VALUES (%s, true)")


def subscribe_chat(chat_id: int):
    with connection.cursor() as cursor:
        cursor.execute(select_subscribe_by_chat_id, (chat_id,))
        subscribe = cursor.fetchone()
        if subscribe:
            if bool(subscribe[1]) is False:
                cursor.execute(update_subscribe, (True, chat_id))
        else:
            cursor.execute(insert_subscribe, (chat_id,))
        connection.commit()


def unsubscribe_chat(chat_id: int):
    with connection.cursor() as cursor:
        cursor.execute(update_subscribe, (False, chat_id))
        connection.commit()


subscribe_chat(12421)

connection.close()
