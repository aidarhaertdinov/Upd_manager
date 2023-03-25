from app import scheduler
import logging


logging.basicConfig(level=logging.INFO, filename='mylog.log')


@scheduler.task('interval', id='do_job_1', seconds=20, misfire_grace_time=30)
def job1():
    logging.info('Это приложение UPD Manager')



