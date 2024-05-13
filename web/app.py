from flask import Flask, render_template, request, Response, redirect
import subprocess
from jinja2 import Environment, FileSystemLoader
from ansi2html import Ansi2HTMLConverter

app = Flask(__name__)

@app.route('/')
def Lab():
    return render_template('index.html')

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

@app.route('/01', methods=['GET', 'POST'])
def Lab_01():
    if request.method == 'GET':
        return render_template('01.html')
    else:
        lab_id = request.form['lab_id']

        template = get_template(lab_id)

        hosts = template.render(
            # pfsense_ip = request.form['pfsense_ip'],
            # pfsense_user = request.form['pfsense_user'],
            # pfsense_pass = request.form['pfsense_pass'],
            winsrv_ip = request.form['winsrv_ip'],
            winsrv_user = request.form['d_admin_name'],
            winsrv_pass = request.form['d_admin_pass'],
            win7_ip = request.form['win7_ip'],
            win10_ip = request.form['win10_ip'],
            win_user = request.form['l_admin_name'],
            win_pass = request.form['l_admin_pass'],
            user1 = request.form['user1'],
            pass1 = request.form['pass1'],
            user2 = request.form['user2'],
            pass2 = request.form['pass2'],
            user3 = request.form['user3'],
            pass3 = request.form['pass3'],
        )
        
        with open(f'../ansible/{lab_id}/hosts_rendered.ini', 'w+t') as f:
            f.write(hosts)

        command = f"ansible-playbook -i ../ansible/{lab_id}/hosts_rendered.ini ../ansible/{lab_id}/check.yml"
        return run_command(command)

def get_template(id):
    env = Environment(loader=FileSystemLoader(f'../ansible/{id}'))
    template = env.get_template(f'hosts_template.jinja')
    return template


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)