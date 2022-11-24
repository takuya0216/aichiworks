from django.shortcuts import render
from django.http import Http404

from .form import queryForm
from .dbtable import generate_dbtable, get_dataframe_from_accdb,init_dbtable,DBTABLENAME, ACCESSDBPATH


def index(request):
  params = {
    'plateDt_start':'', 'plateDt_end':'', 'printDt_start':'', 'printDt_end':'', 'orderNum':'',
    'checkBox_gaibu':'', 'checkBox_system':'', 'checkBox_design':'', 'checkBox_redbaron':'', 
    'checkBox_aeon':'', 'checkBox_outsource':'', 'checkBox_noproduction':'', 'checkBox_others':'',
    'checkBox_all':'', 'checkBox_year': '','checkBox_half_year':'', 'checkBox_rinten': '',
    'checkBox_kikuhan':'', 'checkBox_kikuzen':'', 'checkBox_pod':'', 'checkBox_futou':'',
    'checkBox_inkjet':'', 'checkBox_print_multi':'', 'checkBox_print_meishi': '', 'checkBox_noprint':'',
    'checkBox_print_outsource':'', 'checkBox_print_others': '', 'checkBox_shinohara': '', 'form':None}
  if request.method == 'POST':
    form = queryForm(request.POST)
    params['form'] = form
    params['checkBox_all'] = 'checkBox_all' in request.POST
    params['checkBox_year'] = 'checkBox_year' in request.POST
    params['checkBox_half_year'] = 'checkBox_half_year' in request.POST

    params['orderNum'] = request.POST['orderNum']
    params['plateDt_start'] = request.POST['plateDt_start']
    params['plateDt_end'] = request.POST['plateDt_end']
    params['printDt_start'] = request.POST['printDt_start']
    params['printDt_end'] = request.POST['printDt_end']

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
      'checkBox_half_year':params['checkBox_half_year'],'checkBox_rinten':params['checkBox_rinten'],
      'checkBox_kikuhan':params['checkBox_kikuhan'],'checkBox_kikuzen':params['checkBox_kikuzen'],
      'checkBox_pod':params['checkBox_pod'],'checkBox_futou':params['checkBox_futou'],
      'checkBox_inkjet':params['checkBox_inkjet'],'checkBox_print_multi':params['checkBox_print_multi'],   
      'checkBox_print_meishi':params['checkBox_print_meishi'],'checkBox_noprint':params['checkBox_noprint'],
      'checkBox_print_others':params['checkBox_print_others'],'checkBox_shinohara':params['checkBox_shinohara'],
      'checkBox_print_outsource':params['checkBox_print_outsource']
    }
    params['table'] = generate_dbtable(query)
  else:
    params['table'] = init_dbtable()
    params['form'] = queryForm()

  return render(request, 'index.html', params)

def detail(request, orderNum):
  params = {}
  df = get_dataframe_from_accdb(ACCESSDBPATH , DBTABLENAME)
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
  
  return render(request, 'detail.html', params)