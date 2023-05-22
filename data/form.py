from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    main_beans = IntegerField('Количество заработанных бобов', validators=
    [DataRequired(message="Это поле обязательно для заполнения")])
    add_beans = IntegerField('Количество дополнительных бобов', validators=[])
    submit = SubmitField('Рассчитать')