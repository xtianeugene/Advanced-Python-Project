from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()
clients = []

HTML = """
<script>
    var ws = new Websocket("ws://localhost:8080/ws");
    ws.onmessage = e => document.body.innerHTML += e.data + "<br>";
    function send() { ws.send(document.getElementById("m").value); }
</script>

<input id="m"><button onclick="send()">Send</button>
"""

@app.get("/")
def root(): return HTMLResponse(content=HTML)

@app.websocket("/ws")
async def ws(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            msg = await websocket.receive_text()
            for c in clients:
                await c.send(msg)
    finally:
        clients.remove(websocket)
