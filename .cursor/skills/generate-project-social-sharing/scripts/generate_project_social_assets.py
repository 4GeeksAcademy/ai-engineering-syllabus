#!/usr/bin/env python3
"""Generate project previews and social sharing copy in learn.json."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote


IMAGE_MAP = {
    "command-line": "command-line.svg",
    "workflow": "workflow.svg",
    "ai-communication": "ai-communication.svg",
    "ai-web-development": "ai-web-development.svg",
    "ai-coding": "ai-coding.svg",
    "working-with-ai": "working-with-ai.svg",
}

# Explicit slug overrides beat keyword heuristics when metadata is ambiguous.
SLUG_IMAGE_OVERRIDES = {
    "ai-eng-telemetry-plan": IMAGE_MAP["workflow"],
    "ai-eng-telemetry-storage": IMAGE_MAP["ai-coding"],
    "ai-eng-telemetry-report": IMAGE_MAP["workflow"],
    "ai-eng-telemetry-capture": IMAGE_MAP["ai-web-development"],
    "ai-eng-user-authentication-flows": IMAGE_MAP["ai-web-development"],
    "ai-eng-user-authentication-restore": IMAGE_MAP["ai-web-development"],
    "ai-eng-application-caching": IMAGE_MAP["ai-coding"],
    "ai-eng-backend-serialization": IMAGE_MAP["ai-coding"],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate project cover previews and social-sharing messages "
            "from learn.json metadata."
        )
    )
    parser.add_argument(
        "--project-root",
        default=".",
        help="Repository root path (default: current directory).",
    )
    parser.add_argument(
        "--cover-template",
        default="assets/cover/cover-template.html",
        help="Relative path from project root to cover template HTML.",
    )
    parser.add_argument(
        "--images-dir",
        default="assets/cover/images",
        help="Relative path from project root to SVG image directory.",
    )
    parser.add_argument(
        "--projects-dir",
        default="content/projects",
        help="Relative path from project root to projects directory.",
    )
    parser.add_argument(
        "--author",
        default="by 4Geeks Academy",
        help="Author subtitle shown on covers.",
    )
    parser.add_argument(
        "--preview-filename",
        default="preview.png",
        help="Filename generated inside each project's .learn folder.",
    )
    parser.add_argument(
        "--preview-key",
        default="preview",
        help="learn.json key used to store preview path.",
    )
    parser.add_argument(
        "--absolute-base-url",
        default="https://raw.githubusercontent.com/4GeeksAcademy/ai-engineering-syllabus/main",
        help="Absolute base URL used to build preview URLs.",
    )
    parser.add_argument(
        "--sharing-key",
        default="sharing",
        help="learn.json key used to store social-sharing messages.",
    )
    parser.add_argument(
        "--skip-sharing",
        action="store_true",
        help="Skip writing social-sharing messages to learn.json.",
    )
    parser.add_argument(
        "--sharing-brand",
        default="@4GeeksAcademy",
        help="Brand tag included in sharing messages.",
    )
    parser.add_argument(
        "--sharing-link-template",
        default="https://github.com/4GeeksAcademy/{slug}",
        help=(
            "Template for project URL included in sharing messages. "
            "Use {slug} placeholder."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned operations without writing files.",
    )
    parser.add_argument(
        "--slug",
        default="",
        help="Process only one project slug (default: all projects).",
    )
    return parser.parse_args()


def build_haystack(learn_data: dict) -> str:
    technologies = " ".join(str(t)
                            for t in (learn_data.get("technologies") or []))
    title_obj = learn_data.get("title", {}) or {}
    description_obj = learn_data.get("description", {}) or {}
    title_en = title_obj.get("en", "") or title_obj.get("us", "")
    description_en = description_obj.get(
        "en", "") or description_obj.get("us", "")
    slug = learn_data.get("slug", "")
    return " ".join([technologies, title_en, description_en, slug]).lower()


def contains_token(haystack: str, token: str, *, word_boundary: bool = False) -> bool:
    if not token:
        return False
    if word_boundary:
        return re.search(rf"\b{re.escape(token)}\b", haystack) is not None
    return token in haystack


def contains_any(
    haystack: str,
    tokens: list[str],
    *,
    word_boundary: bool = False,
) -> bool:
    return any(
        contains_token(haystack, token, word_boundary=word_boundary)
        for token in tokens
    )


def choose_image_filename(learn_data: dict) -> str:
    cover_image = learn_data.get("coverImage")
    if isinstance(cover_image, str) and cover_image.strip():
        return cover_image.strip()

    slug = (learn_data.get("slug") or "").lower()
    if slug in SLUG_IMAGE_OVERRIDES:
        return SLUG_IMAGE_OVERRIDES[slug]

    haystack = build_haystack(learn_data)

    if slug in {
        "openclaw-memory",
        "openclaw-skills",
        "openclaw-setup",
        "ai-eng-milestone-choose-company",
        "openclaw-onboarding-agent",
    } or contains_any(
        haystack,
        [
            "personal ai agent",
            "choose your company",
        ],
    ):
        return IMAGE_MAP["working-with-ai"]

    if contains_any(
        haystack,
        [
            "docker",
            "container",
            "containerization",
            "containerized",
        ],
    ):
        return IMAGE_MAP["command-line"]

    if contains_any(
        haystack,
        [
            "data pipeline",
            "class diagram",
            "uml",
            "flowchart",
            "diagram",
            "modeling",
            "architectural",
            "telemetry plan",
            "digital wallet",
            "music playlist",
            "vision-to-spec",
            "ai-driven engineering",
            "ingenieria impulsada",
        ],
    ) or (
        contains_token(haystack, "workflow", word_boundary=True)
        and not contains_any(haystack, ["next.js", "nextjs", "react", "frontend"])
    ):
        if not contains_any(
            haystack,
            ["next.js", "nextjs", "react", "tailwind", "html", "css", "frontend"],
        ):
            return IMAGE_MAP["workflow"]

    if contains_any(
        haystack,
        [
            "next.js",
            "nextjs",
            "react",
            "tailwind",
            "html",
            "css",
            "frontend",
            "backoffice",
            "dashboard",
            "landing",
            "seo",
            "mobile-first",
            "ui clone",
            "web vitals",
            "wanderlust",
            "lighthouse",
        ],
    ):
        return IMAGE_MAP["ai-web-development"]

    if contains_any(
        haystack,
        [
            "bash",
            "shell",
            "terminal",
            "command line",
        ],
    ) or contains_token(haystack, "cli", word_boundary=True):
        return IMAGE_MAP["command-line"]

    if contains_any(
        haystack,
        [
            "chat",
            "conversation",
            "voice",
            "telegram",
            "talk to the machine",
            "talk to your",
        ],
        word_boundary=True,
    ) or contains_token(haystack, "prompt", word_boundary=True) or slug.startswith(
        "openclaw-"
    ):
        return IMAGE_MAP["ai-communication"]

    if contains_any(
        haystack,
        [
            "python",
            "javascript",
            "typescript",
            "fastapi",
            "backend",
            "orm",
            "sqlmodel",
            "postgresql",
            "postgres",
            "supabase",
            "sql",
            "serialization",
            "caching",
            "authentication",
            "incident",
            "coding",
            "script",
            "telemetry storage",
            "supplier directory",
            "inventory management with orm",
        ],
    ) or contains_token(haystack, "llm", word_boundary=True):
        return IMAGE_MAP["ai-coding"]

    return IMAGE_MAP["working-with-ai"]


def encode_query(params: dict[str, str]) -> str:
    query_parts = []
    for key, value in params.items():
        query_parts.append(f"{quote(key, safe='')}={quote(value, safe='')}")
    return "&".join(query_parts)


def run_playwright_screenshot(page_url: str, output_file: Path, dry_run: bool) -> None:
    cmd = [
        "npx",
        "playwright",
        "screenshot",
        "--viewport-size=1024,576",
        "--wait-for-selector=[data-ready=true]",
        page_url,
        str(output_file),
    ]
    if dry_run:
        print("dry_run_command", " ".join(cmd))
        return
    subprocess.run(cmd, check=True)


def get_lang_text(multilang_value: dict | str | None, preferred: list[str]) -> str:
    if isinstance(multilang_value, str):
        return multilang_value
    if not isinstance(multilang_value, dict):
        return ""
    for lang in preferred:
        value = multilang_value.get(lang)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def normalize_hashtag(token: str) -> str:
    cleaned = "".join(ch for ch in token if ch.isalnum())
    return cleaned


def build_hashtags(technologies: list[str]) -> str:
    tags = ["AIEngineering", "LearnPack", "4GeeksAcademy"]
    for tech in technologies:
        normalized = normalize_hashtag(tech)
        if normalized:
            tags.append(normalized)
        if len(tags) >= 6:
            break
    unique_tags = []
    for tag in tags:
        if tag and tag not in unique_tags:
            unique_tags.append(tag)
    return " ".join(f"#{tag}" for tag in unique_tags)


def build_sharing_messages(learn_data: dict, brand: str, link_template: str) -> list[dict[str, str]]:
    slug = (learn_data.get("slug") or "").strip()
    title_obj = learn_data.get("title", {}) or {}
    title_en = get_lang_text(
        title_obj, ["en", "us", "es"]) or slug or "this project"
    title_es = get_lang_text(title_obj, ["es", "en", "us"]) or title_en
    technologies = learn_data.get("technologies", []) or []
    if not isinstance(technologies, list):
        technologies = []
    hashtags = build_hashtags([str(t) for t in technologies])
    share_link = link_template.format(slug=slug) if slug else link_template

    return [
        {
            "en": (
                f"I just completed {title_en} with LearnPack {brand}. "
                f"Check it out: {share_link} {hashtags}"
            ),
            "es": (
                f"Acabo de completar {title_es} con LearnPack {brand}. "
                f"Mira el proyecto: {share_link} {hashtags}"
            ),
        },
        {
            "en": (
                f"Built and shipped: {title_en}. "
                f"Learning by building with {brand}. {share_link} {hashtags}"
            ),
            "es": (
                f"Construido y publicado: {title_es}. "
                f"Aprendiendo con proyectos reales en {brand}. {share_link} {hashtags}"
            ),
        },
    ]


def main() -> int:
    args = parse_args()
    root = Path(args.project_root).resolve()
    template_file = root / args.cover_template
    images_dir = root / args.images_dir
    projects_dir = root / args.projects_dir

    if not template_file.exists():
        print(f"Template not found: {template_file}")
        return 1
    if not images_dir.exists():
        print(f"Images directory not found: {images_dir}")
        return 1
    if not projects_dir.exists():
        print(f"Projects directory not found: {projects_dir}")
        return 1

    learn_files = sorted(projects_dir.glob("*/learn.json"))
    if args.slug:
        learn_files = [
            f for f in learn_files if f.parent.name == args.slug.strip()
        ]
    if not learn_files:
        if args.slug:
            print(
                f"No learn.json found for slug '{args.slug}' in: {projects_dir}")
        else:
            print(f"No learn.json files found in: {projects_dir}")
        return 1

    generated = 0
    updated = 0
    sharing_updated = 0
    skipped = 0

    for learn_file in learn_files:
        with learn_file.open("r", encoding="utf-8") as f:
            learn_data = json.load(f)

        title_obj = learn_data.get("title", {}) or {}
        title_en = title_obj.get("en") or title_obj.get("us")
        if not title_en:
            print("skip_missing_title_en", str(learn_file))
            skipped += 1
            continue

        image_name = choose_image_filename(learn_data)
        image_path = images_dir / image_name
        if not image_path.exists():
            print("skip_missing_image", str(image_path))
            skipped += 1
            continue

        project_dir = learn_file.parent
        learn_dir = project_dir / ".learn"
        output_file = learn_dir / args.preview_filename
        preview_rel_path = str(Path(".learn") / args.preview_filename)
        project_rel_dir = project_dir.relative_to(root).as_posix()
        base_url = args.absolute_base_url.rstrip("/")
        preview_absolute_url = f"{base_url}/{project_rel_dir}/{preview_rel_path}"

        query = encode_query(
            {
                "title": title_en,
                "author": args.author,
                "image": f"./images/{image_name}",
            }
        )
        page_url = f"file://{template_file}?{query}"

        print("generate_preview", str(project_dir), "using_image", image_name)
        if not args.dry_run:
            learn_dir.mkdir(parents=True, exist_ok=True)
        run_playwright_screenshot(page_url, output_file, args.dry_run)
        generated += 1

        learn_data[args.preview_key] = preview_absolute_url
        if args.preview_key != "preview" and "preview" in learn_data:
            del learn_data["preview"]
        if args.preview_key != "preview_url" and "preview_url" in learn_data:
            del learn_data["preview_url"]
        if not args.skip_sharing:
            learn_data[args.sharing_key] = build_sharing_messages(
                learn_data,
                brand=args.sharing_brand,
                link_template=args.sharing_link_template,
            )
            sharing_updated += 1

        if args.dry_run:
            print("dry_run_update_json", str(learn_file),
                  args.preview_key, preview_absolute_url)
            if not args.skip_sharing:
                print("dry_run_update_json", str(learn_file),
                      args.sharing_key, "generated_messages")
        else:
            with learn_file.open("w", encoding="utf-8") as f:
                json.dump(learn_data, f, indent=2, ensure_ascii=False)
                f.write("\n")
        updated += 1

    print("summary_generated", generated)
    print("summary_updated", updated)
    print("summary_sharing_updated", sharing_updated)
    print("summary_skipped", skipped)
    return 0


if __name__ == "__main__":
    sys.exit(main())
