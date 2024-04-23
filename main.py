#!/usr/bin/env python

from src.Application.App import App


app = App(storage='storage')

app.api_service().run()
