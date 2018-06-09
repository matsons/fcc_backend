import pytest
import pdb

def test_timestamp(client):
    """API route should be present at
    [project_url]/api/timestamp/:date_string?
    """
    response = client.get('/api/timestamp/1')
    # pdb.set_trace()
    assert response.is_json
    """ invalid date strings rejected """
    pdb.set_trace()
    assert '{"error" : "Invalid Date"}' in response.get_json()
