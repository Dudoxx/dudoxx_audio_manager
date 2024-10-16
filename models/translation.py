from odoo import models, fields

class AudioTranslation(models.Model):
    _name = 'dudoxx.audio.translation'
    _description = 'Audio Translation'

    recording_id = fields.Many2one('dudoxx.audio.recording', string='Related Audio Recording')
    language_id = fields.Many2one('res.lang', string='Language')
    translated_text = fields.Text(string='Translated Transcription')
    translator_id = fields.Many2one('res.users', string='Translator')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('reviewed', 'Reviewed'),
        ('approved', 'Approved')
    ], string='Status', default='draft')
