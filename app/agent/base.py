def state_context(self):
    previous_state = self.state
    try:
        # Execution logic
        yield
    finally:
        if self.state == AgentState.RUNNING:
            self.state = previous_state
