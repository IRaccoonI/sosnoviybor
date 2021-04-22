from source.bot.bot import tb, dispatch_message
from source.db import DBQuery

tb.polling(none_stop=True, interval=0)
# print(DBQuery.get_version())
# dispatch_message('Hello')