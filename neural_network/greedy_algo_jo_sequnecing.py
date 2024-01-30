class job:
    def __init__(self,task_id,daeadline,profit):
        self.task_id =task_id
        self.daeadline = daeadline
        self.profit =profit
def sechedulejobs(jobs,t):
     profit = 0 
     slot = [-1]*t
     jobs.sort(key=lambda X: X.profit ,reverse=True)
     for job in jobs:
        for j in reversed(range(job.daeadline)):
             if j<t and slot[j] == -1 :
                 slot[j] = job.task_id
                 profit += job.profit
                 break
     print("selected jobs",list(filter(lambda x:x !=-1 , slot )))
     print(profit)
     
if __name__ == '__main__':
    jobs = [
        job(1,9,15), job(2,4,10),job(3,7,20),job(4,10,2)
    ]
    sechedulejobs(jobs,10)
    
 