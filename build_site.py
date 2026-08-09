#!/usr/bin/env python3
"""Build docs/index.html — bilingual HR/EN book behind a passphrase gate.

Usage:  BOOK_PASS='phrase' python3 build_site.py
Both language versions are encrypted together; the toggle switches instantly
in the browser with no reload and no second decryption.
"""
import base64, json, os, re, sys, markdown
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

PASS = os.environ.get("BOOK_PASS") or sys.exit("set BOOK_PASS")
ITER = 300000
MD = ["extra", "toc", "sane_lists", "tables"]

def render(path):
    src = open(path, encoding="utf-8").read()
    # <cite index="..."> is editorial bookkeeping, not for the reader
    src = re.sub(r'</?cite[^>]*>', '', src)
    return markdown.markdown(src, extensions=MD)

payload_plain = json.dumps({"en": render("EN.md"), "hr": render("HR.md")})

salt, iv = os.urandom(16), os.urandom(12)
key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32,
                 salt=salt, iterations=ITER).derive(PASS.encode())
ct = AESGCM(key).encrypt(iv, payload_plain.encode("utf-8"), None)

blob = json.dumps({"salt": base64.b64encode(salt).decode(),
                   "iv": base64.b64encode(iv).decode(),
                   "ct": base64.b64encode(ct).decode(),
                   "iter": ITER})

out = open("page_template.html", encoding="utf-8").read().replace("__PAYLOAD__", blob)
os.makedirs("docs", exist_ok=True)
open("docs/index.html", "w", encoding="utf-8").write(out)
print("docs/index.html —", len(out), "bytes")
