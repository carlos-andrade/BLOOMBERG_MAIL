import unittest
from scripts.rec001_b3_cotahist_cross_repo_v15 import compare_date_maps

class TestRec001DateMultiset(unittest.TestCase):
    def test_equal_multisets_pass(self):
        x={"20260102":{"count":2,"multiset_sha256":"abc"}}
        dates,bad=compare_date_maps(x,x)
        self.assertEqual(dates,["20260102"])
        self.assertEqual(bad,[])

    def test_changed_hash_fails(self):
        a={"20260102":{"count":2,"multiset_sha256":"abc"}}
        b={"20260102":{"count":2,"multiset_sha256":"xyz"}}
        _,bad=compare_date_maps(a,b)
        self.assertEqual(bad[0]["reason"],"MULTISET_MISMATCH")

    def test_missing_date_fails(self):
        a={"20260102":{"count":2,"multiset_sha256":"abc"}}
        _,bad=compare_date_maps(a,{})
        self.assertEqual(bad[0]["reason"],"DATE_MISSING_ON_ONE_SIDE")

if __name__ == "__main__":
    unittest.main()
