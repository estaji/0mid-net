from django import forms


class ScanForm(forms.Form):
    """Add a job for instant check from homepage"""
    url = forms.URLField(label='url', max_length=300)
    action = forms.CharField(label='action')

    def clean_action(self):
        """Take action value and change it to system compatible value"""
        action = self.cleaned_data['action']
        if action == 'ping':
            action = 'pi'
            return action
        elif action == 'http':
            action = 'hi'
            return action
        else:
            self._errors['form'] = self.error_class(['Invalid action.'])
