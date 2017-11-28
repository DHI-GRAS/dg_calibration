from dg_calibration import gain_offset as go


def test_data_saninty():
    assert set(go.GAIN) == set(go.OFFSET)
    for k in go.GAIN:
        assert set(go.GAIN[k]) == set(go.OFFSET[k])


def test_get_gain_values():
    for sat_id in go.GAIN:
        vv = go.get_gain_values(sat_id)
        assert isinstance(vv, list)
        assert isinstance(vv[0], float)


def test_get_offset_values():
    for sat_id in go.OFFSET:
        vv = go.get_gain_values(sat_id)
        assert isinstance(vv, list)
        assert isinstance(vv[0], float)