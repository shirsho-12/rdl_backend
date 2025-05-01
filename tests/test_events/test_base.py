from unittest import TestCase
from fastapi.testclient import TestClient
from rdl_backend.app.application import create_application


class TestBaseEventHandler(TestCase):
    def test_startup_handler(self):
        app = create_application()
        with self.assertLogs('rdl_backend', level='INFO') as cm:

            with TestClient(app):
                pass
            self.assertEqual(cm.output,
                             ['INFO:rdl_backend:Starting up ...',
                              'INFO:rdl_backend:Shutting down ...'])
