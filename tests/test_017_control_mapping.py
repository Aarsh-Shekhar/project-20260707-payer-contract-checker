import unittest

from payer_contract_checker.models import Record
from payer_contract_checker.scoring import score_record


class DepthCheck17(unittest.TestCase):
    def test_017_control_mapping(self):
        record = Record(id="line-017", exposure=41560, signal=0.342, urgency=8)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
