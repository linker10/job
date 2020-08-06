from django import forms
from django.contrib.auth.models import User
from .models import CoverLetter, Document_CV

class CoverLetterForm(forms.ModelForm):
    class Meta:
        model = CoverLetter
        fields = ('cover_letter',)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document_CV
        fields = ('document', )

    def clean_document(self):
        document = self.cleaned_data['document']

        try:
            #validate content type
            main, sub = document.content_type.split('/')
            if not (sub in ['pdf']):
                raise forms.ValidationError('Please use a PDF file only.')

            #validate file size     # 4MB
            if len(document) > (4 * 1024000):
                raise forms.ValidationError('PDF file size may not exceed 4MBs.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new document
            """
            raise forms.ValidationError('You must provide a PDF file.')

        return document