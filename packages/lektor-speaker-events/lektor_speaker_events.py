# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin


class SpeakerEventsPlugin(Plugin):
    name = 'Speaker Events'
    description = u'Lektor plugin that adds a function to filter events by speaker.'

    def on_setup_env(self, **extra):
        def speaker_events(eventos, speaker):
            filtered = []
            for evento in eventos:
                if evento["talks"]:
                    for talk in evento["talks"].blocks:
                        if speaker in talk["speaker"]:
                            filtered.append({"event": evento, "talk": talk})
            return filtered
        self.env.jinja_env.filters["speakerevents"] = speaker_events
