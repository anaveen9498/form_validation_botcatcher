from django import forms

def check_a(value):
    if value[0]=='a':
        raise forms.ValidationError('Enter The Name Must Be Starting Letter With N')
    

class StudentForm (forms.Form):
    name=forms.CharField(max_length=100,validators=[check_a])
    age=forms.IntegerField()
    email=forms.EmailField()
    botcatcher=forms.CharField(max_length=50,widget=forms.HiddenInput,required=False)
    Re_Enter_Email=forms.EmailField()


    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['Re_Enter_Email']
        if e!=r:
            raise forms.ValidationError('Your Entered Email Is Not Valid Mail...Please Check Your Email..!!!')
        

    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('Required data is Not entered By Humans')
        
    def clean(self):
        ag=self.cleaned_data['age']
        if ag>15:
            raise forms.ValidationError('NOt Matched')

        


