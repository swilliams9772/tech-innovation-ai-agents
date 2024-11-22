from agents.automation_agent import AutomationAgent
from tasks.custom_task import Task

def agent_example():
    # Create an agent with specific capabilities
    agent = AutomationAgent(
        role="data_processor",
        capabilities=["data_analysis", "task_scheduling"]
    )
    
    # Create a task
    task = Task(
        name="process_dataset",
        required_capabilities=["data_analysis"],
        parameters={"dataset": "example_data.csv"}
    )
    
    # Assign task to agent
    if agent.assign_task(task):
        print(f"Task assigned successfully")
    else:
        print(f"Agent cannot handle this task") 