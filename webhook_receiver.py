from flask import Flask, request, abort
import subprocess

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        try:
            subprocess.check_call('deploy_sandra-russian-tutor-bot.sh', shell=True)
            return 'Success', 200
        except subprocess.CalledProcessError as error:
            print(f'Error while executing deploy_sandra-russian-tutor-bot.sh: {error}')
            abort(500)
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

#test