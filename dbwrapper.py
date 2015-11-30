#!/usr/bin/python
import MySQLdb

def dbwrap(func):
  def new_func(conn, *args, **kwargs):
    cursor =conn.cursor()
    try:
      cursor.execute("BEGIN")
      retval = func(cursor, *args, **kwargs)
      cursor.execute("COMMIT")
    except:
      cursor.execute("ROLLBACK")
      raise
   finally:
     cursor.close()
   return retval

  new_func.__name__=func.__name__
  new_func.__doc = func.__doc__

  return new_func


 
@dbwrap
def do_something(cursor, val1=1, val2=2):
  cursor.execute("SELECT %s, %s", (val1, val2))
  return cursor.fetchall()


class SomeClass(object):
  def __init__(self):
    conn = MySQLdb.connect(db="test")
    self.instance_var = SomeClass.get_stuff(conn)
    print self.instance_var
    conn.close()
  
  @staticmethod
  @dbwrap
    def get_stuff(cursor):
      cursor.execute("SELECT 'blah'")
      return cursor.fetchall()[0][0]

if "__main__" == __name__:
  conn = MySQLdb.connect(db="test")
  print do_something(conn)
  print do_something(conn,3,4)
  print do_something(conn,5)

  s=SomeClass()
