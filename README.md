# ADHD Cure

A real-time focus detection system that uses your webcam to monitor head position and plays escalating audio alerts when you get distracted. Built for people with ADHD who need a nudge (or a shove) to stay on task.

## How It Works

1. Your webcam tracks your head pose using MediaPipe face landmarks
2. A 3-second calibration learns your "normal" focused position
3. When you look away, a grace period gives you a moment before alerting
4. Alerts escalate through 3 levels if you stay distracted — from a subtle Metal Gear Solid alert to Gordon Ramsay yelling at you

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run
python main.py
```

The app will open your webcam, calibrate for 3 seconds (look at your screen), and start monitoring.

## Controls

| Key | Action |
|-----|--------|
| `q` | Quit |
| `s` | Toggle settings panel |
| `r` | Recalibrate head position |
| `1` / `2` / `3` | Preview L1 / L2 / L3 alert sounds |

## CLI Options

```
--no-debug            Hide the camera debug window
--skip-calibration    Skip calibration, use absolute thresholds
--threshold-yaw N     Yaw deviation threshold in degrees (default: 30)
--threshold-pitch-down N   Pitch down threshold (default: 15)
--threshold-pitch-up N     Pitch up threshold (default: 20)
--grace-period N      Grace period in seconds (default: 3)
--cooldown N          Alert cooldown in seconds (default: 10)
```

## Alert Sounds

15 built-in sounds including:

- **Metal Gear Solid alert** (L1 default)
- **JonTron "Excuse Me, What?"** (L2 default)
- **"Get Back To Work"** (L3 default)
- Gordon Ramsay, Shrek, GTA Wasted, Navi "Hey Listen!", Vine Boom, and more

All sound selections and settings persist across sessions via `settings.json`.

## Architecture

| File | Purpose |
|------|---------|
| `main.py` | Camera capture, UI overlays, settings panel |
| `detector.py` | Head pose estimation via MediaPipe + PnP solver |
| `alerter.py` | State machine with grace period and 3-level escalation |
| `config.py` | Centralized settings with JSON persistence |

## Requirements

- Python 3.9+
- Webcam
- macOS (uses `afplay` for audio — swap for `aplay`/`ffplay` on Linux)
