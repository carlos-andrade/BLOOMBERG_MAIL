import unittest
from collections import Counter
from scripts.rec001_b3_cotahist_incremental_v16 import compare_incremental

class IncrementalComparisonTests(unittest.TestCase):
    def test_identical_multisets_pass(self):
        rows = {"20260924": Counter({"a": 2, "b": 1}), "20260925": Counter({"c": 1})}
        dates, diffs = compare_incremental(rows, dict(rows))
        self.assertEqual(dates, ["20260924", "20260925"])
        self.assertEqual(diffs, [])

    def test_multiplicity_mismatch_detected(self):
        left = {"20260924": Counter({"a": 2})}
        right = {"20260924": Counter({"a": 1})}
        dates, diffs = compare_incremental(left, right)
        self.assertEqual(dates, ["20260924"])
        self.assertEqual(diffs[0]["reason"], "MULTISET_MISMATCH")

    def test_missing_date_detected(self):
        dates, diffs = compare_incremental({"20260924": Counter({"a": 1})}, {})
        self.assertEqual(diffs[0]["reason"], "DATE_MISSING_ON_ONE_SIDE")

    def test_baseline_dates_excluded(self):
        dates, diffs = compare_incremental({"20260923": Counter({"a": 1})}, {})
        self.assertEqual(dates, [])
        self.assertEqual(diffs, [])

    def test_newer_official_dates_do_not_extend_local_target_period(self):
        local = {"20260924": Counter({"a": 1})}
        official = {"20260924": Counter({"a": 1}), "20260925": Counter({"b": 1})}
        dates, diffs = compare_incremental(local, official)
        self.assertEqual(dates, ["20260924"])
        self.assertEqual(diffs, [])

if __name__ == "__main__":
    unittest.main()
