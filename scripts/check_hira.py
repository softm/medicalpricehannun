#!/usr/bin/env python3
"""Low-volume HIRA API connectivity check. Never prints credentials."""
import json, os, sys, urllib.parse, urllib.request, urllib.error
from datetime import datetime, timezone
from pathlib import Path

URL = "https://apis.data.go.kr/B551182/hospInfoServicev2/getHospBasisList"
def main():
    key = os.getenv("HIRA_API_KEY", "").strip()
    if not key:
        print("ERROR: HIRA_API_KEY GitHub secret is missing")
        return 2
    print("::add-mask::" + key)
    # Decoded keys should be passed through urlencode exactly once.
    query = urllib.parse.urlencode({"serviceKey": key, "pageNo": 1, "numOfRows": 1, "_type": "json"})
    req = urllib.request.Request(URL + "?" + query, headers={"User-Agent": "medicalpricehannun/0.1"})
    result = {"checked_at": datetime.now(timezone.utc).isoformat(), "source": "HIRA hospital information API", "endpoint": "hospInfoServicev2/getHospBasisList", "status": "failed"}
    try:
        with urllib.request.urlopen(req, timeout=25) as response:
            raw = response.read(200000).decode("utf-8", errors="replace")
            result["http_status"] = response.status
        try:
            payload = json.loads(raw)
            header = payload.get("response", {}).get("header", {})
            result["result_code"] = str(header.get("resultCode", "unknown"))
            result["result_message"] = str(header.get("resultMsg", ""))[:150]
            result["status"] = "success" if result["result_code"] in ("00", "0") else "api_error"
        except (ValueError, AttributeError):
            import xml.etree.ElementTree as ET
            try:
                root = ET.fromstring(raw)
                code = root.findtext(".//resultCode") or "unknown"
                result["result_code"] = code
                result["result_message"] = (root.findtext(".//resultMsg") or "")[:150]
                result["status"] = "success" if code in ("00", "0") else "api_error"
            except ET.ParseError:
                result["status"] = "unrecognized_response"
    except urllib.error.HTTPError as e:
        result["http_status"] = e.code
        result["status"] = "http_error"
    except Exception as e:
        result["status"] = "connection_error"
        result["error_type"] = type(e).__name__
    Path("reports").mkdir(exist_ok=True)
    Path("reports/hira-check.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["status"] == "success" else 1
if __name__ == "__main__":
    sys.exit(main())
