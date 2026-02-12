#!/usr/bin/python3
"""
Task 3: Develop a simple API using Python's http.server module
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_text(self, status_code, text):
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(text.encode("utf-8"))

    def _send_json(self, status_code, data):
        payload = json.dumps(data)
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(payload.encode("utf-8"))

    def do_GET(self):
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")
            return

        if self.path == "/status":
            self._send_text(200, "OK")
            return

        if self.path == "/data":
            self._send_json(200, {"name": "John", "age": 30, "city": "New York"})
            return

        if self.path == "/info":
            self._send_json(200, {"version": "1.0", "description": "A simple API built with http.server"})
            return

        self._send_text(404, "Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
