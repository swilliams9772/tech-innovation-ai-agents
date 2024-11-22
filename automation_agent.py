class AutomationAgent:
    def __init__(self, role, capabilities):
        self.role = role
        self.capabilities = capabilities
        self.tasks = []
        
    def assign_task(self, task):
        """Assign tasks based on agent capabilities"""
        if self.can_handle(task):
            self.tasks.append(task)
            return True
        return False
        
    def can_handle(self, task):
        """Check if agent has required capabilities"""
        return all(cap in self.capabilities for cap in task.required_capabilities) 