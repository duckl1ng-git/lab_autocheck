from flask import Flask, render_template, request, Response
import re, subprocess
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

    if id not in mapping.keys():
        return Response(response="<h2>404 Error</h2>", status=404)

    lab = mapping[id]
    values = lab['vars']

    if request.method == 'GET':
        return render_template('lab.html', lab=lab, id=id)
    else:
        template = get_template(id)

        for k in values:
            if validate(k, request.form[k]):
                values[k] = request.form[k]
            else:
                return "<h1 style='color: red; text-align: center; vartical-align: middle;'>Form validation error!</h1>"

        hosts = template.render(values)
            
        with open(f'../ansible/{id}/hosts_rendered.ini', 'w+t') as f:
            f.write(hosts)

        command = f"ansible-playbook -i ../ansible/{id}/hosts_rendered.ini ../ansible/{id}/check.yml -CD"
        return run_command(command)

def validate(key, value):
    if 'ip' in key:
        ip_regex = r'^([0-9]{1,3}\.){3}[0-9]{1,3}$'
        if not re.match(ip_regex, value):
            return False
        
        octets = value.split('.')
        return all(0 <= int(octet) <= 255 for octet in octets)
    else:
        string_regex = r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:,.<>?/]+$'
        return len(value) <= 20 and re.match(string_regex, value) != None

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