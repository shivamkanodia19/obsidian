"""
ML Model Scorer — honest stub.

DO NOT fake scores. DO NOT invent accuracy numbers. DO NOT pretend training happened.

This module exists so the interface is defined before any model exists.
When real labeled data from paper trading is available (V6+), a real model can be
plugged in here without changing any calling code.

Current state: always returns 'not_available'.
"""

from __future__ import annotations

from .schemas import ModelScore, TradeProposal
from ..utils.logging import get_logger

logger = get_logger(__name__)


class ModelScorer:
    """
    Scores trade proposals using a trained ML model.

    V0: not available. Returns transparent placeholder.
    V6+: replace score() with a real model (XGBoost, logistic regression, etc.)
         trained on labeled paper trade data.

    What a real model would need:
    - 100+ labeled paper trades with outcomes
    - Feature engineering: spread %, volume, thesis age, market regime, etc.
    - Out-of-sample validation (not just in-sample accuracy)
    - Regular retraining as market conditions change
    - Confidence calibration (P(outcome) must actually mean something)
    """

    def score(self, proposal: TradeProposal) -> ModelScore:
        """
        Score a trade proposal. V0: always returns not_available.
        """
        logger.debug(
            f"ModelScorer.score() called for {proposal.asset_or_market} — "
            f"returning not_available (V0 stub)"
        )
        return ModelScore(
            proposal_id=proposal.id,
            available=False,
            probability_of_positive_outcome=None,
            expected_value=None,
            setup_quality=None,
            liquidity_risk=None,
            confidence_calibration=None,
            model_version="not_available",
            note=(
                "No ML model exists yet. This system has not been trained. "
                "Do not treat this placeholder as a signal. "
                "Real model requires 100+ labeled trades and out-of-sample validation."
            ),
        )

    def is_available(self) -> bool:
        return False


# Module-level singleton
_scorer: ModelScorer | None = None


def get_scorer() -> ModelScorer:
    global _scorer
    if _scorer is None:
        _scorer = ModelScorer()
    return _scorer
