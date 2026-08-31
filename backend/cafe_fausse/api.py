"""HTTP API for reservations and newsletter signup (FR-18, NFR-6)."""

from datetime import date

from flask import Flask, jsonify, request
from flask_cors import CORS

from cafe_fausse.db import ping
from cafe_fausse.errors import ApiError, DatabaseUnavailable
from cafe_fausse.newsletter import subscribe
from cafe_fausse.reservations import create_reservation, remaining_tables
from cafe_fausse.slots import isoformat_local, slots_for_date


def _error_body(exc):
    return {"ok": False, "error": exc.code, "message": exc.message}


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.errorhandler(ApiError)
    def handle_api_error(exc):
        return jsonify(_error_body(exc)), exc.status

    @app.errorhandler(404)
    def handle_404(_exc):
        return jsonify({"ok": False, "error": "not_found", "message": "That API path does not exist."}), 404

    @app.errorhandler(405)
    def handle_405(_exc):
        return jsonify({"ok": False, "error": "method_not_allowed", "message": "That method is not allowed."}), 405

    @app.get("/api/health")
    def health():
        up = ping()
        body = {"ok": up, "database": "up" if up else "down"}
        if not up:
            body["message"] = "The database is unavailable. Reservations and newsletter signup are closed."
            return jsonify(body), 503
        return jsonify(body)

    @app.get("/api/slots")
    def list_slots():
        raw = request.args.get("date", "")
        try:
            day = date.fromisoformat(raw)
        except ValueError:
            raise ApiError(400, "invalid_date", "Please choose a valid date (YYYY-MM-DD).")
        try:
            slots = []
            for dt in slots_for_date(day):
                slots.append(
                    {
                        "timeslot": isoformat_local(dt),
                        "tables_remaining": remaining_tables(dt),
                    }
                )
        except DatabaseUnavailable:
            raise
        return jsonify({"ok": True, "date": day.isoformat(), "slots": slots})

    @app.post("/api/reservations")
    def post_reservation():
        payload = request.get_json(silent=True)
        result = create_reservation(payload)
        return jsonify(result), 201

    @app.post("/api/newsletter")
    def post_newsletter():
        payload = request.get_json(silent=True)
        result = subscribe(payload)
        status = 200 if result.get("already_subscribed") else 201
        return jsonify(result), status

    return app
