from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem, HardwareType, Popularity

# you can also import SoftwareEngine, HardwareType, SoftwareType, Popularity from random_user_agent.params
# you can also set number of user agents required by providing `limit` as parameter


user_agent_rotator = UserAgent(
    operating_systems=[OperatingSystem.ANDROID.value],
    hardware_types=[HardwareType.MOBILE.value],
    software_names=[SoftwareName.CHROME.value],
    Popularity=[Popularity.POPULAR.value],
    limit=100
)

# Get Random User Agent String.
user_agent = user_agent_rotator.get_random_user_agent()

print(user_agent)