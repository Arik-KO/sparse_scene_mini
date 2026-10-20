import csv
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def make_out_dir(script_name, data_version):
    out_dir = PROJECT_ROOT/"work_dirs"/"explore"/script_name/data_version
    out_dir.mkdir(parents=True, exists_ok=True)
    return out_dir


def save_figure(fig, out_dir, name):
    fig.savefig(out_dir/ f"{name}.pdf", bbox_inches="tight")
    fig.savefig(out_dir/f"{name}.png", dpi=300, bbox_inches="tight")


def save_csv(rows, out_dir, name):
    path = out_dir/ f"{name}".csv
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames= list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(eows)
    return path


def save_json(data, out_dir, name):
    path = out_dir / f"{name}".json
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path
