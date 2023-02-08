import csv

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('base.html')


@app.route('/careers')
def careers():
    table_header = ('Job Position', 'Link', 'Campus')
    table_data = [('Maths Teacher',
                   ' https://www.betterteam.com/math-teacher-job-description ', 'Laval'),
                  ('Vice Principal',
                   'https://www.zippia.com/vice-principal-jobs/what-does-a-vice-principal-do/',
                   'Montreal'),
                  ('Secretary',
                   'https://climbtheladder.com/school-secretary/', 'Quebec City'),
                  ('Literature Teacher',
                   'https://ca.indeed.com/Literature-Teaching-jobs?vjk=ae9b5a6e965859d6 ', 'Quebec City'), ]
    return render_template('careers.html', table_header=table_header,
                           table_data=table_data)


@app.route('/info')
def info():
    headings = ('Name', 'Position', 'Email', 'Campus')
    data = [('Patrick Lebois', 'Director', 'patrick@amity.com', 'Laval'),
            ('Mary Tremblay', 'Vice Principal', 'marry@amity.com', 'Laval'),
            ('Kunal Patel', 'Maths Teacher', 'kunal@amity.com', 'Laval'),
            ('Bahar Erva', 'English Language Teacher', 'bahar@amity.com', 'Laval'),
            ('Yannick McAlly', 'Vice Principal', 'yannick@amity.com', 'Montreal'),
            ('Hassan Elkabir', 'Coordinator', 'hassan@amity.com', 'Montreal'),
            ('Helen Lechavette ', 'Vice Principal', 'helen@amity.com', 'Quebec City'),
            ('Simon Brown', 'Sport Teacher ', 'simon@amity.com', 'Quebec City'), ]

    return render_template('info.html', headings=headings, data=data)


@app.route('/news')
def news():
    prefix = '/static/'
    with open('data/news.csv') as f:
        doc_list = list(csv.reader(f))[1:]
    return render_template('news.html', doc_list=doc_list, prefix=prefix)


if __name__ == '__main__':
    app.run()
