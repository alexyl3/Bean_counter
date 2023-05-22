from flask import Flask, render_template

from data.form import Form

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/", methods=['GET', 'POST'])
def index():
    form = Form()
    info = [2000, 4000, 7000, 10000, 20000, 35000, 50000, 65000, 80000,
            100000, 130000, 160000, 200000, 250000, 35000, 500000, 700000, 900000, 1200000, 1500000, 1800000]
    sal = [4200, 7350, 12600, 16800, 31500, 52500, 73500, 94500, 115500,
           136500, 168000, 210000, 252000, 315000, 336000, 420000, 525000, 630000, 735000, 787500, 945000]
    if form.validate_on_submit():
        main_beans = form.main_beans.data
        print(main_beans)
        salar = 0
        if not form.add_beans.data:
            add = 0
        else:
            add = form.add_beans.data
        for i in info:
            if i > main_beans:
                salar = sal[info.index(i) - 1]
                break
        print(salar)
        result = round((add + main_beans + salar) / 210, 2)
        return render_template('index.html', title='Главная', form=form, result=result)
    return render_template("index.html", title='Главная', form=form)


def main():
    app.run(port=8000)


if __name__ == '__main__':
    main()
