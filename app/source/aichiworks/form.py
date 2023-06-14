from django import forms

class queryForm(forms.Form):
  checkBox_all = forms.BooleanField(
    label='全て',
    label_suffix='',
    required=False,
    initial=False
  )
  checkBox_year = forms.BooleanField(
    label='1年',
    label_suffix='',
    required=False,
    initial=False
  )
  checkBox_half_year = forms.BooleanField(
    label='半年',
    label_suffix='',
    required=False,
    initial=False
  )
  checkBox_three_month = forms.BooleanField(
    label='3ヶ月',
    label_suffix='',
    required=False,
    initial=True
  )
  checkBox_one_month = forms.BooleanField(
    label='1ヶ月',
    label_suffix='',
    required=False,
    initial=False
  )
  checkBox_today = forms.BooleanField(
    label='今日',
    label_suffix='',
    required=False,
    initial=False
  )

  orderNum = forms.CharField(
    label='計画書No',
    label_suffix='',
    required = False,
    widget=forms.TextInput(
      attrs={'placeholder':'H99999999'})
  )

  plateDt_start = forms.DateField(
    label='刷版日',
    label_suffix='',
    input_formats=['%Y-%m-%d'],
    required = False,
    widget=forms.DateInput(attrs={"type":"date"})
  )

  plateDt_end = forms.DateField(
    label='',
    input_formats=['%Y-%m-%d'],
    required = False,
    widget=forms.DateInput(attrs={"type":"date"})
  )

  printDt_start = forms.DateField(
    label='印刷日',
    label_suffix='',
    input_formats=['%Y-%m-%d'],
    required = False,
    widget=forms.DateInput(attrs={"type":"date"})
  )

  printDt_end = forms.DateField(
    label='',
    input_formats=['%Y-%m-%d'],
    required = False,
    widget=forms.DateInput(attrs={"type":"date"})
  )

  checkBox_gaibu = forms.BooleanField(
    label='外部',
    label_suffix='',
    required=False,
    initial=False
  )

  checkBox_system = forms.BooleanField(
    label='システム',
    label_suffix='',
    required=False,
    initial=False
  )

  checkBox_design = forms.BooleanField(
    label='デザイン',
    label_suffix='',
    required=False,
    initial=False
  )

  checkBox_redbaron = forms.BooleanField(
    label='RB',
    label_suffix='',
    required=False,
    initial=False
  )

  checkBox_aeon = forms.BooleanField(
    label='イオン',
    label_suffix='',
    required=False,
    initial=False
  )

  checkBox_outsource = forms.BooleanField(
    label='外注',
    label_suffix='',
    required=False,
    initial=False
  )

  checkBox_noproduction = forms.BooleanField(
    label='制作なし',
    label_suffix='',
    required=False,
    initial=False
  )

  checkBox_others = forms.BooleanField(
    label='その他',
    label_suffix='',
    required=False,
    initial=False
  )

  checkBox_rinten = forms.BooleanField(
    label='輪転',
    label_suffix='',
    required=False,
    initial=False
  )
  
  checkBox_kikuhan = forms.BooleanField(
    label='菊半',
    label_suffix='',
    required=False,
    initial=False
  )

  checkBox_kikuzen = forms.BooleanField(
    label='菊全',
    label_suffix='',
    required=False,
    initial=False
  )

  checkBox_pod = forms.BooleanField(
    label='オンデマンド',
    label_suffix='',
    required=False,
    initial=False
  )

  checkBox_futou = forms.BooleanField(
    label='封筒機',
    label_suffix='',
    required=False,
    initial=False
  )

  checkBox_inkjet = forms.BooleanField(
    label='インクジェット',
    label_suffix='',
    required=False,
    initial=False
  )

  checkBox_print_multi = forms.BooleanField(
    label='複数あり',
    label_suffix='',
    required=False,
    initial=False
  )

  checkBox_print_outsource = forms.BooleanField(
    label='外注',
    label_suffix='',
    required=False,
    initial=False
  )

  checkBox_print_meishi = forms.BooleanField(
    label='名刺機',
    label_suffix='',
    required=False,
    initial=False
  )

  checkBox_noprint = forms.BooleanField(
    label='印刷なし',
    label_suffix='',
    required=False,
    initial=False
  )

  checkBox_print_others = forms.BooleanField(
    label='その他',
    label_suffix='',
    required=False,
    initial=False
  )

  checkBox_shinohara = forms.BooleanField(
    label='シノハラ',
    label_suffix='',
    required=False,
    initial=False
  )

  employee_id = forms.IntegerField(
    label='社員番号',
    label_suffix='',
    required = False,
  )

  time = forms.DateTimeField(
    label='時間',
    input_formats=['%Y-%m-%dT%H:%M'],
    required = False,
    widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
  )

  process_status_id = forms.IntegerField(
    label='進行状況ID',
    label_suffix='',
    required = False,
  )

  employee_id_from = forms.IntegerField(
    label='送信者（社員番号）',
    label_suffix='',
    required = False,
  )

  employee_id_to = forms.IntegerField(
    label='受信者（社員番号）',
    label_suffix='',
    required = False,
  )

  message = forms.CharField(
    label='メッセージ',
    label_suffix='',
    required = False,
    widget=forms.Textarea(attrs={'placeholder':'メッセージ...'})
  )

  message_id = forms.CharField(
    label='messageID',
    label_suffix='',
    required = True,
    max_length=100,
  )

  checkBox_messabe_enabled = forms.BooleanField(
    label='有効・無効切り替え',
    label_suffix='',
    required=False,
    initial=False
  )

  checkBox_update = forms.BooleanField(
    label='更新',
    label_suffix='',
    required=False,
    initial=False
  )

  checksheet_output_1 = forms.BooleanField(
    label='印刷用PDFである事を確認した',
    label_suffix='',
    required=True,
    initial=False
  )

  checksheet_output_2 = forms.BooleanField(
    label='フォントが埋め込みまたは、アウトライン化されている',
    label_suffix='',
    required=True,
    initial=False
  )

  checksheet_output_3 = forms.BooleanField(
    label='カラーは適正である（版数・特色・リッチブラック・カラースペース）',
    label_suffix='',
    required=True,
    initial=False
  )

  checksheet_output_4 = forms.BooleanField(
    label='出力サイズ（仕上がり）は適正である',
    label_suffix='',
    required=True,
    initial=False
  )

  checksheet_output_5 = forms.BooleanField(
    label='化粧断・塗り足しの有無と適正を確認した',
    label_suffix='',
    required=True,
    initial=False
  )

  checksheet_output_6 = forms.BooleanField(
    label='面付けの有無と適正を確認した',
    label_suffix='',
    required=True,
    initial=False
  )

  checksheet_output_7 = forms.BooleanField(
    label='ファイル名は適正である',
    label_suffix='',
    required=True,
    initial=False
  )

  message_input = forms.CharField(
    label='',
    label_suffix='',
    required = True,
    widget=forms.Textarea(attrs={'rows':'1','name':'message_input'})
  )