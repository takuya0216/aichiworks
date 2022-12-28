import datetime

from django.shortcuts import render
from .models import DistoributionType,ShopHoliday,Printer,Service,Destination,DeliverySetting,Shop,ShopSample
import pandas as pd

PATH_TO_CSV = "rbworks/data/2212_all_2.csv"
PATH_TO_NOUHINSAKI = "rbworks/data/nohinsaki.csv"
PATH_TO_DELIVERYSETTING = "rbworks/data/DeliverySetting.csv"
PATH_TO_SHOP = "rbworks/data/shop.csv"

START_INDEX_OF_ORIKOMI = 64
START_INDEX_OF_POS = 96
START_INDEX_OF_SHOP_SAMPLE = 24

DATAOFFSET = 4
SHOP_SAMPLE_DATAOFFSET = 10
SHOP_SAMPLE_TARGETOFFSET = 8
DATASETNUM = 8
SHOP_SAMPLE_DATASETNUM = 4

def csv_to_shopsample_database(csv_path):
    output_dct2 = {'shop_id':'','year':'','month':'','service':'','shop_sample_num':''}
    output_list2 = []
    df = pd.read_csv(csv_path)
    #df = df.replace('(.*)⑭(.*)',r'\1（株）\2',regex=True)
    #df = df.replace('(.*)⑰(.*)',r'\1（有）\2',regex=True)

    for index in df.index:
        df_test = df[index:index+1]

        shop_id = df_test.iloc[0,2]
        shop_id = shop_id % 1000

        if(shop_id == 652):
            continue

        output_dct2['shop_id'] = int(shop_id)
        month = df_test.iloc[0,4]
        if(month == '<設定なし>'):
            month = 0
        else:
            month = int(month.replace('月', ''))

        output_dct2['month'] = month

        dt = datetime.datetime.now()
        if(month != 1):
            output_dct2['year'] = dt.year
        else:
            output_dct2['year'] = dt.year + 1 

        for dataset in range(SHOP_SAMPLE_DATASETNUM):
            start_index = START_INDEX_OF_SHOP_SAMPLE + SHOP_SAMPLE_DATAOFFSET*dataset
            tmp_df = df_test.iloc[:,[start_index,start_index + SHOP_SAMPLE_TARGETOFFSET]]
            if tmp_df.iloc[0,0] == '<設定なし>':
                break

            service = Service.objects.get(service_no=tmp_df.iloc[0,0])
            output_dct2['service'] = service.service_id
            output_dct2['shop_sample_num'] = tmp_df.iloc[0,1]
            output_list2.append(output_dct2.copy())
    
    return output_list2

def csv_to_lotdatabase(csv_path):
    ng_dataframe = ['<設定なし>','<設定なし>','<設定なし>','<設定なし>']
    output_dct = {'shop_id':'','year':'','month':'','distribution_type_id':'','platenum':'', 'printDate':'',
                'shipDate':'','arriveDate':'','distributionDate':'','deliveryDate':'','service':'',
                'printNum':'','distributer':'','destination_id':'','printer':'','note':''}
    output_list = []
    df = pd.read_csv(csv_path)
    df = df.replace('(.*)⑭(.*)',r'\1（株）\2',regex=True)
    df = df.replace('(.*)⑰(.*)',r'\1（有）\2',regex=True)

    for index in df.index:
        df_test = df[index:index+1]

        shop_id = df_test.iloc[0,2]
        shop_id = shop_id % 1000

        if(shop_id == 652):
            continue

        output_dct['shop_id'] = int(shop_id)
        month = df_test.iloc[0,4]
        if(month == '<設定なし>'):
            month = 0
        else:
            month = int(month.replace('月', ''))

        output_dct['month'] = month

        dt = datetime.datetime.now()
        if(month != 1):
            output_dct['year'] = dt.year
        else:
            output_dct['year'] = dt.year + 1 

        #折込
        for dataset in range(DATASETNUM):
            start_index = START_INDEX_OF_ORIKOMI + DATAOFFSET*dataset
            tmp_df = df_test.iloc[:,start_index:start_index + DATAOFFSET]
            answear = (tmp_df == ng_dataframe)
            
            if(answear.all(axis='columns')[index]):
                break
            else:
                output_dct['distribution_type_id'] = 1
                output_dct['distributionDate'] = datetime.datetime.strptime(tmp_df.iloc[0,0],'%Y/%m/%d')
                service = Service.objects.get(service_no=tmp_df.iloc[0,1])
                output_dct['service'] = service.service_id
                output_dct['printNum'] = tmp_df.iloc[0,2]
                output_dct['distributer'] = tmp_df.iloc[0,3]

                output_list.append(output_dct.copy())
               
        #ポスティング
        for dataset in range(DATASETNUM):
            start_index = START_INDEX_OF_POS + DATAOFFSET*dataset
            tmp_df = df_test.iloc[:,start_index:start_index + DATAOFFSET]
            answear = (tmp_df == ng_dataframe)
            
            if(answear.all(axis='columns')[index]):
                break
            else:
                output_dct['distribution_type_id'] = 2
                output_dct['distributionDate'] = datetime.datetime.strptime(tmp_df.iloc[0,0],'%Y/%m/%d')
                service = Service.objects.get(service_no=tmp_df.iloc[0,1])
                output_dct['service'] = service
                output_dct['printNum'] = tmp_df.iloc[0,2]
                output_dct['distributer'] = tmp_df.iloc[0,3]

                output_list.append(output_dct.copy())
               
    return output_list


# Create your views here.
def index(request):
    """
    df = pd.read_csv(PATH_TO_SHOP, header=None)
    for col in df.itertuples():
        Shop.objects.create(shop_id=col[1], shop_name=col[2],
        shopHoliday_id=col[3],shop_tell=col[4], shop_fax=col[5],
        shop_address=col[6])
    
    df = pd.read_csv(PATH_TO_DELIVERYSETTING, header=None)
    for col in df.itertuples():
        DeliverySetting.objects.create(shop_id=col[1], destination_id=col[2],
        distoribution_type_id=col[3],folding=col[4], notes=col[5],
        arrive_offset=col[6], shipp_offset=col[7])

    df = pd.read_csv(PATH_TO_NOUHINSAKI, header=None)
    for col in df.itertuples():
        Destination.objects.create(destination_id=col[1], destination_name=col[2],
        destination_post=col[3],destination_address=col[4], destination_tell=col[5])
    
    DistoributionType.objects.create(distribution_type_id=1, distribution_type_name='折込')
    DistoributionType.objects.create(distribution_type_id=2,distribution_type_name='ポスティング')
    ShopHoliday.objects.create(shopHoliday_id=1, shopHoliday_name='火曜定休')
    ShopHoliday.objects.create(shopHoliday_id=2, shopHoliday_name='水曜定休')
    ShopHoliday.objects.create(shopHoliday_id=3, shopHoliday_name='年中無休')
    Printer.objects.create(printer_name='あいち印刷')
    Printer.objects.create(printer_name='永昌堂')
    Printer.objects.create(printer_name='奉仕堂')
    Printer.objects.create(printer_name='プレステック')
    Service.objects.create(service_no='A', service_size='B3', service_tieup=False, service_name='工場PR')
    Service.objects.create(service_no='B', service_size='B3', service_tieup=False, service_name='修理保証')
    Service.objects.create(service_no='C', service_size='B3', service_tieup=False, service_name='ROS')
    Service.objects.create(service_no='D', service_size='B3', service_tieup=False, service_name='盗難保険')
    Service.objects.create(service_no='O', service_size='B3', service_tieup=False, service_name='オープンセール')
    Service.objects.create(service_no='AT', service_size='B3', service_tieup=True, service_name='工場PR+タイアップ')
    Service.objects.create(service_no='BT', service_size='B3', service_tieup=True, service_name='修理保証+タイアップ')
    Service.objects.create(service_no='CT', service_size='B3', service_tieup=True, service_name='ROS+タイアップ')
    Service.objects.create(service_no='DT', service_size='B3', service_tieup=True, service_name='盗難保険+タイアップ')
    Service.objects.create(service_no='6', service_size='B4', service_tieup=False, service_name='B4買取タテ(N)')
    Service.objects.create(service_no='7', service_size='B4', service_tieup=False, service_name='B4買取ヨコ(S)')
    Service.objects.create(service_no='8', service_size='B4', service_tieup=False, service_name='B4買取ヨコ(NS)')
    Service.objects.create(service_no='7T', service_size='B4', service_tieup=True, service_name='B4買取ヨコ(S)+タイアップ')
    Service.objects.create(service_no='8T', service_size='B4', service_tieup=True, service_name='B4買取ヨコ(NS)+タイアップ')
    
    
    shopsample_data = csv_to_shopsample_database(PATH_TO_CSV)

    for data in shopsample_data:
        ShopSample.objects.create(shop_id=data['shop_id'], year=data['year'], month=data['month'],
                                service_id=data['service'], shopsample_number=data['shop_sample_num'])
    """
    response = {}
    
    response['distoributionType'] = DistoributionType.objects.all()
    response['shopHoliday'] = ShopHoliday.objects.all()
    response['printer'] = Printer.objects.all()
    response['service'] = Service.objects.all()
    response['destination'] = Destination.objects.all()
    response['deliverySetting'] = DeliverySetting.objects.all()
    response['shop'] = Shop.objects.all()
    response['lot_data'] = csv_to_lotdatabase(PATH_TO_CSV)
    response['shopsample_data'] = ShopSample.objects.all()
    
    return render(request, 'rbworks/index.html', response)
    