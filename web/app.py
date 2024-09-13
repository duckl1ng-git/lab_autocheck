from flask import Flask, render_template, request, Response
import subprocess
from jinja2 import Environment, FileSystemLoader
from ansi2html import Ansi2HTMLConverter
from mapping import mapping

app = Flask(__name__)

# Main page
@app.route('/')
def Lab():
    return render_template('index.html')

# Lab page
@app.route('/<id>', methods=['GET', 'POST'])
def Lab_N(id):
    if request.method == 'GET':
        return render_template(f'{id}.html')
    else:
        template = get_template(id)

        values = mapping[int(id) - 1]

        for k in values:
            values[k] = request.form[k]

        hosts = template.render(values)

        # hosts = template.render(
        #     # pfsense_ip = request.form['pfsense_ip'],
        #     # pfsense_user = request.form['pfsense_user'],
        #     # pfsense_pass = request.form['pfsense_pass'],
        #     winsrv_ip = request.form['winsrv_ip'],
        #     winsrv_user = request.form['d_admin_name'],
        #     winsrv_pass = request.form['d_admin_pass'],
        #     win7_ip = request.form['win7_ip'],
        #     win10_ip = request.form['win10_ip'],
        #     win_user = request.form['l_admin_name'],
        #     win_pass = request.form['l_admin_pass'],
        #     user1 = request.form['user1'],
        #     pass1 = request.form['pass1'],
        #     user2 = request.form['user2'],
        #     pass2 = request.form['pass2'],
        #     user3 = request.form['user3'],
        #     pass3 = request.form['pass3'],
        # )
            
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
    app.run(debug=True, host="0.0.0.0", port=80)