import asyncio
import os
from tracardi.service.storage.driver import storage
from tracardi.service.storage.drivers.elastic_driver import ElasticDriver
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.domain.result import Result
from pytimeparse import parse


class EventCounter(ActionRunner):

    def __init__(self, **kwargs):
        pass

    async def run(self, payload) -> Result:
        wyniki = await storage.driver.event.search({
            "bool":{
                "must":[
                    {"range": {"metadata.time.insert":{"gte":"now-{}s".format(int(parse(payload["timeSpan"].strip("-")))), "lte":"now"}}},
                    {"match":{"type":payload["eventType"]}}
                ]
            }
        })
        return Result(port="payload", value=wyniki["hits"]["total"]["value"])


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='Event_Counter.plugin',
            className='EventCounter',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1',
            license="MIT",
            author="Dawid Kruk",
            init={}
        ),
        metadata=MetaData(
            name='Event_Counter',
            desc='This plugin reads how many events of defined type were triggered with defined time',
            type='flowNode',
            width=200,
            height=100,
            icon='icon',
            group=["General"]
        )
    )