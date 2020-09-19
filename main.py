from flask import Flask, render_template

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


@app.route('/')
def pageLanding():
    return render_template("index.html")


@app.route('/study')
def pageStudy():
    return render_template("study.html", proffys=proffys)


@app.route('/give-classes')
def pageGiveClasses():
    return render_template("give-classes.html")


# Video_04 = 01h21m00s

app.run(debug=True)
