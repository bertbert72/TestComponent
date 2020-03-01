import time
import logging

from homeassistant.components.media_player import (
    MediaPlayerDevice, PLATFORM_SCHEMA)

DATA_COMPNAME = 'testcomponent'
_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_devices, discovery_info=None):
    hass.data[DATA_COMPNAME] = []
    hass.data[DATA_COMPNAME].append(TestComponent('testcomponent'))
    add_devices(hass.data[DATA_COMPNAME], True)


class TestComponent(MediaPlayerDevice):
    def __init__(self, comp_name):
        self._updatetime = time.time()
        self._updatecount = 0
        self._name = comp_name

        _LOGGER.info("Added [%s]", self._name)

    @property
    def name(self):
        return self._name

    @property
    def media_duration(self):
        return 100

    @property
    def media_position(self):
        return self._updatecount % 100

    @property
    def media_image_url(self):
        pic_url = "https://multiscreen-cdn-hgo-thumb.virginmedia.com/images/VM18/thumbnail.jpg"
        if time.time() - self._updatetime > 10:
            self._updatecount += 1
            self._updatetime = time.time()
            _LOGGER.info("Update count: [%d]", self._updatecount)
        return pic_url + "?" + str(self._updatecount)
