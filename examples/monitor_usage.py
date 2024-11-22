from monitoring.system_monitor import SystemMonitor
from monitoring.config import MONITORING_CONFIG

def monitor_example():
    monitor = SystemMonitor()
    
    # Track agent performance
    agent_metrics = {
        'response_time': 1.5,
        'success_rate': 0.98,
        'completion_rate': 0.95
    }
    
    monitor.track_agent_performance('agent_1', agent_metrics)
    
    # Get system health
    health_metrics = monitor.monitor_system_health()
    print(f"System Health: {health_metrics}") 