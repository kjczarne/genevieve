import unittest
from genevieve import generate_pwsh, generate_sh, parse_yaml
from pathlib import Path


class TestGenevieve(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.parsed_yaml = parse_yaml(Path(__file__).parent / "test.yaml")
        cls.expected_bash = Path(__file__).parent / "xout_bash.txt"
        cls.expected_pwsh = Path(__file__).parent / "xout_pwsh.txt"

    def test_bash_output(self):
        out = generate_sh(self.parsed_yaml, "variables")
        with open(self.expected_bash, "r") as f:
            expected = f.read()
        self.assertEqual(out, expected)

    def test_powershell_output(self):
        out = generate_pwsh(self.parsed_yaml, "variables")
        with open(self.expected_pwsh, "r") as f:
            expected = f.read()
        self.assertEqual(out, expected)


if __name__ == "__main__":
    unittest.main()
