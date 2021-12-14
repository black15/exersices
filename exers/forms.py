from django import forms 
from .models import Exer
class AddAnAexerForms(forms.ModelForm):
    class Meta:
        '''
        '''
        model = Exer 
        fields = ['name','speciality','subject','ex_file','sou_file']
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)#        self.fields['username'].widget.attrs.update({'class':'text__field','id':'username'})
        self.fields['name'].widget.attrs.update({'class':'field_input'})
        self.fields['name'].label = 'title'
        self.fields['speciality'].widget.attrs.update({'class':'field_select'})
        self.fields['speciality'].label = 'speciality'
        self.fields['subject'].widget.attrs.update({'class':'field_select'})
        self.fields['subject'].label = 'module'
        self.fields['ex_file'].label = 'File'
        self.fields['sou_file'].label = 'Solution File'