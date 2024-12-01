from flask import Flask, render_template, request, Response
import subprocess
from jinja2 import Environment, FileSystemLoader
from ansi2html import Ansi2HTMLConverter
from mapping import mapping

app = Flask(__name__, static_url_path='/static')

# Main page
@app.route('/')
def Lab():
    return render_template('index.html', labs=mapping)

# Help page
@app.route('/help')
def Help():
    return render_template('help.html', labs=mapping)

# Lab page
@app.route('/<id>', methods=['GET', 'POST'])
def Lab_N(id):

    lab = mapping[int(id) - 1]
    values = lab['vars']

    if request.method == 'GET':
        return render_template('lab.html', lab=lab)
    else:
        template = get_template(id)


        for k in values:
            values[k] = request.form[k]

        hosts = template.render(values)
            
        with open(f'../ansible/{id}/hosts_rendered.ini', 'w+t') as f:
            f.write(hosts)

        command = f"ansible-playbook -i ../ansible/{id}/hosts_rendered.ini ../ansible/{id}/check.yml -CD"
        return run_command(command)

def get_template(id):
    env = Environment(loader=FileSystemLoader(f'../ansible/{id}'))
    template = env.get_template(f'hosts_template.jinja')
    return template

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    conv = Ansi2HTMLConverter(inline=True)

    def generate():
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                yield conv.convert(output.strip())
        rc = process.poll()

    return Response(generate(), mimetype='text/html')

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=80)