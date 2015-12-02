from scipy import integrate
from ..approximate_kernel_density import ApproximateKernelDensity
import unittest

class TestApproximateKernelDensity(unittest.TestCase):
    def setUp(self):
        self.model = ApproximateKernelDensity([
            2.3, 5.0, 15.8, 16.2, 17.1, 19.2, 31.2
        ])

    def test_pdf(self):
        self.assertTrue(self.model.pdf(6.3) < 0.025)
        self.assertTrue(self.model.pdf(6.3) > 0.024)

        self.assertTrue(self.model.pdf(12.2) > 0.0001)
        self.assertTrue(self.model.pdf(12.2) < 0.00011)

        self.assertTrue(self.model.pdf(18.1) < 0.0792)
        self.assertTrue(self.model.pdf(18.1) > 0.0790)

    def test_total_pdf_not_insane(self):
        total, err = integrate.quad(self.model.pdf, -100.0, 200.0)
        self.assertTrue(total > 0.9990)
        self.assertTrue(total < 1.0001)

