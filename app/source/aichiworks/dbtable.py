import pandas as pd
import pandas_access as mdb
import datetime
from dateutil.relativedelta import relativedelta
from bs4 import BeautifulSoup

HEADERNAMES = {"IssueDt": "発行日", "Status":"状況" ,"UserNm": "担当営業", "OrderNb": "計画書No", "Classification":"種別", "MasterCd":"取引先No", "CodeNm":"取引先名",
                "CustomerIp": "取引先名2", "Delivery":"納品先", "DeliveryRm":"納品先備考", "ArticleNm":"品名", "ProductionDt":"制作開始", "OutsideDt":"外部入稿",
                "PlateDt":"刷版日", "PrintDt":"印刷日", "CuttingDt":"断裁日", "CuttingCt":"種別【断裁】", "BookbindingDt":"製本・加工", "BookbindingCt":"種別【製本・加工】",
                "PackingDt":"帯止・梱包", "PackingCt":"種別【帯止・梱包】", "DeliveryDt":"納品日", "DeliveryTm":"納品時刻", "Quantity":"数量", "QuantityUn":"単位【数量】",
                "Standard":"サイズ", "ColorCn":"色数", "ColorPr":"刷色", "Process_instructionsMc":"印刷機", "Process_instructionsMcIp":"外注先【印刷】", "Process_instructionsPd":"制作担当",
                "Process_instructionsPdIp":"外注先【制作】", "Distributor":"配送", "Distributor_Ip":"備考【配送】", "ShipmentDt":"本体発送日", "Sample_deliveryDt":"見本納品日",
                "Sample_deliveryTm":"見本納品時刻", "Sample_distributor":"見本配送", "Sample_distributorIp":"備考【見本配送】", "Sample_shipmentDt":"見本発送日", "Insert1Dt":"折込日1",
                "Insert2Dt":"折込日2", "Bookbinding":"製本・加工方法", "Remarks":"備考"}

TEAMLIST = ['外部', 'システム', 'デザイン', 'RB', 'デジタルA', '外注']
ACCESSDBPATH = "./aichiworks/data/Database.accdb"
DBTABLENAME = "T_DataList"

#ヘッダーを日本語化
def translate_head(dataframe: pd.DataFrame):
    header_list = list(dataframe.columns.values)
    df_tr = dataframe
    for hd in header_list:
        if(hd in HEADERNAMES):
           df_tr = df_tr.rename(columns={hd: HEADERNAMES[hd]})

    return df_tr

def getLastyearDateTime():
    lastyear = datetime.datetime.now() - relativedelta(years=1)
    lastyear = lastyear.strftime('%Y-%m-%d')
    return lastyear
    #print(lastyear)

def getTodayDateTime():
    return datetime.datetime.now().strftime('%Y-%m-%d')

#不正値の変換やデータ型を揃える
#日付:datetime、不正値='1951/11/01 00:00:00'（あいち印刷創業日）
#文字列の0を''
#Bookbinding：'nan'を'なし'
#計画書システム側の修正が必要
#Weight、Spare、Real、Totalは自由入力ぽい。0と％のみを''に、その他はそのまま使用。データの扱いは文字列とする。
def formatDataframe(dataframe: pd.DataFrame):
    dataframe.loc[dataframe['IssueDt'] == "01/00/00 00:00:00", 'IssueDt'] = '1951/11/01 00:00:00'
    dataframe.loc[dataframe['PlateDt'] == "01/00/00 00:00:00", 'PlateDt'] = '1951/11/01 00:00:00'
    dataframe.loc[dataframe['PrintDt'] == "01/00/00 00:00:00", 'PrintDt'] = '1951/11/01 00:00:00'
    dataframe.loc[dataframe['ProductionDt'] == "01/00/00 00:00:00", 'ProductionDt'] = '1951/11/01 00:00:00'
    dataframe.loc[dataframe['OutsideDt'] == "01/00/00 00:00:00", 'OutsideDt'] = '1951/11/01 00:00:00'
    dataframe.loc[dataframe['CuttingDt'] == "01/00/00 00:00:00", 'CuttingDt'] = '1951/11/01 00:00:00'
    dataframe.loc[dataframe['BookbindingDt'] == "01/00/00 00:00:00", 'BookbindingDt'] = '1951/11/01 00:00:00'
    dataframe.loc[dataframe['PackingDt'] == "01/00/00 00:00:00", 'PackingDt'] = '1951/11/01 00:00:00'
    dataframe.loc[dataframe['DeliveryDt'] == "01/00/00 00:00:00", 'DeliveryDt'] = '1951/11/01 00:00:00'
    dataframe.loc[dataframe['ShipmentDt'] == "01/00/00 00:00:00", 'ShipmentDt'] = '1951/11/01 00:00:00'
    dataframe.loc[dataframe['Sample_deliveryDt'] == "01/00/00 00:00:00", 'Sample_deliveryDt'] = '1951/11/01 00:00:00'
    dataframe.loc[dataframe['Sample_shipmentDt'] == "01/00/00 00:00:00", 'Sample_shipmentDt'] = '1951/11/01 00:00:00'
    dataframe.loc[dataframe['Insert1Dt'] == "01/00/00 00:00:00", 'Insert1Dt'] = '1951/11/01 00:00:00'
    dataframe.loc[dataframe['Insert2Dt'] == "01/00/00 00:00:00", 'Insert2Dt'] = '1951/11/01 00:00:00'
    dataframe.loc[dataframe['RequestDt'] == "01/00/00 00:00:00", 'RequestDt'] = '1951/11/01 00:00:00'
    dataframe["IssueDt"] = pd.to_datetime(dataframe["IssueDt"])
    dataframe["PlateDt"] = pd.to_datetime(dataframe["PlateDt"])
    dataframe["PrintDt"] = pd.to_datetime(dataframe["PrintDt"])
    dataframe["ProductionDt"] = pd.to_datetime(dataframe["ProductionDt"])
    dataframe["OutsideDt"] = pd.to_datetime(dataframe["OutsideDt"])
    dataframe["CuttingDt"] = pd.to_datetime(dataframe["CuttingDt"])
    dataframe["BookbindingDt"] = pd.to_datetime(dataframe["BookbindingDt"])
    dataframe["PackingDt"] = pd.to_datetime(dataframe["PackingDt"])
    dataframe["DeliveryDt"] = pd.to_datetime(dataframe["DeliveryDt"])
    dataframe["ShipmentDt"] = pd.to_datetime(dataframe["ShipmentDt"])
    dataframe["Sample_deliveryDt"] = pd.to_datetime(dataframe["Sample_deliveryDt"])
    dataframe["Sample_shipmentDt"] = pd.to_datetime(dataframe["Sample_shipmentDt"])
    dataframe["Insert1Dt"] = pd.to_datetime(dataframe["Insert1Dt"])
    dataframe["Insert2Dt"] = pd.to_datetime(dataframe["Insert2Dt"])
    dataframe["RequestDt"] = pd.to_datetime(dataframe["RequestDt"])

    dataframe.loc[dataframe['CustomerIp'] == '0', 'CustomerIp'] = ''
    dataframe.loc[dataframe['Delivery'] == '0', 'Delivery'] = ''
    dataframe.loc[dataframe['DeliveryRm'] == '0', 'DeliveryRm'] = ''
    dataframe.loc[dataframe['CuttingCt'] == '0', 'CuttingCt'] = ''
    dataframe.loc[dataframe['BookbindingCt'] == '0', 'BookbindingCt'] = ''
    dataframe.loc[dataframe['PackingCt'] == '0', 'PackingCt'] = ''
    dataframe.loc[dataframe['QuantityUn'] == '0', 'QuantityUn'] = ''
    dataframe.loc[dataframe['Process_instructionsMc'] == '0', 'Process_instructionsMc'] = ''
    dataframe.loc[dataframe['Process_instructionsMcIp'] == '0', 'Process_instructionsMcIp'] = ''
    dataframe.loc[dataframe['Process_instructionsPd'] == '0', 'Process_instructionsPd'] = ''
    dataframe.loc[dataframe['Process_instructionsPdIp'] == '0', 'Process_instructionsPdIp'] = ''
    dataframe.loc[dataframe['Distributor'] == '0', 'Distributor'] = ''
    dataframe.loc[dataframe['Distributor_Ip'] == '0', 'Distributor_Ip'] = ''
    dataframe.loc[dataframe['Sample_distributor'] == '0', 'Sample_distributor'] = ''
    dataframe.loc[dataframe['Sample_distributorIp'] == '0', 'Sample_distributorIp'] = ''
    dataframe.loc[dataframe['Sample_distributor'] == '0', 'Sample_distributor'] = ''
    dataframe.loc[dataframe['Remarks'] == '0', 'Remarks'] = 'なし'

    dataframe.loc[dataframe['Paper'] == '0', 'Paper'] = ''

    dataframe.loc[dataframe['Standard1'] == '0', 'Standard1'] = ''
    dataframe.loc[dataframe['Quality1'] == '0', 'Quality1'] = ''
    dataframe.loc[dataframe['Weight1'] == '0', 'Weight1'] = ''
    dataframe.loc[dataframe['Grain1'] == '0', 'Grain1'] = ''
    dataframe.loc[dataframe['Spare1'] == '％', 'Spare1'] = ''
  
    dataframe.loc[dataframe['Standard2'] == '0', 'Standard2'] = ''
    dataframe.loc[dataframe['Quality2'] == '0', 'Quality2'] = ''
    dataframe.loc[dataframe['Weight2'] == '0', 'Weight2'] = ''
    dataframe.loc[dataframe['Grain2'] == '0', 'Grain2'] = ''
    dataframe.loc[dataframe['Spare2'] == '％', 'Spare2'] = ''

    dataframe.loc[dataframe['Standard3'] == '0', 'Standard3'] = ''
    dataframe.loc[dataframe['Quality3'] == '0', 'Quality3'] = ''
    dataframe.loc[dataframe['Weight3'] == '0', 'Weight3'] = ''
    dataframe.loc[dataframe['Grain3'] == '0', 'Grain3'] = ''
    dataframe.loc[dataframe['Spare3'] == '％', 'Spare3'] = ''

    dataframe.loc[dataframe['Bookbinding'].isnull(), 'Bookbinding'] = 'なし'
    dataframe.loc[dataframe['DeliveryTm'].isnull(), 'DeliveryTm'] = ''
    dataframe.loc[dataframe['Sample_deliveryTm'].isnull(), 'Sample_deliveryTm'] = ''
    
    return dataframe

#チェックボックスのクエリーから、テーブル表示するチーム名リストを取得する
def getTeamListFromQuery(gaibu :bool, system :bool, design :bool,
    readbaron :bool, aeon :bool, outsource :bool):

    teamlist = []

    if(gaibu):
       teamlist.append(TEAMLIST[0])
    if(system):
       teamlist.append(TEAMLIST[1])
    if(design):
       teamlist.append(TEAMLIST[2])
    if(readbaron):
       teamlist.append(TEAMLIST[3])
    if(aeon):
       teamlist.append(TEAMLIST[4])
    if(outsource):
       teamlist.append(TEAMLIST[5])
    
    return teamlist

def getDataframeFormAccdb(dbPath, tableName):
   return formatDataframe(mdb.read_table(dbPath, tableName))

# accessDBからqueryを使ってテーブルHTMLを生成。view.pyで出力。
def generate_dbtable(query):    
    df = getDataframeFormAccdb(ACCESSDBPATH, DBTABLENAME)

#前処理  
    
    #topページ用に列制限
    df_top = df[[ "IssueDt", "OrderNb", "UserNm", "CodeNm", "ArticleNm",
                "Standard", "ColorCn", "PlateDt", "PrintDt", "Process_instructionsMc", "Process_instructionsPd", "Status"]]
    #今日から一年前までに制限
    query_datetime = getLastyearDateTime()
    df_top = df_top[df_top['IssueDt'] >= query_datetime]
    df_top = df_top.drop('IssueDt', axis=1)
    #降順ソート
    #df_top = df_top.sort_values(by='IssueDt', ascending=False)

    
#クエリー処理

    #計画書番号
    if query['orderNum'] != '':
        df_top = df_top[df_top['OrderNb'] == query['orderNum']]

    #刷版日
    if (query['plateDt_start'] != '') ^ (query['plateDt_end'] != ''):
        #どちらか一方のみ
        if query['plateDt_start'] != '':
            df_top = df_top[df_top['PlateDt'] >= query['plateDt_start']]
        else:
            df_top = df_top[df_top['PlateDt'] <= query['plateDt_end']]
    elif (query['plateDt_start'] != '') and (query['plateDt_end'] != ''):
        #範囲
        df_top = df_top[
            (df_top['PlateDt'] >= query['plateDt_start']) &
            (df_top['PlateDt'] <= query['plateDt_end'])
        ]

    #印刷日
    if (query['printDt_start'] != '') ^ (query['printDt_end'] != ''):
        #どちらか一方のみ
        if query['printDt_start'] != '':
            df_top = df_top[df_top['PrintDt'] >= query['printDt_start']]
        else:
            df_top = df_top[df_top['PrintDt'] <= query['printDt_end']]
    elif (query['printDt_start'] != '') and (query['printDt_end'] != ''):
        #範囲
        df_top = df_top[
            (df_top['PrintDt'] >= query['printDt_start']) &
            (df_top['PrintDt'] <= query['printDt_end'])
        ]
    
    #チーム
    df_team_others = df_top[~df_top['Process_instructionsPd'].isin(TEAMLIST)]

    if query['checkBox_gaibu'] or query['checkBox_system'] or query['checkBox_design'] or query['checkBox_redbaron'] or query['checkBox_aeon'] or query['checkBox_outsource'] :
        teamlist = getTeamListFromQuery(query['checkBox_gaibu'], query['checkBox_system'],
            query['checkBox_design'], query['checkBox_redbaron'], query['checkBox_aeon'], query['checkBox_outsource'])
        df_top = df_top[df_top['Process_instructionsPd'].isin(teamlist)]
        df_top = pd.concat([df_top, df_team_others],axis=0)
    
#後処理
    
    df_top = translate_head(df_top)
    df_top.insert(0, '', '')

    soup = BeautifulSoup(df_top.to_html(table_id="table"), "html.parser")
    table = soup.find('tbody')

    tds = table.select('tr > td:nth-of-type(1)')
  
    for td in tds:
        td.string = ""
        td.attrs['class'] = 'checkmark'
        #squre icon
        nt = soup.new_tag('svg', attrs={"xmlns": "http://www.w3.org/2000/svg", "viewBox":"0 0 448 512"})
        nt2 = soup.new_tag('path', attrs={"d": "M384 32C419.3 32 448 60.65 448 96V416C448 451.3 419.3 480 384 480H64C28.65 480 0 451.3 0 416V96C0 60.65 28.65 32 64 32H384zM384 80H64C55.16 80 48 87.16 48 96V416C48 424.8 55.16 432 64 432H384C392.8 432 400 424.8 400 416V96C400 87.16 392.8 80 384 80z"})
        nt.append(nt2)
        td.append(nt)
   
    tds = table.select('tr > td:nth-of-type(2)')
    for td in tds:
        td_text = td.string
        td.string = ""
        nt = soup.new_tag('a', href='./' + td_text, target='blank')
        nt.string = td_text
        td.append(nt)

    return str(soup)
