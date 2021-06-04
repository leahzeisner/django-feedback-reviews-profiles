from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "username": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Review"
        }
        error_messages = {
            "username": {
                "required": "Your name cannot be empty!",
                "max_length": "Please enter a shorter name!"
            }
        }




# class ReviewForm(forms.Form):
#     username = forms.CharField(
#         label="Your Name",
#         max_length=100, 
#         error_messages={
#             "required": "Your name cannot be empty!",
#             "max_length": "Please enter a shorter name!"
#         }
#     )
#     review_text = forms.CharField(
#         label="Your Feedback", 
#         widget=forms.Textarea,
#         max_length=200
#     )
#     rating = forms.IntegerField(
#         label="Your Rating",
#         min_value=1,
#         max_value=10
#     )
