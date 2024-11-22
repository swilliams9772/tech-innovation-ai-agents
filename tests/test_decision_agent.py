import unittest
from unittest.mock import Mock, patch
from decision_agent import DecisionAgent

class TestDecisionAgent(unittest.TestCase):
    def setUp(self):
        self.mock_source = Mock()
        self.agent = DecisionAgent([self.mock_source])
        
    def test_data_analysis(self):
        """Test the data analysis pipeline"""
        # Mock the data source
        self.mock_source.fetch_data.return_value = {'test_data': [1, 2, 3]}
        
        with patch.object(self.agent, 'preprocess') as mock_preprocess:
            with patch.object(self.agent, 'generate_insight') as mock_insight:
                with patch.object(self.agent, 'synthesize_insights') as mock_synth:
                    mock_preprocess.return_value = 'processed_data'
                    mock_insight.return_value = 'insight'
                    mock_synth.return_value = 'final_insight'
                    
                    result = self.agent.analyze_data('test_context')
                    
                    self.assertEqual(result, 'final_insight')
                    mock_preprocess.assert_called_once()
                    mock_insight.assert_called_once() 