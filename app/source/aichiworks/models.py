import uuid
import datetime
from .dbtable import get_dataframe_from_accdb,get_dataframe_nday

from email.policy import default
from django.db import models

# Create your models here.
class Process(models.Model):
    process_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_number = models.CharField(max_length=15)
    process_time = models.DateTimeField(default=datetime.datetime.now())
    employee_id = models.SmallIntegerField(null=True, blank=True)
    status_id = models.SmallIntegerField(default=1)

class Employee(models.Model):
    employee_id = models.SmallIntegerField(primary_key=True)
    department_id = models.SmallIntegerField()
    employee_firstname = models.CharField(max_length=10)
    employee_lastname = models.CharField(max_length=10)
    position_id = models.SmallIntegerField()

class Department(models.Model):
    department_id = models.SmallIntegerField(primary_key=True)
    department_name = models.CharField(max_length=15)

class Position(models.Model):
    position_id = models.SmallIntegerField(primary_key=True)
    position_name = models.CharField(max_length=10)

class Status(models.Model):
    status_id = models.SmallIntegerField(primary_key=True)
    status_name = models.CharField(max_length=10)

class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    process_id = models.UUIDField()
    message_time = models.DateTimeField(default=datetime.datetime.now())
    employee_id_from = models.SmallIntegerField()
    employee_id_to = models.SmallIntegerField()
    message_text = models.TextField()
    message_enabled = models.BooleanField(default=True)

#utils
def conv_orderNum_to_processID(orderNumber):
    process = Process.objects.get(order_number=orderNumber)
    if(Process.objects.filter(order_number=orderNumber).count() == 1):
        return process.pk
    else:
        return False

#Process
#If emp_id is empty. Then database value is recorded as None.
def add_process(order_nm, emp_id=0):
  if not Process.objects.filter(order_number=order_nm).exists():
    if emp_id == 0 or emp_id == '':
      Process.objects.create(order_number=order_nm)
    else:
      Process.objects.create(order_number=order_nm,employee_id=emp_id)

def update_process():
  df = get_dataframe_from_accdb()
  #何日前まで取ってくるべきか要検討
  df = get_dataframe_nday(df, 1)
  process_orderNM_list = Process.objects.all().values_list('order_number', flat=True)
  df_update = df[~df['OrderNb'].isin(process_orderNM_list)]

  for orderNM in df_update['OrderNb'].values:
    add_process(orderNM)

  return df_update['OrderNb'].values

def edit_process_employee_id(process_ID, emp_id):
  process = Process.objects.get(process_id=process_ID)
  if Employee.objects.filter(employee_id=emp_id).exists():
    process.employee_id = emp_id
    process.save()
    return True
  else:
    return False

def edit_process_status_id(process_ID, stus_id):
  process = Process.objects.get(process_id=process_ID)
  if Status.objects.filter(status_id = stus_id).exists():
    process.status_id = stus_id
    process.save()
    return True
  else:
    return False

def del_process(order_nm):
  processID = conv_orderNum_to_processID(order_nm)

  if processID:
    Process.objects.filter(order_number=order_nm).delete()
    #delete Message has ProcessID
    messages = Message.objects.filter(process_id=processID)
    for msg in messages:
      delete_message(msg.message_id)
  else:
    return False

  return True

def del_all_process():
  Process.objects.all().delete()

#Message
def send_message(process_ID, message_from, message_to, message_text):
    Message.objects.create(process_id=process_ID, employee_id_from=message_from,
                            employee_id_to=message_to, message_text=message_text)

def disable_message(message_ID):
    message = Message.objects.get(message_id=message_ID)
    message.message_enabled = False
    message.save()

def enable_message(message_ID):
    message = Message.objects.get(message_id=message_ID)
    message.message_enabled = True
    message.save()

def is_message_enabled(message_ID):
    message = Message.objects.get(message_id=message_ID)
    return message.message_enabled

def tggle_message_enabled(message_id):
    if is_message_enabled(message_id):
        disable_message(message_ID=message_id)
    else:
        enable_message(message_ID=message_id)

def delete_message(message_ID):
    Message.objects.filter(message_id=message_ID).delete()

#Initialize
def init_database():
  #create static database if it not exist
  #if not Process.objects.exists():
  #  add_process('H2212217', 1, datetime.datetime.now(), 288)
  
  #if not Employee.objects.exists():
  #  Employee.objects.create(employee_id=288, department_id=5,
  #                          employee_firstname='卓也', employee_lastname='石田',
  #                          position_id=9)
  
  if not Department.objects.exists():
    Department.objects.create(department_id=1, department_name='営業')
    Department.objects.create(department_id=2, department_name='総務')
    Department.objects.create(department_id=3, department_name='経理')
    Department.objects.create(department_id=4, department_name='工務')
    Department.objects.create(department_id=5, department_name='デジタルプリプレス')
    Department.objects.create(department_id=6, department_name='輪転')
    Department.objects.create(department_id=7, department_name='枚葉')
    Department.objects.create(department_id=8, department_name='製本')
    Department.objects.create(department_id=9, department_name='その他')

  if not Position.objects.exists():
    Position.objects.create(position_id=1, position_name='社長')
    Position.objects.create(position_id=2, position_name='専務')
    Position.objects.create(position_id=3, position_name='次長')
    Position.objects.create(position_id=4, position_name='部長')
    Position.objects.create(position_id=5, position_name='課長')
    Position.objects.create(position_id=6, position_name='課長代理')
    Position.objects.create(position_id=7, position_name='係長')
    Position.objects.create(position_id=8, position_name='主任')
    Position.objects.create(position_id=9, position_name='役職なし')
    Position.objects.create(position_id=10, position_name='パート')
    Position.objects.create(position_id=11, position_name='アルバイト')

  if not Status.objects.exists():
    Status.objects.create(status_id=1, status_name='新規')
    Status.objects.create(status_id=2, status_name='製作中')
    Status.objects.create(status_id=3, status_name='入稿待ち')
    Status.objects.create(status_id=4, status_name='出力・検版')
    Status.objects.create(status_id=5, status_name='刷版')
    Status.objects.create(status_id=6, status_name='完了')

  #if not Message.objects.exists():
    #Message.objects.create(process_id='4c88dcbf-35d9-4ea0-b2d8-93d0c3f1dbaf', employee_id_from=288,
    #                        employee_id_to='314',message_text='メッセージテキスト送信テスト。')
