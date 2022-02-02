import time
from entity_layer.scheduler.scheduler import Scheduler

sch=Scheduler()

#sch.add_recurring_job_in_second(5)
sch.add_recurring_job_in_minute(1)
sch.start()
sch.add_recurring_job_weekly_basis('avn')
res=sch.add_job_at_time('2021-04-02 08:33:40')
res=sch.get_job(id='testing')


print(sch.get_all_job_id())
time.sleep(150)