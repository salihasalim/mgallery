from django import forms

class MovieForm(forms.Form):


    title=forms.CharField()

    genre=forms.CharField()

    language=forms.CharField()

    year=forms.CharField()

    run_time=forms.IntegerField()

    director=forms.CharField()


    def clean(self):

        cleaned_data=super().clean()

        year=cleaned_data.get("year")

        if int(year) < 1990:
            error_message="year should be greater than 1990"

            self.add_error("year",error_message)


        run_time=cleaned_data.get("run_time")

        if run_time < 60 or run_time > 210:
            error_message="run time must between the range 60 and 210"
            self.add_error("run_time",error_message)



    