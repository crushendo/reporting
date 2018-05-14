from __future__ import absolute_import, unicode_literals
from celery import Celery
from reporting.celeryapp import app
from celery.task import Task
import mysql.connector
from mysql.connector import MySQLConnection, Error
from scoutapp.utils.analyze_card import blobDetector

# This task will take the image file uploaded by a user and run it through an image analysis program. 
# The task will then take the statistical outputs of this analysis program and add them to the spraytrials database table

@app.task
def add(image_path, row_id):
    
    sprayAnalysis = blobDetector()
    num_median_in, num_mean_in, num_stdev_in, vol_median_in, vol_mean_in, \
            coverage_percent = sprayAnalysis.main(image_path)
    
    #num_mean_in = 1
    #num_median_in = 2
    #num_stdev_in = 3
    #vol_mean_in = 4
    #vol_median_in = 5
    #coverage_percent = 6
    stats_list = ["num_mean_in", "num_median_in", "num_stdev_in", "vol_mean_in", "vol_median_in", "coverage_percent"]
    
    cnx = mysql.connector.connect(user='root', password='Kh18riku!',
                                      host='127.0.0.1',
                                      database='scouter',
                                      charset='utf8',
                                      use_unicode='FALSE',
                                      port = 3306)
    
    for column in stats_list:
        #print(locals()[column])
        print(num_mean_in)
        stat = float(format(locals()[column], '.4f'))
        query = """UPDATE scoutapp_spraytrials
                   SET """ + column + """ = %s
                   WHERE id = %s """
        data = (stat, row_id)

        try:
            conn = MySQLConnection(user='root', password='Kh18riku!',
                                      host='127.0.0.1',
                                      database='scouter',
                                      charset='utf8',
                                      use_unicode='FALSE',
                                      port = 3306)
            print(query, data)
            cursor = conn.cursor()
            cursor.execute(query, data)

            conn.commit()
            cursor.close()
            conn.close()
        except Error as error:
            print(error)
    
    #cursor.close()
    #conn.close()
    
    x = 2
    y = 3
    sum = x + y
    print row_id
    return row_id

