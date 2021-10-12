from tracardi.domain.context import Context
from tracardi.domain.entity import Entity
from tracardi.domain.event import Event
from tracardi.domain.profile import Profile
from tracardi.domain.session import Session
from tracardi_plugin_sdk.service.plugin_runner import run_plugin

from Event_Counter.plugin import EventCounter

init = {}
payload = {"eventType": "page-view", "timeSpan":"-1h30min"}
profile = Profile(id="profile-id")
event = Event(id="event-id",
              type="event-type",
              profile=profile,
              session=Session(id="session-id"),
              source=Entity(id="source-id"),
              context=Context())
result = run_plugin(EventCounter, init, payload,
                    profile, event=event)

print("OUTPUT:", result.output)
print("PROFILE:", result.profile)