"""VOID.Bounty — Triage Agent Tests"""
import pytest
from agents.triage import triage_report, Severity

def test_rce_is_critical():
    result = triage_report("RCE vulnerability found", "remote code execution via upload endpoint", "steps...")
    assert result.severity == Severity.CRITICAL

def test_xss_is_high():
    result = triage_report("Stored XSS in comments", "xss payload executes on page load", "inject <script>")
    assert result.severity == Severity.HIGH

def test_clickjacking_is_low():
    result = triage_report("Clickjacking possible", "missing X-Frame-Options header", "iframe the site")
    assert result.severity == Severity.LOW

def test_confidence_in_range():
    result = triage_report("Test", "test", "test")
    assert 0.0 <= result.confidence <= 1.0
