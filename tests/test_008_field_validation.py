import unittest

from payer_contract_checker.models import Record
from payer_contract_checker.scoring import score_record


class DepthCheck8(unittest.TestCase):
    def test_008_field_validation(self):
        record = Record(id="line-008", exposure=44555, signal=0.637, urgency=9)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
