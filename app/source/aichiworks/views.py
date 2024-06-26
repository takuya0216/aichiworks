import datetime

from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse,HttpResponse

import aichiworks.models as models
from .form import queryForm
import aichiworks.dbtable as dbtable

def index(request):
  params = {
    'plateDt_start':'', 'plateDt_end':'',
    'printDt_start':'', 'printDt_end':'', 'orderNum':'',
    'checkBox_gaibu':'', 'checkBox_system':'', 'checkBox_design':'', 'checkBox_redbaron':'', 
    'checkBox_aeon':'', 'checkBox_outsource':'', 'checkBox_noproduction':'', 'checkBox_others':'',
    'checkBox_all':'', 'checkBox_year': '','checkBox_half_year':'','checkBox_three_month':'','checkBox_one_month':'',
    'checkBox_today':'', 'checkBox_rinten': '',
    'checkBox_kikuhan':'', 'checkBox_kikuzen':'', 'checkBox_pod':'', 'checkBox_futou':'',
    'checkBox_inkjet':'', 'checkBox_print_multi':'', 'checkBox_print_meishi': '', 'checkBox_noprint':'',
    'checkBox_print_outsource':'', 'checkBox_print_others': '', 'checkBox_shinohara': '', 'form':None}
  if request.method == 'POST':
    form = queryForm(request.POST)
    params['form'] = form
    params['checkBox_all'] = 'checkBox_all' in request.POST
    params['checkBox_year'] = 'checkBox_year' in request.POST
    params['checkBox_half_year'] = 'checkBox_half_year' in request.POST
    params['checkBox_three_month'] = 'checkBox_three_month' in request.POST
    params['checkBox_one_month'] = 'checkBox_one_month' in request.POST
    params['checkBox_today'] = 'checkBox_today' in request.POST

    params['orderNum'] = request.POST['orderNum']
    params['printDt_start'] = request.POST['printDt_start']
    params['printDt_end'] = request.POST['printDt_end']
    params['plateDt_start'] = request.POST['plateDt_start']
    params['plateDt_end'] = request.POST['plateDt_end']

    params['checkBox_gaibu'] = 'checkBox_gaibu' in request.POST
    params['checkBox_system'] = 'checkBox_system' in request.POST
    params['checkBox_design'] = 'checkBox_design' in request.POST
    params['checkBox_redbaron'] = 'checkBox_redbaron' in request.POST
    params['checkBox_aeon'] = 'checkBox_aeon' in request.POST
    params['checkBox_outsource'] = 'checkBox_outsource' in request.POST
    params['checkBox_noproduction'] = 'checkBox_noproduction' in request.POST
    params['checkBox_others'] = 'checkBox_others' in request.POST

    params['checkBox_rinten'] = 'checkBox_rinten' in request.POST
    params['checkBox_kikuhan'] = 'checkBox_kikuhan' in request.POST
    params['checkBox_kikuzen'] = 'checkBox_kikuzen' in request.POST
    params['checkBox_pod'] = 'checkBox_pod' in request.POST
    params['checkBox_futou'] = 'checkBox_futou' in request.POST
    params['checkBox_inkjet'] = 'checkBox_inkjet' in request.POST
    params['checkBox_print_multi'] = 'checkBox_print_multi' in request.POST
    params['checkBox_print_meishi'] = 'checkBox_print_meishi' in request.POST
    params['checkBox_noprint'] = 'checkBox_noprint' in request.POST
    params['checkBox_print_others'] = 'checkBox_print_others' in request.POST
    params['checkBox_shinohara'] = 'checkBox_shinohara' in request.POST
    params['checkBox_print_outsource'] = 'checkBox_print_outsource' in request.POST

    query = {
      'orderNum':params['orderNum'],
      'plateDt_start':params['plateDt_start'],'plateDt_end':params['plateDt_end'],
      'printDt_start':params['printDt_start'],'printDt_end':params['printDt_end'],
      'checkBox_gaibu':params['checkBox_gaibu'],'checkBox_system':params['checkBox_system'],
      'checkBox_design':params['checkBox_design'],'checkBox_redbaron':params['checkBox_redbaron'],
      'checkBox_aeon':params['checkBox_aeon'],'checkBox_outsource':params['checkBox_outsource'],
      'checkBox_noproduction':params['checkBox_noproduction'],'checkBox_others':params['checkBox_others'],
      'checkBox_all':params['checkBox_all'], 'checkBox_year':params['checkBox_year'],
      'checkBox_half_year':params['checkBox_half_year'],'checkBox_three_month':params['checkBox_three_month'],
      'checkBox_one_month':params['checkBox_one_month'],'checkBox_today':params['checkBox_today'],
      'checkBox_rinten':params['checkBox_rinten'],
      'checkBox_kikuhan':params['checkBox_kikuhan'],'checkBox_kikuzen':params['checkBox_kikuzen'],
      'checkBox_pod':params['checkBox_pod'],'checkBox_futou':params['checkBox_futou'],
      'checkBox_inkjet':params['checkBox_inkjet'],'checkBox_print_multi':params['checkBox_print_multi'],   
      'checkBox_print_meishi':params['checkBox_print_meishi'],'checkBox_noprint':params['checkBox_noprint'],
      'checkBox_print_others':params['checkBox_print_others'],'checkBox_shinohara':params['checkBox_shinohara'],
      'checkBox_print_outsource':params['checkBox_print_outsource']
    }
    params['table'] = dbtable.generate_dbtable(query)
  else:
    params['table'] = dbtable.init_dbtable()
    params['form'] = queryForm()

  return render(request, 'aichiworks/index.html', params)

def detail(request, orderNum):
  params = {}
  df = dbtable.get_dataframe_from_accdb(dbtable.ACCESSDBPATH , dbtable.DBTABLENAME)
  df_orderNum = df[df['OrderNb'] == orderNum]
  
  if len(df_orderNum) == 0 :
    raise Http404("計画書番号が見つかりませんでした。")
  elif len(df_orderNum) > 1:
    raise Http404("計画書番号の重複があります。")

  params = df_orderNum.to_dict(orient='records')
  params = params[0]
  
  #Timestampのフォーマット：とりあえずゴリ押し。もっとうまい方法あるはず
  time_format = '%Y/%m/%d'
  params['IssueDt'] = params['IssueDt'].strftime(time_format)
  params['PlateDt'] = params['PlateDt'].strftime(time_format)
  params['PrintDt'] = params['PrintDt'].strftime(time_format)
  params['ProductionDt'] = params['ProductionDt'].strftime(time_format)
  params['OutsideDt'] = params['OutsideDt'].strftime(time_format)
  params['BookbindingDt'] = params['BookbindingDt'].strftime(time_format)
  params['PackingDt'] = params['PackingDt'].strftime(time_format)
  params['DeliveryDt'] = params['DeliveryDt'].strftime(time_format)
  params['Sample_deliveryDt'] = params['Sample_deliveryDt'].strftime(time_format)
  params['Sample_shipmentDt'] = params['Sample_shipmentDt'].strftime(time_format)
  params['Insert1Dt'] = params['Insert1Dt'].strftime(time_format)
  params['Insert2Dt'] = params['Insert2Dt'].strftime(time_format)
  params['ShipmentDt'] = params['ShipmentDt'].strftime(time_format)
  params['CuttingDt'] = params['CuttingDt'].strftime(time_format)
  
  return render(request, 'aichiworks/detail.html', params)

def show_process(request):

  models.update_process()

  response = {}
  response['process_new'] = models.Process.objects.filter(status_id=1)
  response['process_edit_wait'] = models.Process.objects.filter(status_id=2)
  response['process_prepress'] = models.Process.objects.filter(status_id=3)
  response['process_pressed'] = models.Process.objects.filter(status_id=4)
  response['process_complete'] = models.Process.objects.filter(status_id=5)
  response['status'] = models.Status.objects.all()

  return render(request, 'aichiworks/process.html', response)

def show_database(request):

  models.init_database()
  
  #show database
  response = {}
  
  response['process'] = models.Process.objects.all()
  response['process_new'] = models.Process.objects.filter(status_id=1)
  response['process_edit_wait'] = models.Process.objects.filter(status_id=2)
  response['process_prepress'] = models.Process.objects.filter(status_id=3)
  response['process_pressed'] = models.Process.objects.filter(status_id=4)
  response['process_complete'] = models.Process.objects.filter(status_id=5)
  response['employee'] = models.Employee.objects.all()
  response['department'] = models.Department.objects.all()
  response['position'] = models.Position.objects.all()
  response['status'] = models.Status.objects.all()
  response['message'] = models.Message.objects.all()
  
  return render(request, 'aichiworks/show_database.html', response)

def add_process_render(request):
  params = {}
  form = queryForm(request.POST)
  params['form'] = form

  if request.method == 'GET':  
    return render(request, 'aichiworks/add_process.html', params)
  if request.method == 'POST':
    params['log'] = '追加された'
    if 'checkBox_update' in request.POST:
      params['update_oderNM'] = models.update_process()
      params['log'] = '計画書DBから更新された'
    else:
      if(request.POST['orderNum'] != ''):
        models.add_process(order_nm=request.POST['orderNum'], emp_id=request.POST['employee_id'])
        params['log'] = request.POST['orderNum'] + 'が追加された'

    return render(request, 'aichiworks/add_process.html', params)

def edit_process_render(request, processID):
  params = {}
  form = queryForm(request.POST)
  params['form'] = form
  params['process_id'] = processID

  if request.method == 'GET':  
    return render(request, 'aichiworks/edit_process.html', params)
  if request.method == 'POST':
    if not models.edit_process_employee_id(processID, request.POST['employee_id']):
      raise Http404("社員番号が見つかりません。")
    if not models.edit_process_status_id(processID, request.POST['process_status_id']):
      raise Http404("状態IDが見つかりません。")

    params['log'] = '変更された' 
  
    return render(request, 'aichiworks/edit_process.html', params)

def delete_process_ajax(request):
  if request.method == 'POST':
    processID=request.POST.get('process_id')
    if models.del_process(process_ID=processID):
      return HttpResponse(status=200)
    else:
      return Http404("プロセスの削除に失敗しました")
  
def delete_process_render(request):
  params = {}
  form = queryForm(request.POST)
  params['form'] = form

  if request.method == 'GET':  
    return render(request, 'aichiworks/delete_process.html', params)
  if request.method == 'POST':
    if 'checkBox_all' in request.POST:
      models.del_all_process()
      params['log'] = '全て削除された'
    else:
      if(request.POST['orderNum'] != ''):
        models.del_process(order_nm=request.POST['orderNum'])
        params['log'] = request.POST['orderNum'] + 'が削除された'

    return render(request, 'aichiworks/delete_process.html', params)

def show_message(request):
  if request.method == 'POST':
    order_num=request.POST.get('order_num')
    if models.Message.objects.filter(order_number=order_num).exists():
      response = models.Message.objects.filter(order_number=order_num)
      response_dic ={'message_json':[]}
      for res in response:
        res_dic = {
          'message_id':res.message_id,
          'order_num':res.order_number,
          'message_time':res.message_time,
          'employee_id_from':res.employee_id_from,
          'employee_id_to':res.employee_id_to,
          'message_text':res.message_text,
          'message_enabled':res.message_enabled
        }
        response_dic['message_json'].append(res_dic)
      return JsonResponse(response_dic, safe=False)
    else:
      return HttpResponse(status=204)

def send_message_render(request):
  params = {}
  form = queryForm(request.POST)
  params['form'] = form

  if request.method == 'GET':  
    return render(request, 'aichiworks/send_message.html', params)
  if request.method == 'POST':
    params['log'] = '送信された'
    if(request.POST['orderNum'] != ''):    
      models.send_message(order_num=request.POST['orderNum'], message_from=request.POST['employee_id_from'],
                message_text=request.POST['message'])
      params['log'] = request.POST['orderNum']

    return render(request, 'aichiworks/send_message.html', params)

def send_message_ajax(request):
  if request.method == 'POST':
    order_number=request.POST.get('order_num')
    message = request.POST.get('message')
    
    if message == '':
      return HttpResponse(status=204)

    response = models.send_message(order_num=order_number, message_text=message)
    res_dic = {
      'message_json': {
        'message_id':response.message_id,
        'order_num':response.order_number,
        'message_time':response.message_time,
        'employee_id_from':response.employee_id_from,
        'employee_id_to':response.employee_id_to,
        'message_text':response.message_text,
        'message_enabled':response.message_enabled
      }
    }
    return JsonResponse(res_dic, safe=False)
    
def delete_message_render(request):
  params = {}
  form = queryForm(request.POST)
  params['form'] = form

  if request.method == 'GET':  
    return render(request, 'aichiworks/delete_message.html', params)
  if request.method == 'POST':
    params['log'] = '削除された'
    message_id = request.POST['message_id']
    if 'checkBox_messabe_enabled' in request.POST:
      params['log'] = '有効無効が切り替わった'
      models.tggle_message_enabled(message_id)
      return render(request, 'aichiworks/delete_message.html', params)
    
    models.delete_message(message_ID=message_id)
    params['log'] = message_id + 'が削除された'

    return render(request, 'aichiworks/delete_message.html', params)

def change_status_ajax(request):
  if request.method == 'POST':
    processID = request.POST.get('process_id')
    offset = request.POST.get('offset')
    if models.Process.objects.filter(process_id=processID).exists():
      status =  models.Process.objects.get(process_id=processID).status_id + int(offset)
      models.edit_process_status_id(processID, status)
      return JsonResponse(data={'result':status}, status=200)
    else:
      raise Http404("プロセスIDが見つかりません")