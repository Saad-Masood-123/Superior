class SimpleReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature 
        self.heater="AC is off"

    def perceive(self, current_temperature):
        return current_temperature
    def act(self, current_temperature):
        if current_temperature < self.desired_temperature and self.heater=="AC is off":
            action = "Turn on heater"
            self.heater="AC is on"
        elif current_temperature >= self.desired_temperature and self.heater=="AC is on":
            self.heater="heater is on"
            action = "Turn on AC"
        else:
            action="Do Nothing"
        return action
rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}
desired_temperature =int(input("Enter Your Desire Temperature which do you want in your room  :"))
agent = SimpleReflexAgent(desired_temperature)
for room, temperature in rooms.items():
    action = agent.act(temperature)
    print(f"{room}: Current temperature = {temperature}°C.{action},prev_heater is {agent.heater}")