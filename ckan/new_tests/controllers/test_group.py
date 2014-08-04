from nose.tools import assert_equal, assert_true

from routes import url_for

import ckan.new_tests.helpers as helpers
import ckan.model as model


class TestPackageControllerNew(helpers.FunctionalTestBase):

    @classmethod
    def setup_class(cls):
        super(cls, cls).setup_class()
        helpers.reset_db()

    def setup(self):
        model.repo.rebuild_db()

    def test_bulk_process_throws_404_for_nonexistent_org(self):
        app = self._get_test_app()
        response = app.get(url=url_for(controller='organization',
                            action='bulk_process', id='does-not-exist'),
                            status=404)
