from clearml import Task
task = Task.init(project_name='exploring', task_name='ignore-just-print')
# // This next line is essential for your script to be executed remotely.
task.execute_remotely()
# // so anything you would use after this line, it would copied and sent to the server.
# // do something for example the next line!
print('Hello from the other side!')
task.close()