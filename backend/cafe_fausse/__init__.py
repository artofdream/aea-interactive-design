"""Café Fausse Flask app (FR-18). Modular factory; documented for NFR-9."""

from __future__ import annotations

import os
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

from cafe_fausse.content import OFFICIAL_IMAGE_FILES, REPO_ROOT, freeze
from cafe_fausse.db import DatabaseUnavailable, ping
from cafe_fausse.newsletter import subscribe as subscribe_newsletter
from cafe_fausse.reservations import (
    ReservationError,
    create_reservation,
    remaining_tables,
)
from cafe_fausse.slots import list_slots_for_date, parse_time_slot

DIST_DIR = REPO_ROOT / "frontend" / "dist"
IMAGE_DIR = REPO_ROOT / "assets" / "images"


def create_app() -> Flask:
    app = Flask(__name__, static_folder=None)
    app.config["JSON_SORT_KEYS"] = False

    CORS(
        app,
        resources={r"/api/*": {"origins": ["http://127.0.0.1:5173", "http://localhost:5173"]}},
    )

    @app.errorhandler(DatabaseUnavailable)
    def _db_unavailable(exc: DatabaseUnavailable):
        return jsonify({"ok": False, "error": str(exc)}), 503

    @app.get("/api/health")
    def health():
        ping()
        return jsonify({"ok": True})

    @app.get("/api/menu")
    def menu():
        return jsonify({"ok": True, "menu": freeze["menu"]})

    @app.get("/api/site")
    def site():
        return jsonify(
            {
                "ok": True,
                "name": freeze["name"],
                "address": freeze["address"],
                "phone": freeze["phone"],
                "hoursDisplay": freeze["hoursDisplay"],
                "history": freeze["history"],
                "locallySourced": freeze["locallySourced"],
                "founders": freeze["founders"],
                "awards": freeze["awards"],
                "reviews": freeze["reviews"],
                "officialImages": freeze["officialImages"],
                "tableCount": freeze["tableCount"],
            }
        )

    @app.get("/api/slots")
    def slots():
        date_str = (request.args.get("date") or "").strip()
        if not date_str:
            return jsonify({"ok": False, "error": "Query parameter date is required (YYYY-MM-DD)."}), 400
        try:
            slots_iso = list_slots_for_date(date_str)
        except ValueError as exc:
            return jsonify({"ok": False, "error": str(exc)}), 400
        return jsonify({"ok": True, "slots": slots_iso})

    @app.get("/api/availability")
    def availability():
        raw = (request.args.get("time_slot") or "").strip()
        try:
            slot = parse_time_slot(raw)
        except ValueError as exc:
            return jsonify({"ok": False, "error": str(exc)}), 400
        remaining = remaining_tables(slot)
        return jsonify(
            {
                "ok": True,
                "time_slot": slot.isoformat(),
                "remaining": remaining,
                "table_count": freeze["tableCount"],
                "fully_booked": remaining == 0,
            }
        )

    @app.post("/api/reservations")
    def reservations_create():
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"ok": False, "error": "JSON body is required."}), 400
        try:
            result = create_reservation(payload)
        except ReservationError as exc:
            return jsonify({"ok": False, "error": str(exc), "code": exc.code}), exc.status
        return jsonify({"ok": True, **result}), 201

    @app.post("/api/newsletter")
    def newsletter_create():
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"ok": False, "error": "JSON body is required."}), 400
        try:
            result = subscribe_newsletter(payload)
        except ReservationError as exc:
            return jsonify({"ok": False, "error": str(exc), "code": exc.code}), exc.status
        return jsonify({"ok": True, **result}), 201

    @app.get("/images/<path:filename>")
    def official_image(filename: str):
        name = Path(filename).name
        if name not in OFFICIAL_IMAGE_FILES:
            return jsonify({"ok": False, "error": "Unknown image."}), 404
        return send_from_directory(IMAGE_DIR, name)

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def spa(path: str):
        if path.startswith("api/") or path.startswith("images/"):
            return jsonify({"ok": False, "error": "Not found."}), 404
        if DIST_DIR.is_dir():
            candidate = (DIST_DIR / path).resolve()
            if path and candidate.is_file() and DIST_DIR.resolve() in candidate.parents:
                return send_from_directory(DIST_DIR, path)
            index = DIST_DIR / "index.html"
            if index.is_file():
                return send_from_directory(DIST_DIR, "index.html")
        return (
            jsonify(
                {
                    "ok": False,
                    "error": (
                        "Frontend build is not present. Run npm install && npm run build "
                        "in frontend/, or use the Vite dev server (see README)."
                    ),
                }
            ),
            503,
        )

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", "5000")))
