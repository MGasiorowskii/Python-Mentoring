import functionality.db_handler
import pytest
from functionality.db_handler import *


@pytest.mark.connect_to_database
def test_should_pass_for_expected_message(mocker):
    mocker.patch.object(functionality.db_Handler.Config, DB_URL, 'xd')

