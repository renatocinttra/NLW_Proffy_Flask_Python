from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

proffys = [
    {
        'name': 'Diego Fernandes',
        'avatar': 'https://avatars2.githubusercontent.com/u/2254731?s=460&amp;u=0ba16a79456c2f250e7579cb388fa18c5c2d7d65&amp;v=4',
        'whatsapp': '89987654534',
        'bio': 'Entusiasta das melhores tecnologias de química avançada.Apaixonado por explodir coisas em laboratório e por mudar a vida das pessoas através de experiências. Mais de 200.000 pessoas já passaram por uma das minhas explosões.',
        'subject': 'Química',
        'cost': '20',
        'weekday': [0],
        'time_from': [720],
        'time_to': [1220]
    },
    {
        'name': 'Daniela Evangelista',
        'avatar': 'https://avatars2.githubusercontent.com/u/2254731?s=460&amp;u=0ba16a79456c2f250e7579cb388fa18c5c2d7d65&amp;v=4',
        'whatsapp': '89987654534',
        'bio': 'Entusiasta das melhores tecnologias de química avançada. Apaixonado por explodir coisas em laboratório e por mudar a vida das pessoas através de experiências. Mais de 200.000 pessoas já passaram por uma das minhas explosões.',
        'subject': 'Química',
        'cost': '20',
        'weekday': [1],
        'time_from': [720],
        'time_to': [1220]
    },
    {
        'name': 'Mayk Brito',
        'avatar': 'https://avatars2.githubusercontent.com/u/6643122?s=460&u=1e9e1f04b76fb5374e6a041f5e41dce83f3b5d92&v=4',
        'whatsapp': '89987654534',
        'bio': 'Entusiasta das melhores tecnologias de química avançada. Apaixonado por explodir coisas em laboratório e por mudar a vida das pessoas através de experiências. Mais de 200.000 pessoas já passaram por uma das minhas explosões.',
        'subject': 'Química',
        'cost': '20',
        'weekday': [1],
        'time_from': [720],
        'time_to': [1220]
    }
]

subjects = [
    'Artes',
    'Biologia',
    'Ciência',
    'Educação Física',
    'Física',
    'Geografia',
    'História',
    'Matemática',
    'Português',
    'Química'
]

weekdays = [
    'Domingo',
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-feira',
    'Sexta-feira',
    'Sábado'
]


@app.route('/')
def pageLanding():
    return render_template("index.html")


@app.route('/study', methods=['GET'])
def pageStudy():
    filters = request.args
    # Try change to loop.index in the conditional of page study.html
    return render_template("study.html", proffys=proffys, filters=filters, subjects=subjects, weekdays=weekdays)


@app.route('/give-classes', methods=['GET'])
def pageGiveClasses():
    data = request.args
    # Try change to loop.index in the conditional of page give-classes.html
    if len(data) != 0:
        proffys.append(data)
        return redirect(url_for('pageStudy'))
    else:
        return render_template("give-classes.html", subjects=subjects, weekdays=weekdays, data=data)


# Video_05 = 00h00m00s

app.run(debug=True)
