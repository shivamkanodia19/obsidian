from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "trading_cockpit.py"
SPEC = importlib.util.spec_from_file_location("trading_cockpit", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class TradingCockpitTests(unittest.TestCase):
    def test_risk_gate_blocks_oversized_trade(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            paths = MODULE.make_paths_for_testing(root)
            MODULE.ensure_structure(paths)
            MODULE.write_text(paths.policy_path, Path(SCRIPT_PATH.parent / "config" / "risk_policy.toml").read_text(encoding="utf-8"))
            policy = MODULE.load_risk_policy(paths.policy_path)
            MODULE.bootstrap_mock_state(paths)

            proposal = MODULE.build_proposal(
                ticker="NVDA",
                position_size_usd=200.0,
                limit_price=950.0,
                thesis="Too large on purpose.",
                invalidation="Always invalid.",
                time_horizon="1 day",
                confidence="medium",
                strategy_tag="test",
                source_note=None,
                requires_initial_approval=policy.require_initial_approval,
                requires_final_approval=policy.require_final_approval,
            )
            record = MODULE.risk_check_record(proposal, policy, MODULE.bootstrap_mock_state(paths))

            self.assertEqual(record["status"], "fail")
            self.assertTrue(any(check["name"] == "trade-size" and not check["passed"] for check in record["checks"]))

    def test_demo_flow_generates_execution_and_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            paths = MODULE.make_paths_for_testing(root)
            MODULE.ensure_structure(paths)
            MODULE.write_text(paths.policy_path, Path(SCRIPT_PATH.parent / "config" / "risk_policy.toml").read_text(encoding="utf-8"))

            result = MODULE.run_demo(paths, reset=True)

            self.assertEqual(result["risk_status"], "pass")
            self.assertEqual(result["execution_status"], "filled")
            self.assertTrue((paths.snapshot_note_dir / "latest-account-status.md").exists())
            self.assertTrue((paths.executions_data_dir / f"{result['proposal_id']}.json").exists())


if __name__ == "__main__":
    unittest.main()
