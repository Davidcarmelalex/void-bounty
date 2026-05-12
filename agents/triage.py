"""
VOID.Bounty — AI Vulnerability Triage Agent

Analyzes vulnerability reports, estimates CVSS severity,
and provides structured triage output for reviewers.
"""
from __future__ import annotations
import logging
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger("void.triage")


class Severity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFORMATIONAL = "informational"


@dataclass
class TriageResult:
    severity: Severity
    cvss_estimate: float
    confidence: float
    summary: str
    recommended_action: str


CRITICAL_KEYWORDS = ["rce", "remote code execution", "authentication bypass", "sql injection", "zero-day"]
HIGH_KEYWORDS = ["xss", "csrf", "idor", "privilege escalation", "data exposure", "path traversal"]
MEDIUM_KEYWORDS = ["information disclosure", "open redirect", "ssrf", "insecure deserialization"]
LOW_KEYWORDS = ["clickjacking", "missing header", "brute force", "rate limit"]


def triage_report(title: str, description: str, steps: str) -> TriageResult:
    """
    Heuristic triage. In production, replace with fine-tuned security LLM.
    """
    text = f"{title} {description} {steps}".lower()

    if any(k in text for k in CRITICAL_KEYWORDS):
        return TriageResult(Severity.CRITICAL, 9.5, 0.75, "Potential critical vulnerability detected", "Immediate review required — escalate to security team")
    if any(k in text for k in HIGH_KEYWORDS):
        return TriageResult(Severity.HIGH, 7.5, 0.70, "High severity vulnerability pattern detected", "Review within 72 hours")
    if any(k in text for k in MEDIUM_KEYWORDS):
        return TriageResult(Severity.MEDIUM, 5.5, 0.65, "Medium severity finding", "Review within 7 days")
    if any(k in text for k in LOW_KEYWORDS):
        return TriageResult(Severity.LOW, 2.5, 0.60, "Low severity finding", "Review within 30 days")
    return TriageResult(Severity.INFORMATIONAL, 0.0, 0.50, "Informational finding — manual review needed", "Acknowledge and review at convenience")
