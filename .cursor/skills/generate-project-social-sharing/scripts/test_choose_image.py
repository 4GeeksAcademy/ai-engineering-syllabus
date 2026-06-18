#!/usr/bin/env python3
"""Tests for preview cover image selection."""

from __future__ import annotations

import unittest

from generate_project_social_assets import IMAGE_MAP, choose_image_filename


def learn(slug: str, title_en: str, *, technologies=None, description_en: str = "") -> dict:
    return {
        "slug": slug,
        "title": {"en": title_en},
        "description": {"en": description_en},
        "technologies": technologies or [],
    }


class ChooseImageFilenameTests(unittest.TestCase):
    def test_cover_image_override_wins(self) -> None:
        data = learn("any-slug", "Any title", technologies=["fastapi"])
        data["coverImage"] = "workflow.svg"
        self.assertEqual(choose_image_filename(data), "workflow.svg")

    def test_fastapi_backend_uses_coding_not_communication(self) -> None:
        data = learn(
            "ai-eng-milestone-backend-development",
            "Milestone 5 — Backend: Inventory Management with ORM & Dual Database",
            technologies=["fastapi", "sqlmodel", "postgresql", "supabase"],
        )
        self.assertEqual(choose_image_filename(data), IMAGE_MAP["ai-coding"])

    def test_frontend_backoffice_uses_web_not_communication(self) -> None:
        data = learn(
            "ai-eng-inventory-management-backoffice",
            "Milestone 5 — Backoffice: Inventory Management Interface",
            technologies=["react", "tailwind-css", "frontend"],
        )
        self.assertEqual(choose_image_filename(
            data), IMAGE_MAP["ai-web-development"])

    def test_nextjs_clone_uses_web_not_workflow(self) -> None:
        data = learn(
            "nextjs-airbnb-ui-clone",
            "Building an Airbnb UI Clone with Next.js and React",
            technologies=["next.js", "react", "tailwind-css"],
            description_en=(
                "Build a mobile-first Airbnb UI clone in Next.js 16 using "
                "React components and a vision-to-spec workflow."
            ),
        )
        self.assertEqual(choose_image_filename(
            data), IMAGE_MAP["ai-web-development"])

    def test_container_project_uses_command_line(self) -> None:
        data = learn(
            "ai-eng-container-project",
            "Company Monorepo Containerization",
            technologies=["docker", "fastapi"],
        )
        self.assertEqual(choose_image_filename(
            data), IMAGE_MAP["command-line"])

    def test_data_pipeline_uses_workflow(self) -> None:
        data = learn(
            "designing-data-pipeline",
            "Designing a Data Pipeline: From Raw Data to Reliable Insights",
            technologies=["python", "sql"],
        )
        self.assertEqual(choose_image_filename(data), IMAGE_MAP["workflow"])

    def test_chat_project_uses_communication(self) -> None:
        data = learn(
            "chat-interface-real-ai-api",
            "Talk to the Machine - Building a Chat Interface with a Real AI API",
            technologies=["javascript", "openai"],
        )
        self.assertEqual(choose_image_filename(
            data), IMAGE_MAP["ai-communication"])

    def test_clone_slug_does_not_match_cli(self) -> None:
        data = learn(
            "nextjs-airbnb-ui-clone",
            "UI Clone",
            technologies=["react"],
        )
        self.assertNotEqual(choose_image_filename(data),
                            IMAGE_MAP["command-line"])

    def test_telemetry_plan_uses_workflow(self) -> None:
        data = learn(
            "ai-eng-telemetry-plan",
            "Company's Telemetry plan design",
            technologies=["architecture", "technical-documentation"],
        )
        self.assertEqual(choose_image_filename(data), IMAGE_MAP["workflow"])

    def test_telemetry_capture_uses_web(self) -> None:
        data = learn(
            "ai-eng-telemetry-capture",
            "Company's Telemetry – Frontend capture",
            technologies=["javascript", "frontend"],
        )
        self.assertEqual(choose_image_filename(
            data), IMAGE_MAP["ai-web-development"])

    def test_sql_audit_uses_coding(self) -> None:
        data = learn(
            "edutrack-data-audit-sql",
            "EduTrack Data Audit",
            technologies=["sql", "postgresql"],
            description_en=(
                "Audit the EduTrack enrollments table in Supabase: write 12 SQL queries."
            ),
        )
        self.assertEqual(choose_image_filename(data), IMAGE_MAP["ai-coding"])

    def test_performance_audit_uses_web_not_agent_skills(self) -> None:
        data = learn(
            "ai-eng-performance-web-vitals",
            "Frontend Performance Audit",
            technologies=["nextjs", "react", "lighthouse"],
            description_en=(
                "Audit corporate site and backoffice with Lighthouse and agent skills guidance."
            ),
        )
        self.assertEqual(choose_image_filename(
            data), IMAGE_MAP["ai-web-development"])

    def test_docker_with_nextjs_prefers_command_line(self) -> None:
        data = learn(
            "launch-ready-containerized-mvp",
            "Launch Ready: Containerized MVP from Scratch",
            technologies=["docker", "docker-compose", "fastapi", "nextjs"],
        )
        self.assertEqual(choose_image_filename(
            data), IMAGE_MAP["command-line"])


if __name__ == "__main__":
    unittest.main()
