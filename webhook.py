from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Received alert, triggering Ansible...")
        subprocess.run(["ansible-playbook", "heal.yml"])

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 5001), Handler)
    print("Listening on port 5001 for alerts...")
    server.serve_forever()
