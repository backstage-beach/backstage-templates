from flask import Flask, jsonify
import boto3
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "${{ values.name }} is running!"

@app.route('/health')
def health():
    return jsonify(status="healthy")

@app.route('/ready')
def ready():
    return jsonify(status="ready")

@app.route('/s3/buckets')
def list_buckets():
    try:
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        buckets = [bucket['Name'] for bucket in response.get('Buckets', [])]
        return jsonify(buckets=buckets)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', ${{ values.container_port }}))
    app.run(host='0.0.0.0', port=port)
