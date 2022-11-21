from django.shortcuts import render
from django.http import Http404

from .form import queryForm
from .dbtable import generate_dbtable, getDataframeFormAccdb, DBTABLENAME, ACCESSDBPATH


# TopPage.
def index(request):
  params = {'plateDt_start':'', 'plateDt_end':'', 'printDt_start':'', 'printDt_end':'', 'orderNum':'',
    'checkBox_gaibu':'', 'checkBox_system':'', 'checkBox_design':'', 'checkBox_redbaron':'', 'checkBox_aeon':'',
    'checkBox_outsource':'', 'form':None}
  if request.method == 'POST':
    form = queryForm(request.POST)

    params['form'] = form
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

    query = {
      'orderNum':params['orderNum'],
      'plateDt_start':params['plateDt_start'],'plateDt_end':params['plateDt_end'],
      'printDt_start':params['printDt_start'],'printDt_end':params['printDt_end'],
      'checkBox_gaibu':params['checkBox_gaibu'],'checkBox_system':params['checkBox_system'],
      'checkBox_design':params['checkBox_design'],'checkBox_redbaron':params['checkBox_redbaron'],
      'checkBox_aeon':params['checkBox_aeon'],'checkBox_outsource':params['checkBox_outsource'],
    }

    params['table'] = generate_dbtable(query)

  else:
    params['form'] = queryForm()

  return render(request, 'index.html', params)

#計画書詳細ページ
def detail(request, orderNum):
  params = {}
  #params['orderNum'] = orderNum

  #データベースから詳細取得
  df = getDataframeFormAccdb(ACCESSDBPATH , DBTABLENAME)
  #計画書番号の行取得
  df_orderNum = df[df['OrderNb'] == orderNum]
  
  #例外処理
  if len(df_orderNum) == 0 :
    raise Http404("計画書番号が見つかりませんでした。")
  elif len(df_orderNum) > 1:
    raise Http404("計画書番号の重複があります。")

  #詳細HTML表示
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