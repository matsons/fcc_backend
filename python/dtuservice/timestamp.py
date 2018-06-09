from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from dateutil import parser
from datetime import datetime, timezone
import time
import pdb

bp = Blueprint('stamp', __name__)

@bp.route('/api/timestamp/<string:timestamp>', defaults={'timestamp': None})
@bp.route('/api/timestamp/<string:timestamp>')
def service_timestamp(timestamp):
    if not timestamp:
        return jsonify(0)
    try:
        stamp = parser.parse(timestamp)
        return jsonify(unix=int(stamp.replace(tzinfo=timezone.utc).timestamp()*1000), utc=stamp)
    except ValueError:
        return jsonify(error="Invalid Date")

