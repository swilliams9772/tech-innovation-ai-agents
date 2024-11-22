import logging
from datetime import datetime
from typing import Dict, Any

class SystemMonitor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.metrics: Dict[str, Any] = {}
        self.setup_logging()
        
    def setup_logging(self):
        """Configure logging settings"""
        logging.basicConfig(
            filename=f'logs/mas_system_{datetime.now().strftime("%Y%m%d")}.log',
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
    def track_agent_performance(self, agent_id: str, metrics: Dict[str, Any]):
        """Track individual agent performance metrics"""
        self.metrics[agent_id] = {
            'timestamp': datetime.now(),
            'metrics': metrics
        }
        self.logger.info(f'Agent {agent_id} metrics: {metrics}')
        
    def monitor_system_health(self):
        """Monitor overall system health"""
        system_metrics = {
            'active_agents': len(self.metrics),
            'last_update': datetime.now(),
            'performance_summary': self.calculate_performance_summary()
        }
        self.logger.info(f'System health metrics: {system_metrics}')
        return system_metrics
        
    def calculate_performance_summary(self) -> Dict[str, float]:
        """Calculate summary statistics for system performance"""
        if not self.metrics:
            return {}
            
        summary = {
            'avg_response_time': 0.0,
            'success_rate': 0.0,
            'task_completion_rate': 0.0
        }
        
        # Calculate averages across all agents
        for agent_metrics in self.metrics.values():
            metrics = agent_metrics['metrics']
            summary['avg_response_time'] += metrics.get('response_time', 0)
            summary['success_rate'] += metrics.get('success_rate', 0)
            summary['task_completion_rate'] += metrics.get('completion_rate', 0)
            
        agent_count = len(self.metrics)
        for key in summary:
            summary[key] /= agent_count
            
        return summary 