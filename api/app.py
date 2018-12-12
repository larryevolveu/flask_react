import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='react_app/build')

# Serve React App
default_page = 'index.html'
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    print('--path--', path)
    if path != "" and os.path.exists('react_app/build/' + path):
        return send_from_directory('react_app/build', path)
    elif os.path.exists('react_app/build/' + default_page):
        return send_from_directory('react_app/build', default_page)
    else:
        return 'I could not find what you were looking for in "react_app/build": ' + path;

    return('<h1>Nothing to serve</h1><br>' + path)


@app.route('/api/<name>')
@app.route('/api/<name>/')
def api(name):
    return('should be running api:' + name)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print('*** ---- Starting from __main__ port:', port)
    # app.run(use_reloader=True, port=5000, threaded=True)
    # app.run(use_reloader=True, port=port, threaded=True)
    app.run(use_reloader=True, threaded=True,  host='0.0.0.0')
    