from odoo.tests import TransactionCase

class TestAudioChunk(TransactionCase):

    def setUp(self):
        super(TestAudioChunk, self).setUp()
        self.AudioChunk = self.env['dudoxx.audio.chunk']
        self.AudioRecording = self.env['dudoxx.audio.recording'].create({
            'name': 'Test Recording',
            'duration': 120.0,
            'language_id': self.env.ref('base.lang_en').id,
            'transcription': 'This is a test transcription.',
        })

    def test_create_audio_chunk(self):
        chunk = self.AudioChunk.create({
            'recording_id': self.AudioRecording.id,
            'start_time': 0.0,
            'end_time': 60.0,
            'transcription': 'This is a chunk transcription.',
        })
        self.assertEqual(chunk.recording_id, self.AudioRecording)
        self.assertEqual(chunk.start_time, 0.0)
        self.assertEqual(chunk.end_time, 60.0)
        self.assertEqual(chunk.transcription, 'This is a chunk transcription.')
