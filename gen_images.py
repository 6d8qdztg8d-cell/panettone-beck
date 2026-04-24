#!/usr/bin/env python3
import requests, time, json, sys, os

API_KEY = "a359f5c03242ed0499e097ad71f02d4d"
BASE_URL = "https://api.kie.ai/api/v1/jobs"
OUT_DIR = os.path.join(os.path.dirname(__file__), "images")
os.makedirs(OUT_DIR, exist_ok=True)

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

STYLE = (
    "ultra premium editorial food photography, dark moody atmosphere, "
    "warm golden accent lighting, dark marble or stone surfaces, "
    "deep shadows, rich textures, luxury Swiss bakery, cinematic, "
    "high-end magazine quality, no text, no logos"
)

IMAGES = [
    {
        "name": "hero",
        "prompt": f"Artisan sourdough bread freshly baked on dark marble counter, dramatic chiaroscuro lighting, single warm golden light source, thick crust with beautiful score marks, flour dusting, ultra detailed, {STYLE}",
        "ratio": "16:9"
    },
    {
        "name": "panettone",
        "prompt": f"Luxury Italian panettone on dark stone surface, golden crust, candied fruits visible in cross-section, warm glowing backlight, soft bokeh background, {STYLE}",
        "ratio": "16:9"
    },
    {
        "name": "hausbrot",
        "prompt": f"Rustic sourdough loaf with deep decorative score marks on dark linen cloth, dramatic side lighting, dark background, close-up artisan bread photography, {STYLE}",
        "ratio": "3:4"
    },
    {
        "name": "feingebaeck",
        "prompt": f"Stack of perfectly baked butter croissants, flaky golden layers, dark background, warm atmospheric light, extreme close-up, {STYLE}",
        "ratio": "1:1"
    },
    {
        "name": "saisonal",
        "prompt": f"Wide cinematic spread of artisan breads pastries and seasonal baked goods on long dark wooden table, warm candlelight atmosphere, bakery interior, multiple products, {STYLE}",
        "ratio": "16:9"
    },
    {
        "name": "backstube",
        "prompt": f"Baker's skilled hands shaping bread dough on dark stone counter, flour dusting in air, dramatic overhead lighting, warm atmospheric kitchen, artisan craft, {STYLE}",
        "ratio": "1:1"
    },
]

def generate(img):
    name = img["name"]
    out_path = os.path.join(OUT_DIR, f"{name}.jpg")
    if os.path.exists(out_path):
        print(f"[{name}] already exists, skipping.")
        return True

    print(f"\n[{name}] Creating task...")
    payload = {
        "model": "nano-banana-2",
        "input": {
            "prompt": img["prompt"],
            "aspect_ratio": img["ratio"],
            "resolution": "1K",
            "output_format": "jpg"
        }
    }

    try:
        r = requests.post(f"{BASE_URL}/createTask", headers=HEADERS, json=payload, timeout=30)
        r.raise_for_status()
        result = r.json()
    except Exception as e:
        print(f"[{name}] ERROR creating task: {e}")
        if 'r' in dir() and r is not None:
            print(r.text[:500])
        return False

    task_id = result.get("data", {}).get("taskId")
    if not task_id:
        print(f"[{name}] ERROR: No taskId. Response: {result}")
        return False

    print(f"[{name}] Task ID: {task_id} — polling...")

    for attempt in range(90):
        time.sleep(4)
        try:
            pr = requests.get(f"{BASE_URL}/recordInfo", headers=HEADERS, params={"taskId": task_id}, timeout=15)
            pr.raise_for_status()
            data = pr.json().get("data", {})
        except Exception as e:
            print(f"[{name}] Poll {attempt+1} error: {e}")
            continue

        state = data.get("state", "unknown")
        print(f"[{name}] Poll {attempt+1}: {state}")

        if state in ("success", "completed"):
            try:
                result_json = json.loads(data.get("resultJson", "{}"))
                urls = result_json.get("resultUrls", [])
                if not urls:
                    print(f"[{name}] No URLs in result")
                    return False
                img_r = requests.get(urls[0], timeout=30)
                img_r.raise_for_status()
                with open(out_path, "wb") as f:
                    f.write(img_r.content)
                print(f"[{name}] Saved → images/{name}.jpg")
                return True
            except Exception as e:
                print(f"[{name}] Download error: {e}")
                return False

        elif state in ("failed", "error"):
            print(f"[{name}] Task failed: {json.dumps(data, indent=2)}")
            return False

    print(f"[{name}] Timeout after 6 min")
    return False

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else None
    jobs = [i for i in IMAGES if not target or i["name"] == target]
    ok = sum(1 for i in jobs if generate(i))
    print(f"\nDone: {ok}/{len(jobs)} images generated.")
