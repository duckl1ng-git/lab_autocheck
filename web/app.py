from flask import Flask, render_template, request, Response, redirect
import subprocess
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

@app.route('/')
def Lab():
    return render_template('index.html')

#@app.route('/check', methods=['POST'])
def run_command(command):
    #command = request.form['command']
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    def generate():
        yield '<pre>\n'
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                yield output.strip() + '<br>\n'
        rc = process.poll()
        yield f'Exit code: {rc}'
        yield '</pre>\n'

    return Response(generate(), mimetype='text/html')

@app.route('/01', methods=['GET', 'POST'])
def Lab_01():
    if request.method == 'GET':
        return render_template('01.html')
    else:
        lab_id = request.form['lab_id']

        template = get_template(lab_id)

        hosts = template.render(
            pfsense_ip = request.form['pfsense_ip'],
            winsrv_ip = request.form['winsrv_ip'],
            win7_ip = request.form['win7_ip'],
            win10_ip = request.form['win10_ip'],
        )
        
        with open(f'../ansible/{lab_id}/hosts_rendered.yml', 'w+t') as f:
            f.write(hosts)
        #return '<pre>\n'+hosts+'</pre>'
        command = request.form['command']
        precommand = f"ansible-playbook -i ../ansible/{lab_id}/hosts_rendered.yml ../ansible/{lab_id}/check.yml"
        return run_command(command)

def get_template(id):
    env = Environment(loader=FileSystemLoader(f'../ansible/{id}'))
    template = env.get_template(f'hosts_template.yml')
    return template


if __name__ == '__main__':
    app.run(debug=True)