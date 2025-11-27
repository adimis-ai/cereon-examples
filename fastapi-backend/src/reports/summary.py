# fastapi-backend/src/reports/summary.py

from cereon_sdk.fastapi import (
    BaseCard,
    ChartCardRecord,
    TableCardRecord,
    NumberCardRecord,
)

import os
from fastapi import FastAPI
from dotenv import load_dotenv
from typing import List, AsyncIterable
from datetime import datetime, timedelta

load_dotenv()

CONFIG = {
    "tokens": {
        "npm": os.getenv("NPM_TOKEN"),
        "pypi": os.getenv("PYPI_TOKEN"),
        "github": os.getenv("GITHUB_TOKEN"),
    },
    "packages": {
        "@cereon/dashboard": {
            "url": "https://www.npmjs.com/package/@cereon/dashboard",
            "type": "npm",
            "repo": "https://github.com/adimis-ai/cereon-dashboard",
        },
        "@cereon/recharts": {
            "url": "https://www.npmjs.com/package/@cereon/recharts",
            "type": "npm",
            "repo": "https://github.com/adimis-ai/cereon-recharts",
        },
        "cereon-sdk": {
            "url": "https://pypi.org/project/cereon-sdk/",
            "type": "pypi",
            "repo": "https://github.com/adimis-ai/cereon-sdk",
        },
    },
}

"""
- All 3 packages download counts as a single area chart with 3 areas, if possible should update in real-time (every minute)
- All 3 packages commit history as a single line chart with 3 line, if possible should update in real-time (every minute)
- All 3 packages repo likes as a single horizontal bar chart with 3 bar, if possible should update in real-time (every minute)
"""
