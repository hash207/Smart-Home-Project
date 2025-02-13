from pyngrok import ngrok, conf
import os

# Configure ngrok to use a local directory
home_dir = os.path.expanduser("~")
ngrok_path = os.path.join(home_dir, "ngrok_bin")
os.makedirs(ngrok_path, exist_ok=True)
conf.get_default().ngrok_path = os.path.join(ngrok_path, "ngrok")

# Start ngrok tunnel
url = ngrok.connect(5000)
print(f'Ngrok tunnel is running at: {url}')

# Keep the tunnel open
ngrok_process = ngrok.get_ngrok_process()
try:
    ngrok_process.proc.wait()
except KeyboardInterrupt:
    print("Shutting down tunnel...")
    ngrok.kill()
