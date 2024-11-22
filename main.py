from agents.automation_agent import AutomationAgent
from agents.decision_agent import DecisionAgent
from system_coordinator import MASCoordinator
from monitoring.system_monitor import SystemMonitor

def main():
    # Initialize the coordinator
    coordinator = MASCoordinator()
    
    # Create agents
    automation_agent = AutomationAgent(
        role="data_processor",
        capabilities=["data_analysis", "task_scheduling", "automation"]
    )
    
    decision_agent = DecisionAgent(
        data_sources=[
            # Add your data sources here
            # Example: DatabaseSource(), APISource(), etc.
        ]
    )
    
    # Register agents with the coordinator
    coordinator.register_agent("automation_1", automation_agent)
    coordinator.register_agent("decision_1", decision_agent)
    
    # Start system operation
    try:
        while True:
            # Coordinate agent actions
            coordinator.coordinate_actions()
            
            # Monitor system health
            health_metrics = coordinator.get_system_health()
            print(f"System Health: {health_metrics}")
            
    except KeyboardInterrupt:
        print("Shutting down system...")

if __name__ == "__main__":
    main() 