import cassiopeia
import pytest

from datapipelines.common import NotFoundError

from .constants import SUMMONER_NAME, UNKNOWN_SUMMONER_NAME


def test_unknown_summoner():
    assert not cassiopeia.get_summoner(name=UNKNOWN_SUMMONER_NAME, region="NA").exists


def test_equal_summoners():
    from_name = cassiopeia.get_summoner(name=SUMMONER_NAME, region="NA")
    from_id = cassiopeia.get_summoner(id=from_name.id, region="NA")

    assert from_name.id == from_id.id
    assert from_name.name == from_id.name
    assert from_name == from_id
    assert from_name.to_dict() == from_id.to_dict()


def test_can_get_league_entries():
    config_backup = cassiopeia.configuration.settings
    cassiopeia.apply_settings({"global": {"default_region": "NA"}})
    summoner = cassiopeia.Summoner(name=SUMMONER_NAME)
    summoner.league_entries
    # restore global settings to not affect other tests if they are run in one session
    cassiopeia.apply_settings(config_backup)
