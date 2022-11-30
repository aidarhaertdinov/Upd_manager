from . import scheduler

@scheduler.task('interval', id='do_job_1', seconds=5, misfire_grace_time=30)
def job1():
    print('Это приложение UPD Manager')



