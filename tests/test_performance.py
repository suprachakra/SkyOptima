#!/usr/bin/env python3
"""
test_performance.py: Unit tests for performance metrics collection.
"""

import unittest
from src.monitoring.performance_metrics import get_cpu_usage, get_memory_usage

class TestPerformanceMetrics(unittest.TestCase):

    def test_cpu_usage(self):
        cpu = get_cpu_usage()
        self.assertIsInstance(cpu, float)
        self.assertGreaterEqual(cpu, 0)
        self.assertLessEqual(cpu, 100)

    def test_memory_usage(self):
        memory = get_memory_usage()
        self.assertIsInstance(memory, float)
        self.assertGreaterEqual(memory, 0)
        self.assertLessEqual(memory, 100)

if __name__ == '__main__':
    unittest.main()
