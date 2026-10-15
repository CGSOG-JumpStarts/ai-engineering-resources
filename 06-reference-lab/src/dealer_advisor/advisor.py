"""Deterministic, read-only advisor. This module makes no LLM or network calls."""
from __future__ import annotations
from dataclasses import dataclass
from uuid import uuid4
import re
from .catalog import SYNTHETIC_CATALOG

MAX_QUESTION = 280
LOOKUP_TOOL = "lookup_approved_catalog"

class InputError(ValueError):
    def __init__(self, code: str, message: str):
        self.code = code
        super().__init__(message)

@dataclass(frozen=True)
class DemoPrincipal:
    """Trusted only when injected by the local lab host, NEVER a real identity."""
    dealer_id: str
    scopes: frozenset[str]

@dataclass(frozen=True)
class Advice:
    status: str
    answer: str
    source_ids: tuple[str, ...]
    tool_calls: tuple[str, ...]
    request_id: str

    def as_dict(self) -> dict:
        return {
            "status": self.status,
            "answer": self.answer,
            "source_ids": list(self.source_ids),
            "tool_calls": list(self.tool_calls),
            "request_id": self.request_id,
        }


def validate_question(question: object) -> str:
    if not isinstance(question, str):
        raise InputError("invalid_question", "question must be a string")
    normalized = " ".join(question.split())
    if not normalized:
        raise InputError("blank_question", "question cannot be empty")
    if len(normalized) > MAX_QUESTION:
        raise InputError("question_too_long", "question is limited to 280 characters")
    return normalized


def match(pattern: str, question: str) -> bool:
    return re.search(pattern, question, flags=re.IGNORECASE) is not None


class AdviceService:
    """Scope check -> prohibited action -> unsupported claims -> catalog routing."""

    def answer(self, question: object, principal: DemoPrincipal) -> Advice:
        q = validate_question(question)
        rid = uuid4().hex
        if not isinstance(principal, DemoPrincipal) or "advice:read" not in principal.scopes:
            return Advice("denied", "This request is not permitted.", (), (), rid)

        # Fail closed before a supported subject can accidentally authorize a mixed request.
        if match(r"\b(?:another|other)\s+dealer\b|\baccount\s+(?:details|data|status)\b|\b(?:delete|change|modify|update|export|send|email)\s+(?:a\s+|the\s+|my\s+)?(?:dealer|account|customer|record|data|details)\b|\bignore\s+(?:all\s+)?(?:rules|instructions)\b", q):
            return Advice("denied", "This demonstration cannot access or change account records.", (), (), rid)

        # Coverage and policy questions require a human rather than a guessed warranty promise.
        if match(r"\b(?:covered|coverage|guaranteed?|years?|eligible|eligibility|reimbursement|free\s+repair)\b", q):
            return Advice("escalate", "Coverage and policy questions need review by the appropriate support team.", (), (), rid)

        intent = None
        if match(r"\b(?:warranty|claim|support\s+case)\b", q):
            intent = "warranty"
        elif match(r"\b(?:parts?|spare|availability)\b", q):
            intent = "parts"
        elif match(r"\b(?:hours?|opening|open|closing)\b", q):
            intent = "hours"

        if intent is None:
            return Advice("escalate", "I do not have an approved answer for that question. Please contact the support team.", (), (), rid)

        entry = SYNTHETIC_CATALOG[intent]
        return Advice("answered", entry.answer, (entry.source_id,), (LOOKUP_TOOL,), rid)
