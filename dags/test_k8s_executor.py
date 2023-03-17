from airflow import DAG 
from airflow.operators.bash_operator import BashOperator 

dag = DAG( 
	'my_dag', 
	default_args={ 
		'owner': 'me', 
	}, 
	schedule_interval=None, 
) 

task1 = BashOperator( 
	task_id='task1', 
	bash_command= dag=dag
) 

task2 = BashOperator( 
	task_id='task2', 
	bash_command= dag=dag
) 

task1 >> task2 
