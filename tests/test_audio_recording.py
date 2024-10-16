from odoo.tests import TransactionCase

class TestAudioRecording(TransactionCase):

    def setUp(self):
        super(TestAudioRecording, self).setUp()
        self.AudioRecording = self.env['dudoxx.audio.recording']

    def test_create_audio_recording(self):
        recording = self.AudioRecording.create({
            'name': 'Test Recording',
            'duration': 120.0,
            'language_id': self.env.ref('base.lang_en').id,
            'transcription': 'This is a test transcription.',
        })
        self.assertEqual(recording.name, 'Test Recording')
        self.assertEqual(recording.duration, 120.0)
        self.assertEqual(recording.transcription, 'This is a test transcription.')
