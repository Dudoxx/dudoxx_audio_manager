from odoo.tests import TransactionCase

class TestAudioTranslation(TransactionCase):

    def setUp(self):
        super(TestAudioTranslation, self).setUp()
        self.AudioTranslation = self.env['dudoxx.audio.translation']
        self.AudioRecording = self.env['dudoxx.audio.recording'].create({
            'name': 'Test Recording',
            'duration': 120.0,
            'language_id': self.env.ref('base.lang_en').id,
            'transcription': 'This is a test transcription.',
        })

    def test_create_audio_translation(self):
        translation = self.AudioTranslation.create({
            'recording_id': self.AudioRecording.id,
            'language_id': self.env.ref('base.lang_fr').id,
            'translated_text': 'Ceci est une transcription de test.',
        })
        self.assertEqual(translation.recording_id, self.AudioRecording)
        self.assertEqual(translation.translated_text, 'Ceci est une transcription de test.')
