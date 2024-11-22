import unittest
from unittest.mock import Mock
from automation_agent import AutomationAgent

class TestAutomationAgent(unittest.TestCase):
    def setUp(self):
        self.capabilities = ['data_analysis', 'task_scheduling']
        self.agent = AutomationAgent('analyst', self.capabilities)
        
    def test_task_assignment(self):
        """Test if tasks are correctly assigned based on capabilities"""
        # Create a mock task
        task = Mock()
        task.required_capabilities = ['data_analysis']
        
        # Test task assignment
        self.assertTrue(self.agent.assign_task(task))
        self.assertEqual(len(self.agent.tasks), 1)
        
    def test_capability_check(self):
        """Test capability verification"""
        task = Mock()
        task.required_capabilities = ['invalid_capability']
        
        self.assertFalse(self.agent.can_handle(task)) 