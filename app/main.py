import os

from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse

APP_SLUG = os.environ.get("APP_SLUG", "app")
APP_ENV = os.environ.get("APP_ENV", "dev")
PREFIX = f"/{APP_SLUG}-{APP_ENV}"

app = FastAPI()
router = APIRouter(prefix=PREFIX)

_ENV_COLOURS = {"dev": "#2563eb", "tst": "#d97706", "prd": "#16a34a"}
_ENV_COLOUR = _ENV_COLOURS.get(APP_ENV, "#6b7280")

_PAGE = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{APP_SLUG}</title>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: #0f172a;
      color: #f1f5f9;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }}
    .card {{
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 16px;
      padding: 48px 56px;
      text-align: center;
      max-width: 480px;
      width: 90%;
    }}
    .badge {{
      display: inline-block;
      background: {_ENV_COLOUR}22;
      color: {_ENV_COLOUR};
      border: 1px solid {_ENV_COLOUR}55;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 4px 14px;
      margin-bottom: 24px;
    }}
    h1 {{
      font-size: 2rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      margin-bottom: 12px;
    }}
    p {{
      color: #94a3b8;
      font-size: 0.95rem;
      line-height: 1.6;
    }}
    .dot {{
      display: inline-block;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #22c55e;
      margin-right: 6px;
      animation: pulse 2s infinite;
    }}
    .status {{
      margin-top: 32px;
      font-size: 0.85rem;
      color: #64748b;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
    }}
    @keyframes pulse {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0.4; }}
    }}
  </style>
</head>
<body>
  <div class="card">
    <div class="badge">{APP_ENV}</div>
    <h1>{APP_SLUG}</h1>
    <p>Your application is up and running on the PostNord App Platform.</p>
    <div class="status"><span class="dot"></span> Healthy</div>
  </div>
</body>
</html>"""


@router.get("/", response_class=HTMLResponse)
def root():
    return _PAGE


@router.get("/health")
def health():
    return {"status": "ok"}


app.include_router(router)
