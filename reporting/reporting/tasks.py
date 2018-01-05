from __future__ import absolute_import, unicode_literals
from celery import Celery
from celeryapp import app
#from celery.registry import task
from celery.task import Task
import mysql.connector
from python_mysql_dbconfig import read_db_config
#from utils.analyzePaper import (class)


#app = Celery('tasks', broker='amqp://guest:guest@localhost:5672/')

# This task will take the image file uploaded by a user and run it through an image analysis program. 
# The task will then take the statistical outputs of this analysis program and add them to the spraytrials database table

#class analyzeImage(Task):

@app.task
def add(image_path, row_id):
    
    #reportScript = scoutingReport()
    #reportScript.sql2xl(startDateInput, endDateInput)
    #reportScript.update_data()
    #reportScript.create_graph()
    
    num_mean_in = 1
    num_median_in = 2
    num_stdev_in = 3
    vol_mean_in = 4
    vol_median_in = 5
    coverage_percent = 6
    stats_list = ["num_mean_in", "num_median_in", "num_stdev_in", "vol_mean_in", "vol_median_in", "coverage_percent"]
    
    cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1',
                                      database='scouter',
                                      charset='utf8',
                                      use_unicode='FALSE',
                                      port = 3306)
    
    #db_config = read_db_config()
    for column in stats_list:
        stat = locals()[stats_list[column]]
        query = """UPDATE spraytrials
                   SET %s = %s
                   WHERE id = %s """
        data = (column, stat, row_id)

        try:
            conn = MySQLConnection(user='root', password='',
                                      host='127.0.0.1',
                                      database='scouter',
                                      charset='utf8',
                                      use_unicode='FALSE',
                                      port = 3306)
            cursor = conn.cursor
            cursor.execute(query, data)

            conn.commit()

        except Error as error:
            print(error)
    
    cursor.close()
    conn.close()
    
    x = 2
    y = 3
    sum = x + y
    print(row_id)
    return row_id
