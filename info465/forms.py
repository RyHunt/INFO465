from django import forms
from phonenumber_field.modelfields import PhoneNumberField

VisitedStateList = (
    ("Virgina", "Virgina"),
    ("Georgia", "Georgia"),
    ("Mississippi", "Mississippi"),
    ("Florida", "Florida"),
    ("Alabama", "Alabama"),
    ("Tennessee", "Tennessee"),
    ("Kentucky", "Kentucky"),
    )

FavoriteStateList = (
    ("Virgina", "Virgina"),
    ("Georgia", "Georgia"),
    ("Mississippi", "Mississippi"),
    ("Florida", "Florida"),
    ("Alabama", "Alabama"),
    ("Tennessee", "Tennessee"),
    ("Kentucky", "Kentucky"),
    )

BadWeather = (
    ("None", "None"),
    ("Heat", "Heat"),
    ("Humidity", "Humidity"),
    ("Thunder", "Thunder"),
    ("Rain", "Rain"),
    ("Snow", "Snow"),
    )


AllStates = [
    ('AK', 'Alaska'),
    ('AL', 'Alabama'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('DC', 'Washington D.C.'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming')
    ]

FavoriteColor = [
("None", "None"),
("Red", "Red"),
("Orange", "Orange"),
("Yellow", "Yellow"),
("Green", "Green"),
("Blue", "Blue"),
("Indigo", "Indigo"),
("Violet", "Violet")
]


class CheckBoxForm(forms.Form):
    firstName = forms.CharField(label="First Name:", max_length=15)

    lastName = forms.CharField(label="Last Name:", max_length=15)

    email = forms.EmailField(label="Email:", max_length=80)

    phone = forms.CharField(label="Phone Number:")

    statesVisited = forms.MultipleChoiceField(label="Which Southeastern states have you visited?",
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=VisitedStateList)

    faveStateVisited = forms.ChoiceField(label="What is your favorite Southeastern State?", choices=FavoriteStateList, widget=forms.RadioSelect, required=False)

    comment = forms.CharField(label="What's your opinion on the Southeast?", widget=forms.Textarea, required=False)

    badweather = forms.ChoiceField(label="What's your least favorite weather?", choices=BadWeather, required=False)

    faveColor = forms.ChoiceField(label="What is your favorite color?", choices=FavoriteColor)

    faveState = forms.MultipleChoiceField(label="Favorite Other States?", choices=AllStates, widget=forms.SelectMultiple, required=False)
