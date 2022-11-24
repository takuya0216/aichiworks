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
    initial=True
  )
  checkBox_half_year = forms.BooleanField(
    label='半年',
    label_suffix='',
    required=False,
    initial=False
  )

  orderNum = forms.CharField(
    label='計画書No',
    label_suffix='',
    max_length = 13,
    min_length = 8,
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