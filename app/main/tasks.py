from app import scheduler
import logging

logging.basicConfig(filename='mylog.log')
logging.getLogger("apscheduler").setLevel(logging.INFO)
@scheduler.task('interval', id='do_job_1', seconds=10, misfire_grace_time=30)
def job1():
    print('Это приложение UPD Manager')



