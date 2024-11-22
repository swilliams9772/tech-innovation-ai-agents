MONITORING_CONFIG = {
    'log_level': 'INFO',
    'metrics_interval': 300,  # 5 minutes
    'alert_thresholds': {
        'response_time': 5.0,  # seconds
        'error_rate': 0.1,    # 10%
        'memory_usage': 0.9   # 90%
    },
    'performance_targets': {
        'min_success_rate': 0.95,
        'max_response_time': 2.0,
        'min_task_completion': 0.9
    }
} 