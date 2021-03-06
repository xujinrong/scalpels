#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Kun Huang <academicgareth@gmail.com>

from scalpels.client import rpcapi
from scalpels.client import utils

UUID_LOWEST_SUPPORT = utils.UUID_LOWEST_SUPPORT
rpcapi = rpcapi.rpcapi


class API(object):
    def __init__(self):
        pass

    def get_tracer_list(self):
        return rpcapi.tracer_list()

    def start_tracers(self, tracers):
        rpcapi.start_tracers(tracers=tracers)

    def stop_tracers(self, tracers):
        rpcapi.stop_tracers(tracers=tracers)

    def stop_task(self, uuid):
        rpcapi.stop_task(uuid=uuid)

    def get_task(self, uuid, fuzzy=False):
        if fuzzy and len(uuid) < UUID_LOWEST_SUPPORT:
            raise ValueError("fuzzy uuid query must get %s length" %
                             UUID_LOWEST_SUPPORT)
        return rpcapi.get_task(uuid=uuid, fuzzy=fuzzy)

    def get_latest_task(self):
        return rpcapi.get_latest_task()

    def get_result(self, uuid):
        return rpcapi.get_result(uuid=uuid)

    def get_all_results(self):
        return rpcapi.get_all_results()

    def try_get_task_from_config(self, config):
        uuid = config.get("uuid")
        last = config.get("last")

        if last and uuid:
            raise ValueError("can't assign last and uuid togther")
        elif uuid:
            return self.get_task(uuid, fuzzy=True)
        else:  # no matter whether last is set
            return self.get_latest_task()

    def register_tracer(self, tracer_opts):
        if "name" not in tracer_opts:
            raise ValueError("tracer must have a name")
        if "tpl" not in tracer_opts:
            raise ValueError("tracer must have a name")
        rpcapi.register_tracer(tracer_opts=tracer_opts)

    def update_config(self, data_opts):
        rpcapi.update_config(data_opts=data_opts)

    def get_config(self):
        return rpcapi.get_config()

    def set_tracer_stat(self, tracer, running):
        rpcapi.set_tracer_stat(tracer=tracer, running=running)

    def set_tracer_pid(self, tracer, pid):
        rpcapi.set_tracer_pid(tracer=tracer, pid=pid)


api = API()
