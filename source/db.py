from .settings import DB_CON_PARAMETERS
import psycopg2

class DBQuery:
    @staticmethod
    def get_cursor():
        return psycopg2.connect(**DB_CON_PARAMETERS).cursor() 

    @staticmethod
    def get_version():
        with DBQuery.get_cursor() as cur:
            cur.execute('select version();')
            return cur.fetchone()

    @staticmethod
    def save_telegramm_chat(chat_id):
        with psycopg2.connect(**DB_CON_PARAMETERS) as conn, conn.cursor() as cur:
            try:
                cur.execute(
                    'INSERT INTO telegram_chat (id) VALUES (%s)',
                    (chat_id, )
                )
                conn.commit()
            except psycopg2.errors.UniqueViolation:
                pass

    @staticmethod
    def update_telegram_chat_role(chat_id, n_role):
        with psycopg2.connect(**DB_CON_PARAMETERS) as conn, conn.cursor() as cur:
            cur.execute(
                "UPDATE telegram_chat "
                "SET user_role = %s "
                "WHERE id = %s",
                (n_role, chat_id, )
            )
            conn.commit()


    @staticmethod
    def get_all_telegramm_chats():
        with psycopg2.connect(**DB_CON_PARAMETERS) as conn, conn.cursor() as cur:
            cur.execute(
                'SELECT id FROM telegram_chat'
            )
            data = cur.fetchall()
        return data

