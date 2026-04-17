import datetime
import redis
from flask import (
    Flask,
    Response,
    request,
)
from decouple import config


app = Flask(__name__)
app.secret_key = config('SECRET_KEY')
r = redis.Redis(host='localhost', port=6379, db=0)


@app.route('/post', methods=['POST'])
def post():
    message = request.form['message']
    user = request.form['user']
    channel = request.form['channel']

    now = datetime.datetime.now().replace(microsecond=0).time()
    r.publish(channel, '[%s][%s]: %s' % (now.isoformat(), user, message))
    return Response(status=204)


def event_stream(channel):
    pubsub = r.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe(channel)
    for message in pubsub.listen():
        yield f"{message['data']}\n\n"


@app.route('/stream')
def stream():
    channel = request.args.get('channel')
    return Response(event_stream(channel), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run()