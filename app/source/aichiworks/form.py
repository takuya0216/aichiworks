from django import forms

class queryForm(forms.Form):
  orderNum = forms.CharField(
    label='計画書No',
    max_length = 13,
    min_length = 8,
    required = False,
    widget=forms.TextInput(
      attrs={'placeholder':'H99999999'})
  )

  plateDt_start = forms.DateField(
    label='刷版日',
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

  checkBox_others = forms.BooleanField(
    label='その他',
    label_suffix='',
    required=False,
    initial=False
  )