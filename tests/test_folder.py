from odoo.tests import TransactionCase

class TestAudioFolder(TransactionCase):

    def setUp(self):
        super(TestAudioFolder, self).setUp()
        self.AudioFolder = self.env['dudoxx.audio.folder']

    def test_create_audio_folder(self):
        folder = self.AudioFolder.create({
            'name': 'Test Folder',
        })
        self.assertEqual(folder.name, 'Test Folder')
