import datetime

import pandas as pd

START_INDEX_OF_ORIKOMI = 64
START_INDEX_OF_POS = 96
START_INDEX_OF_SHOP_SAMPLE = 24

DATAOFFSET = 4
SHOP_SAMPLE_DATAOFFSET = 10
SHOP_SAMPLE_TARGETOFFSET = 8
DATASETNUM = 8
SHOP_SAMPLE_DATASETNUM = 4


def csv_to_dataframe(filepath):
    df = pd.read_csv(filepath)
    return df

if __name__=='__main__':
    filepath = 'data/2212_all_2.csv'
    ng_dataframe = ['<設定なし>','<設定なし>','<設定なし>','<設定なし>']
    output_dct ={'shop_id':'','year':'','month':'','distribution_type_id':'','platenum':'', 'printDate':'',
                'shipDate':'','arriveDate':'','distributionDate':'','deliveryDate':'','service':'',
                'printNum':'','distributer':'','destination_id':'','printer':'','note':''}
    output_dct2 = {'shop_id':'','year':'','month':'','service':'','shop_sample_num':''}
    output_list = []
    output_list2 = []
    df = pd.read_csv(filepath)
    df = df.replace('(.*)⑭(.*)',r'\1（株）\2',regex=True)
    df = df.replace('(.*)⑰(.*)',r'\1（有）\2',regex=True)

    
    for index in df.index:
        df_test = df[index:index+1]

        shop_id = df_test.iloc[0,2]
        shop_id = shop_id % 1000

        if(shop_id == 652):
            continue

        output_dct['shop_id'] = int(shop_id)
        output_dct2['shop_id'] = int(shop_id)
        month = df_test.iloc[0,4]
        if(month == '<設定なし>'):
            month = 0
        else:
            month = int(month.replace('月', ''))

        output_dct['month'] = month
        output_dct2['month'] = month

        dt = datetime.datetime.now()
        if(month != 1):
            output_dct['year'] = dt.year
            output_dct2['year'] = dt.year
        else:
            output_dct['year'] = dt.year + 1
            output_dct2['year'] = dt.year + 1 
        
        #print('-'*100)
        #print(df_test)
        #print('shop_id:' + str(output_dct2['shop_id']))
        #print('year:' + str(output_dct2['year']))
        #print('month:' + str(output_dct2['month'] ))


        for dataset in range(SHOP_SAMPLE_DATASETNUM):
            start_index = START_INDEX_OF_SHOP_SAMPLE + SHOP_SAMPLE_DATAOFFSET*dataset
            tmp_df = df_test.iloc[:,[start_index,start_index + SHOP_SAMPLE_TARGETOFFSET]]
            if tmp_df.iloc[0,0] == '<設定なし>':
                break
            output_dct2['service'] = tmp_df.iloc[0,0]
            output_dct2['shop_sample_num'] = tmp_df.iloc[0,1]
            output_list2.append(output_dct2.copy())
    """
        #折込
        for dataset in range(DATASETNUM):
            start_index = START_INDEX_OF_ORIKOMI + DATAOFFSET*dataset
            tmp_df = df_test.iloc[:,start_index:start_index + DATAOFFSET]
            answear = (tmp_df == ng_dataframe)
            
            if(answear.all(axis='columns')[index]):
                break
            else:
                #print(tmp_df)
                output_dct['distribution_type_id'] = 1
                output_dct['distributionDate'] = datetime.datetime.strptime(tmp_df.iloc[0,0],'%Y/%m/%d')
                output_dct['service'] = tmp_df.iloc[0,1]
                output_dct['printNum'] = tmp_df.iloc[0,2]
                output_dct['distributer'] = tmp_df.iloc[0,3]
                #print('配付種別:' + str(output_dct['distribution_type_id']))
                #print('配付日:' + str(output_dct['distributionDate']))
                #print('サービス告知:' + str(output_dct['service']))
                #print('部数:' + output_dct['printNum'])
                #print('業者:' + output_dct['distributer'])
                output_list.append(output_dct.copy())
               
        #ポスティング
        for dataset in range(DATASETNUM):
            start_index = START_INDEX_OF_POS + DATAOFFSET*dataset
            tmp_df = df_test.iloc[:,start_index:start_index + DATAOFFSET]
            answear = (tmp_df == ng_dataframe)
            
            if(answear.all(axis='columns')[index]):
                break
            else:
                #print(tmp_df)
                output_dct['distribution_type_id'] = 2
                output_dct['distributionDate'] = datetime.datetime.strptime(tmp_df.iloc[0,0],'%Y/%m/%d')
                output_dct['service'] = tmp_df.iloc[0,1]
                output_dct['printNum'] = tmp_df.iloc[0,2]
                output_dct['distributer'] = tmp_df.iloc[0,3]
                #print('配付種別:' + str(output_dct['distribution_type_id']))
                #print('配付日:' + str(output_dct['distributionDate']))
                #print('サービス告知:' + str(output_dct['service']))
                #print('部数:' + output_dct['printNum'])
                #print('業者:' + output_dct['distributer'])
                output_list.append(output_dct.copy())  

    

    """
    for list in output_list2:
        print(list)