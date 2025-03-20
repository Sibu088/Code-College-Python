# caffeine_chaos.py
import random
import plotly.express as px

class CaffeineChaos:
    def __init__(self):
        self.time_slots = [
            "6 AM: Zombie Fuel", 
            "9 AM: Second Breakfast (but Make It Coffee)", 
            "12 PM: Just to Survive Lunch Meetings", 
            "3 PM: Mid-Afternoon Despair Shot", 
            "8 PM: Definitely Not a Good Idea"
        ]
    
    def simulate_intake(self, num_simulations=500):
        """Simulate caffeine intake throughout the day and plot a humorous histogram."""
        results = [random.choice(self.time_slots) for _ in range(num_simulations)]
        frequencies = [results.count(slot) for slot in self.time_slots]
        
        # Create a bar chart
        fig = px.bar(x=self.time_slots, y=frequencies, title="Caffeine Chaos: Daily Coffee Dependence Histogram",
                     labels={'x': 'Time of Day', 'y': 'Cups of Coffee'}, color_discrete_sequence=['brown'])
        fig.show()

# Example usage
if __name__ == "__main__":
    tracker = CaffeineChaos()
    tracker.simulate_intake(500)