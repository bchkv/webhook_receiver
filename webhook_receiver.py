from flask import Flask, request, abort
import subprocess

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        try:
            print("GOT SOME HOOKS!!!")
            # subprocess.check_call('./deploy.sh', shell=True)
            return 'Success', 200
        except subprocess.CalledProcessError as error:
            print(f'Error while executing deploy.sh: {error}')
            abort(500)
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='34.16.137.83', port=3000)
