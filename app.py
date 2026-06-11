from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os


class AppHandler(BaseHTTPRequestHandler):
    def _send_response(self, status_code, body, content_type="text/plain; charset=utf-8"):
        encoded_body = body.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(encoded_body)))
        self.end_headers()
        self.wfile.write(encoded_body)

    def do_GET(self):
        if self.path == "/":
            html = """<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>App de prueba</title>
  <style>
    body {
      margin: 0;
      min-height: 100vh;
      display: grid;
      place-items: center;
      font-family: Arial, sans-serif;
      background: #f3f6fb;
      color: #1f2937;
    }

    main {
      width: min(90vw, 560px);
      padding: 32px;
      border: 1px solid #d9e2ef;
      border-radius: 8px;
      background: white;
      box-shadow: 0 10px 30px rgba(31, 41, 55, 0.08);
    }

    h1 {
      margin-top: 0;
      color: #0f766e;
    }

    code {
      padding: 2px 6px;
      border-radius: 4px;
      background: #eef2f7;
    }
  </style>
</head>
<body>
  <main>
    <h1>Aplicacion MONTAJES DELSAZ</h1>
    <p>Si puedes ver esta pagina, el servidor Python esta respondiendo correctamente.</p>
    <p>Endpoint de prueba: <code>/health</code></p>
  </main>
</body>
</html>"""
            self._send_response(200, html, "text/html; charset=utf-8")
            return

        if self.path == "/health":
            payload = {"status": "ok", "message": "Servidor activo"}
            self._send_response(200, json.dumps(payload), "application/json; charset=utf-8")
            return

        self._send_response(404, "No encontrado")


def main():
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    server = HTTPServer((host, port), AppHandler)
    print(f"Servidor escuchando en http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
